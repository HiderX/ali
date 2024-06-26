import json
import img_download

with open('items.json', 'r') as file:
        datas = json.load(file)

item_ids = []

for item in datas:
    item_ids.append(item.get("item_id"))

base_url_template = 'https://game.gtimg.cn/images/yxzj/img201606/itemimg/{}.jpg'  # 使用 {} 作为占位符
save_dir = 'items'  # 设置保存图片的目录

img_download.download_images(base_url_template,item_ids, save_dir)