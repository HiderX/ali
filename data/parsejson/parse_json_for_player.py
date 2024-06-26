import os
import json


def generate_insert_statements(json_data):
    insert_statements = []
    players = json_data.get('data', {}).get('battle_player_list', [])

    for player in players:
        team_id = player['team_id']
        player_name = player['player_name']
        player_icon = player['player_icon']

        insert_statement = f"INSERT INTO Player (team_id, player_name, player_icon) VALUES ({team_id}, '{player_name}', '{player_icon}');"
        insert_statements.append(insert_statement)

    return insert_statements


def write_statements_to_file(statements, output_file):
    with open(output_file, 'a', encoding='utf-8') as file:
        for statement in statements:
            file.write(statement + '\n')


def process_json_files(root_folder, output_file):
    for subdir, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    try:
                        json_data = json.load(json_file)
                        insert_statements = generate_insert_statements(json_data)
                        write_statements_to_file(insert_statements, output_file)
                    except json.JSONDecodeError:
                        print(f"Failed to decode JSON from file: {file_path}")


if __name__ == "__main__":
    root_folder = r'D:\Project\ali\match\match_info'  # Replace with the path to your root folder
    output_file = 'player.sql'  # Replace with the desired output file path

    # Clear the output file before starting
    open(output_file, 'w').close()

    process_json_files(root_folder, output_file)
    print(f"SQL insert statements have been written to {output_file}")
