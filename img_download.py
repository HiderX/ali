import requests
import os
import requestparams


def download_images(base_url_template, ids, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)  # 创建保存图片的目录，如果不存在
    for item_id in ids:
        # 使用 f-string 格式化 URL
        url = base_url_template.format(item_id)
        # 发送请求
        response = requests.get(url, headers=requestparams.headers)
        if response.status_code == 200:
            # 图片下载成功
            file_path = os.path.join(save_dir, f"{item_id}.jpg")
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"下载成功：{url}")
        else:
            print(f"下载失败：{url}，状态码：{response.status_code}")
