import os
import json


def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)['data']

    battle_id = data['battle_id']

    teams = [data['camp1'], data['camp2']]
    insert_statements = []

    for team in teams:
        team_id = team['team_id']
        is_win = team['is_win']
        camp = 1 if team_id == teams[0]['team_id'] else 2
        kill_num = team['kill_num']
        assist_num = team['assist_num']
        death_num = team['death_num']
        gold = team['gold']
        kill_big_dragon_num = team['kill_big_dragon_num']
        push_tower_num = team['push_tower_num']
        kill_dark_tyrant_num = team['kill_dark_tyrant_num']
        kill_tyrant_num = team['kill_tyrant_num']
        kda = team['kda']
        kill_prophet_dragon_num = team['kill_prophet_dragon_num']
        kill_shadow_dragon_num = team['kill_shadow_dragon_num']
        kill_storm_dragon_king_num = team['kill_storm_dragon_king_num']

        insert_statement = f"""
        INSERT INTO team_participate_in_battle (
            team_id, battle_id, camp, is_win, kill_num, assist_num, death_num, gold, 
            kill_big_dragon_num, push_tower_num, kill_dark_tyrant_num, kill_tyrant_num, kda, 
            kill_prophet_dragon_num, kill_shadow_dragon_num, kill_storm_dragon_king_num
        ) VALUES (
            {team_id}, '{battle_id}', {camp}, {str(is_win).upper()}, {kill_num}, {assist_num}, {death_num}, {gold}, 
            {kill_big_dragon_num}, {push_tower_num}, {kill_dark_tyrant_num}, {kill_tyrant_num}, {kda}, 
            {kill_prophet_dragon_num}, {kill_shadow_dragon_num}, {kill_storm_dragon_king_num}
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
output_file = 'team_participate_in_battle.sql'

process_all_json_files(input_folder, output_file)
