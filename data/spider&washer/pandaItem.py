import pandas as pd


def process_item_description(df):
    # 处理描述字段，去除 HTML 标签，并将其分割成列表
    df['des1'] = df['des1'].apply(
        lambda x: [desc.strip() for desc in x.replace('<p>', '').replace('</p>', '').split('<br>')] if isinstance(x,
                                                                                                                  str) else x)
    if 'des2' in df.columns:
        df['des2'] = df['des2'].apply(
            lambda x: [desc.strip() for desc in x.replace('<p>', '').replace('</p>', '').split('<br>')] if isinstance(x,
                                                                                                                      str) else x)
    return df


def read_process_write(input_file, output_file):
    # 读取 JSON 文件到 DataFrame
    df = pd.read_json(input_file)

    # 处理数据
    processed_df = process_item_description(df)

    # 将处理后的 DataFrame 输出到 JSON 文件
    processed_df.to_json(output_file, force_ascii=False, orient='records', indent=4)


# 指定输入和输出文件路径
input_filename = 'items.json'
output_filename = 'processed_items.json'
read_process_write(input_filename, output_filename)
