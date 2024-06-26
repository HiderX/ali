
-- 统计某一特定战队的数据，目前的排序顺序是按照参加的对局数量排的，这都可以调，并且也可以加入选择条件，在下面的SELECT中加WHERE条件就行了，就像注释掉的那样
WITH team_game_stats AS (
    SELECT 
        battle_id,
        battle_seq,
        camp,
        CASE
            WHEN camp = 1 THEN '红'
            WHEN camp = 2 THEN '蓝'
            ELSE 'NULL' 
        END AS camp_color,
        team_id,
        team_name,
        team_icon,
        is_win,
        kill_num,
        assist_num,
        death_num,
        (kill_num + assist_num) / NULLIF(death_num, 1) AS kda, -- 确保不会被0除
        gold,
        push_tower_num,
        kill_big_dragon_num,
        kill_tyrant_num,
        kill_dark_tyrant_num,
        kill_prophet_dragon_num,
        kill_shadow_dragon_num,
        kill_storm_dragon_king_num
    FROM 
        team_participate_in_battle 
    NATURAL JOIN 
        battle_belongs 
    NATURAL JOIN 
        battle 
    NATURAL JOIN 
        team 
    ORDER BY 
        battle_seq, camp
)
SELECT 
    team_id,
    team_name,
    COUNT(battle_id) AS total_games,
    AVG(is_win) AS average_win_rate,
    AVG(kda) AS average_kda,
    AVG(kill_num) AS average_kills,
    AVG(death_num) AS average_deaths,
    AVG(assist_num) AS average_assists,
    AVG(gold) AS average_gold,
    AVG(push_tower_num) AS average_push_tower,
    AVG(kill_big_dragon_num) AS average_kill_big_dragon,
    AVG(kill_tyrant_num) AS average_kill_tyrant,
    AVG(kill_dark_tyrant_num) AS average_kill_dark_tyrant,
    AVG(kill_prophet_dragon_num) AS average_kill_prophet_dragon,
    AVG(kill_shadow_dragon_num) AS average_kill_shadow_dragon,
    AVG(kill_storm_dragon_king_num) AS average_kill_storm_dragon_king
FROM 
    team_game_stats
-- WHERE 
--     team_name like '%超玩会%'
GROUP BY 
    team_id, 
    team_name
ORDER BY COUNT(battle_id) DESC;