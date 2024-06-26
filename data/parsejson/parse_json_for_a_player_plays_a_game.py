import os
import json


def process_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)['data']

    battle_id = data['battle_id']
    insert_statements = []

    for player in data['battle_player_list']:
        team_id = player['team_id']
        player_name = player['player_name']
        hero_id = player['hero_id']
        summoner_id = player['SummonerAbilityInfo']['summoner_ability_id']
        is_win = player['camp'] == data['win_camp']
        is_lose_mvp = player['is_lose_mvp']
        camp = player['camp']
        participation_rate = player['participation_rate']
        is_mvp = player['is_mvp']
        kill_num = player['kill_num']
        assist_num = player['assist_num']
        death_num = player['death_num']
        gold = player['gold']
        hurt_total = player['hurt_total']
        be_hurt_total = player['be_hurt_total']
        kda = player['kda']
        hurt_total_rate = player['hurt_total_rate']
        be_hurt_total_rate = player['be_hurt_total_rate']
        mvp_score = player['mvp_score']
        hurt_to_hero_total = player['hurt_to_hero_total']
        be_hurt_by_hero_total = player['be_hurt_by_hero_total']
        hurt_to_hero_total_rate = player['hurt_to_hero_total_rate']
        be_hurt_by_hero_total_rate = player['be_hurt_by_hero_total_rate']

        insert_statement = f"""
        INSERT INTO a_player_plays_a_game (
            team_id, player_name, battle_id, hero_id, summoner_id, is_win, is_lose_mvp, camp, 
            participation_rate, is_mvp, kill_num, assist_num, death_num, gold, hurt_total, 
            be_hurt_total, kda, hurt_total_rate, be_hurt_total_rate, mvp_score, 
            hurt_to_hero_total, be_hurt_by_hero_total, hurt_to_hero_total_rate, be_hurt_by_hero_total_rate
        ) VALUES (
            {team_id}, '{player_name}', '{battle_id}', {hero_id}, {summoner_id}, {str(is_win).upper()}, {is_lose_mvp}, {camp}, 
            {participation_rate}, {is_mvp}, {kill_num}, {assist_num}, {death_num}, {gold}, {hurt_total}, 
            {be_hurt_total}, {kda}, {hurt_total_rate}, {be_hurt_total_rate}, {mvp_score}, 
            {hurt_to_hero_total}, {be_hurt_by_hero_total}, {hurt_to_hero_total_rate}, {be_hurt_by_hero_total_rate}
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



input_folder = r'D:\Project\ali\match\match_info'
output_file = 'a_player_plays_a_game.sql'

process_all_json_files(input_folder, output_file)
