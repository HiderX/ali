-- 数据获取：
-- League：leagues.json
-- Match：match/league_info
-- match_belongs：match/league_info
-- Battle：match/match_info
-- battle_belongs：match/match_info (暂时感觉用处不大)
-- Team：match/match_info
-- team_participate_in_match：match/league_info
-- team_participate_in_battle：match/match_info
-- Player：match/match_info
-- Hero：processed_heroes.json
-- Hero_Skin：processed_heroes.json
-- Item：processed_items.json
-- Summoner：summoner.json
-- Ming：processed_ming.json
-- a_player_plays_a_game：match/match_info
-- use_item：match/match_info
-- hero_skill：heroinfo.json

CREATE TABLE League (
    league_id INT PRIMARY KEY,
    league_type_name VARCHAR(50) NOT NULL,
    start_time DATETIME,
    is_top BOOLEAN,
    end_time DATETIME,
    league_name VARCHAR(100) NOT NULL,
    season INT,
    year INT,
    league_icon VARCHAR(1024)
);

CREATE TABLE matches (
    match_id BIGINT PRIMARY KEY,
    bo INT,
    start_time DATETIME,
    end_time DATETIME,
    match_address VARCHAR(100),
    win_camp INT
);

CREATE TABLE match_belongs (
    match_id BIGINT,
    league_id INT,
    PRIMARY KEY (match_id, league_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (league_id) REFERENCES League(league_id)
);

CREATE TABLE Battle (
    battle_id VARCHAR(255) PRIMARY KEY,
    battle_seq INT NOT NULL,
    win_camp INT
);

CREATE TABLE battle_belongs (
    battle_id VARCHAR(255),
    match_id BIGINT,
    PRIMARY KEY (battle_id, match_id),
    FOREIGN KEY (battle_id) REFERENCES Battle(battle_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);

CREATE TABLE Team (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    team_icon VARCHAR(1024)
);

CREATE TABLE team_participate_in_match (
    team_id INT,
    match_id BIGINT,
    camp INT,
    is_win BOOLEAN,
    score INT,
    PRIMARY KEY (team_id, match_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (match_id) REFERENCES matches(match_id)
);

CREATE TABLE team_participate_in_battle (
    team_id INT,
    battle_id VARCHAR(255),
    camp INT,
    is_win BOOLEAN,
    kill_num INT,
    assist_num INT,
    death_num INT,
    gold INT,
    kill_big_dragon_num INT,
    push_tower_num INT,
    kill_dark_tyrant_num INT,
    kill_tyrant_num INT,
    kda FLOAT,
    kill_prophet_dragon_num INT,
    kill_shadow_dragon_num INT,
    kill_storm_dragon_king_num INT,
    PRIMARY KEY (team_id, battle_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (battle_id) REFERENCES Battle(battle_id)
);

CREATE TABLE Player (
    team_id INT,
    player_name VARCHAR(100),
    player_icon VARCHAR(1024),
    PRIMARY KEY (team_id, player_name),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);

CREATE TABLE Hero (
    hero_id INT PRIMARY KEY,
    hero_name VARCHAR(100) NOT NULL,
    title VARCHAR(100),
    hero_type VARCHAR(100)
);

CREATE TABLE Hero_Skin (
    hero_id INT,
    skin_name VARCHAR(100),
    skin_id INT,
    PRIMARY KEY (hero_id, skin_id),
    FOREIGN KEY (hero_id) REFERENCES Hero(hero_id)
);

CREATE TABLE Item (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_type INT,
    price INT,
    total_price INT
);

CREATE TABLE Summoner (
    summoner_id INT PRIMARY KEY,
    summoner_name VARCHAR(100) NOT NULL,
    summoner_rank VARCHAR(50),
    summoner_description TEXT
);

CREATE TABLE Ming (
    ming_id INT PRIMARY KEY,
    ming_type VARCHAR(50),
    ming_grade INT,
    ming_name VARCHAR(100),
    ming_des TEXT
);

CREATE TABLE a_player_plays_a_game (
    team_id INT,
    player_name VARCHAR(100),
    battle_id VARCHAR(255),
    hero_id INT,
    summoner_id INT,
    is_win BOOLEAN,
    is_lose_mvp BOOLEAN,
    camp INT,
    participation_rate FLOAT,
    is_mvp BOOLEAN,
    kill_num INT,
    assist_num INT,
    death_num INT,
    gold INT,
    hurt_total INT,
    be_hurt_total INT,
    kda FLOAT,
    hurt_total_rate FLOAT,
    be_hurt_total_rate FLOAT,
    mvp_score FLOAT,
    hurt_to_hero_total INT,
    be_hurt_by_hero_total INT,
    hurt_to_hero_total_rate FLOAT,
    be_hurt_by_hero_total_rate FLOAT,
    PRIMARY KEY (team_id, player_name, battle_id),
    -- FOREIGN KEY (team_id, player_name) REFERENCES Player(team_id, player_name),
    FOREIGN KEY (battle_id) REFERENCES Battle(battle_id),
    FOREIGN KEY (hero_id) REFERENCES Hero(hero_id),
    FOREIGN KEY (summoner_id) REFERENCES Summoner(summoner_id)
);

CREATE TABLE use_item (
    team_id INT,
    player_name VARCHAR(100),
    battle_id VARCHAR(255),
    item_id INT,
    PRIMARY KEY (team_id, player_name, battle_id, item_id),
    FOREIGN KEY (team_id, player_name) REFERENCES Player(team_id, player_name),
    FOREIGN KEY (battle_id) REFERENCES Battle(battle_id),
    FOREIGN KEY (item_id) REFERENCES Item(item_id)
);

CREATE TABLE hero_skill (
    hero_id INT,
    skill_name VARCHAR(100),
    cooldown VARCHAR(100),
    cost VARCHAR(100),
    description TEXT,
    image_source VARCHAR(1024),
    PRIMARY KEY (hero_id, skill_name),
    FOREIGN KEY (hero_id) REFERENCES Hero(hero_id)
);



create table hero_pos(
	hero_type INT PRIMARY KEY,
	pos VARCHAR(10)
);



create table item_pos(
	item_type INT PRIMARY KEY,
	pos VARCHAR(10)
);