import json

import img_download

with open('summoner.json', 'r') as file:
    datas = json.load(file)
summoner_ids = []
for item in datas:
    strs = str(item.get("summoner_id"))
    summoner_ids.append(strs)
    summoner_ids.append(strs + "-big")

base_url_template = 'https://game.gtimg.cn/images/yxzj/img201606/summoner/{}.jpg'  # 使用 {} 作为占位符
save_dir = 'summoners'  # 设置保存图片的目录

img_download.download_images(base_url_template, summoner_ids, save_dir)
