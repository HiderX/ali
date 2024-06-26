import json
import threading
from concurrent.futures import ThreadPoolExecutor
import requests

import img_download
import requestparams

from bs4 import BeautifulSoup  # 网页解析

with open('processed_heroes.json', 'r') as file:
    datas = json.load(file)

all_data = []
lock = threading.Lock()


def getEname(data):
    return data['ename']


def getInfo(item):
    ename = str(item.get("ename"))
    url = f"https://pvp.qq.com/web201605/herodetail/{item.get('id_name')}.shtml"
    response = requests.get(url=url, headers=requestparams.headers)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.content, "html.parser")
    data = {}
    data['ename'] = ename
    cover_list = soup.find('ul', class_="cover-list")
    lis = cover_list.find_all('li')
    for li in lis:
        label = li.find('em').text.strip()
        percentage = li.find('i')['style'].split(':')[1].strip()
        data[label] = percentage

    visible_skills = soup.find_all('div', class_='show-list')

    skill_data = []
    for idx, skill in enumerate(visible_skills):
        # Extract skill name
        skill_name_element = skill.find('p', class_='skill-name')
        skill_name = skill_name_element.find('b').text.strip()

        if not skill_name:
            continue

        # Extract cooldown and cost
        cooldown = skill_name_element.find_all('span')[0].text.strip().split('：')[1]
        cost = skill_name_element.find_all('span')[1].text.strip().split('：')[1]

        # Extract skill description
        skill_desc = skill.find('p', class_='skill-desc').text.strip()

        # Fetch corresponding image source
        img_base_url = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/"

        skill_data.append({
            'Skill Name': skill_name,
            'Cooldown': cooldown,
            'Cost': cost,
            'Description': skill_desc,
            'Image Source': img_base_url + ename + "/" + ename + str(idx) + "0.png"
        })

    data['skills'] = []
    for skill in skill_data:
        data['skills'].append(skill)

    story_div = soup.find('div', class_='pop-story')

    # Extract paragraphs within the story
    paragraphs = story_div.find_all('p')

    story = ""
    # Print each paragraph's text
    for p in paragraphs:
        if p == paragraphs[0]:
            story += (p.get_text(strip=True))
        else:
            story += "\n" + (p.get_text(strip=True))

    data['hero-story'] = story

    with lock:
        all_data.append(data)


def getImg(item):
    ename = str(item.get("ename"))
    base_url_template = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/" + ename + "/{}.jpg"
    skin_ids = []
    for i in range(1, len(item.get("skin_name")) + 1):
        skin_ids.append(ename + "-smallskin-" + str(i))
        skin_ids.append(ename + "-bigskin-" + str(i))
    img_download.download_images(base_url_template, skin_ids, f"skins/{ename}")


if __name__ == "__main__":
    with ThreadPoolExecutor(8) as t:
        for item in datas:
            t.submit(getInfo, item=item)

    print(all_data)
    all_data.sort(key=getEname)

    with open("heroinfo.json", "w", encoding='utf8') as f:
        json.dump(all_data, f, ensure_ascii=False)

    with ThreadPoolExecutor(8) as t:
        for item in datas:
            t.submit(getImg, item=item)
