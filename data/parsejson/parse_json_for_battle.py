import os
import json


def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)['data']

    battle_id = data['battle_id']
    battle_seq = data['battle_seq']
    win_camp = data['win_camp']
    insert_statements = []
    insert_statement = f"INSERT INTO Battle (battle_id, battle_seq, win_camp) VALUES ('{battle_id}', {battle_seq}, {win_camp});"

    insert_statements.append(insert_statement)

    return insert_statements


def process_all_json_files(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        insert_statements = process_json_file(file_path)
                        for stmt in insert_statements:
                            out_file.write(stmt)
                            out_file.write('\n')
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")


# 使用示例
input_folder = r'D:\Project\ali\match\match_info'
output_file = 'battle.sql'

process_all_json_files(input_folder, output_file)
