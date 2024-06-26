import os
import json


def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f).get('data', None)
            if data is None:
                print(f"No 'data' key found in {file_path}")
                return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {file_path}: {e}")
            return []

    battle_id = data.get('battle_id', None)
    if battle_id is None:
        print(f"No 'battle_id' found in {file_path}")
        return []

    insert_statements = []

    for player in data.get('battle_player_list', []):
        team_id = player.get('team_id', 'NULL')
        player_name = player.get('player_name', 'NULL').replace("'", "''")

        for equip in player.get('BriefEquipList', []):
            item_id = equip.get('equip_id', 'NULL')

            insert_statement = f"""
            INSERT INTO use_item (
                team_id, player_name, battle_id, item_id
            ) VALUES (
                {team_id}, '{player_name}', '{battle_id}', {item_id}
            );
            """
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
output_file = 'use_item.sql'

process_all_json_files(input_folder, output_file)
