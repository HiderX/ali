import json

# 等更新后的json文件，并且不确定代码是不是有问题

# JSON data
# 来自heroinfo文件

with open(r"D:\Project\ali\heroinfo.json", "r", encoding='utf-8') as f:
    data = json.load(f)

# data = json.loads(json_data)

# Generate INSERT statements
insert_statements = []
for hero in data:
    hero_id = hero['ename']
    for skill in hero['skills']:
        skill_name = skill['Skill Name']
        cooldown = skill['Cooldown']
        cost = skill['Cost']
        description = skill['Description'].replace("'", "''")  # Escape single quotes
        image_source = skill['Image Source']

        insert_statement = (
            f"INSERT INTO hero_skill (hero_id, skill_name, cooldown, cost, description, image_source) "
            f"VALUES ({hero_id}, '{skill_name}', '{cooldown}', {cost}, '{description}', '{image_source}');"
        )
        insert_statements.append(insert_statement)

# Write to a file
with open('hero_skill.sql', 'w', encoding='utf-8') as file:
    file.write('\n'.join(insert_statements))

print("INSERT statements have been written to hero_skill_inserts.sql")
