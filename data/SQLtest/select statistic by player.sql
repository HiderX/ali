-- 查询某一特定player的数据，目前的排序顺序是按照参加的对局数量排的，这都可以调，并且也可以加入选择条件，在下面的SELECT中加WHERE条件就行了，就像注释掉的那样
WITH ranked_data AS (
    SELECT 
        CONCAT(team_name, '.', player_name) AS team_player_name, 
        battle_id,
        is_win,
        kda,
        kill_num,
        death_num,
        assist_num,
        hurt_total,
        be_hurt_total,
        hero_name,
        summoner_name,
        RANK() OVER (PARTITION BY player_name ORDER BY COUNT(hero_name) DESC) AS hero_rank,
        RANK() OVER (PARTITION BY player_name ORDER BY COUNT(summoner_name) DESC) AS summoner_rank
FROM 
    a_player_plays_a_game 
NATURAL JOIN 
    Team 
NATURAL JOIN 
    Hero
NATURAL JOIN 
    Summoner
    GROUP BY 
        player_name, 
		team_name,
        battle_id, 
        hero_name, 
        summoner_name, 
        is_win, 
        kda, 
        kill_num, 
        death_num, 
        assist_num, 
        hurt_total, 
        be_hurt_total
)
SELECT 
    team_player_name,
    COUNT(battle_id) AS total_games,
    AVG(is_win) AS average_win_rate,
    AVG(kda) AS average_kda,
    AVG(kill_num) AS average_kills,
    AVG(death_num) AS average_deaths,
    AVG(assist_num) AS average_assists,
    AVG(hurt_total) AS average_damage_done,
    AVG(be_hurt_total) AS average_damage_taken,
    MAX(CASE WHEN hero_rank = 1 THEN hero_name END) AS most_used_hero,
    MAX(CASE WHEN summoner_rank = 1 THEN summoner_name END) AS most_used_summoner_skill
FROM 
    ranked_data
-- WHERE team_player_name like '%Fly%'
GROUP BY 
    team_player_name
ORDER BY COUNT(battle_id) DESC;