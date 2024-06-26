import os
import json


def parse_json_files(directory):
    import_statements = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)

                # Extracting the information from the JSON data
                results = data.get("results", [])
                for result in results:
                    match_id = result.get("match_id")
                    camp1 = result.get("camp1", {})
                    camp2 = result.get("camp2", {})

                    if match_id:
                        for camp, team_info in enumerate([camp1, camp2], start=1):
                            team_id = team_info.get("team_id")
                            is_win = team_info.get("is_win", False)
                            score = team_info.get("score", 0)

                            if team_id:
                                # Create the SQL import statement
                                import_statement = (
                                    f"INSERT INTO team_participate_in_match (team_id, match_id, camp, is_win, score) "
                                    f"VALUES ({team_id}, {match_id}, {camp}, {str(is_win).upper()}, {score});"
                                )
                                import_statements.append(import_statement)

    return import_statements


def write_to_file(output_file, import_statements):
    with open(output_file, 'w', encoding='utf-8') as file:
        for statement in import_statements:
            file.write(statement + '\n')


if __name__ == "__main__":
    input_directory = r'D:\Project\ali\match\league_info'  # replace with your directory path
    output_file = 'team_participate_in_match.sql'

    # Parse JSON files and generate import statements
    import_statements = parse_json_files(input_directory)

    # Write the import statements to a file
    write_to_file(output_file, import_statements)
