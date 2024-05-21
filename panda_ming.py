import pandas as pd
import json


def process_item_description(df):
    # 处理描述字段，去除 HTML 标签，并将其分割成列表
    df['ming_des'] = df['ming_des'].apply(
        lambda x: x.replace('<p>', '').replace('</p>', '').strip())
    return df


def read_process_write(input_file, output_file):
    # 读取 JSON 文件到 DataFrame
    df = pd.read_json(input_file)

    # 处理数据
    processed_df = process_item_description(df)

    # 将处理后的 DataFrame 输出到 JSON 文件
    processed_df.to_json(output_file, force_ascii=False, orient='records', indent=4)


# 指定输入和输出文件路径
input_filename = 'ming.json'
output_filename = 'processed_ming.json'
read_process_write(input_filename, output_filename)
