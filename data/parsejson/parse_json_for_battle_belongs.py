import os
import json

def generate_import_statements(root_folder, output_file):
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as output:
        # Walk through the root folder
        for subdir, _, files in os.walk(root_folder):
            # Get the name of the subdirectory (match_id)
            match_id = os.path.basename(subdir)
            # Ensure the match_id is numeric
            if match_id.isdigit():
                # Iterate through all the files in the subdirectory
                for file in files:
                    # Process only JSON files
                    if file.endswith('.json'):
                        file_path = os.path.join(subdir, file)
                        try:
                            # Open and load the JSON file
                            with open(file_path, 'r', encoding='utf-8') as f:
                                data = json.load(f)
                                # Get the battle_id from the JSON data
                                _data = data.get("data")
                                battle_id = _data.get("battle_id")
                                # If battle_id is present, write the SQL insert statement
                                if battle_id:
                                    statement = f"INSERT INTO battle_belongs (battle_id, match_id) VALUES ('{battle_id}', {match_id});\n"
                                    output.write(statement)
                        except Exception as e:
                            # Print any errors encountered
                            print(f"Error processing file {file_path}: {e}")

if __name__ == "__main__":
    # Define the path to the root folder
    root_folder = r'D:\Project\ali\match\match_info'  # Replace with the path to your root folder
    # Define the path to the output file
    output_file = 'battle_belongs.sql'
    # Call the function to generate import statements
    generate_import_statements(root_folder, output_file)
    # Inform the user that the script has completed
    print(f"SQL import statements have been written to {output_file}")
