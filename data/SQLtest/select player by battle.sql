
-- 通过battle找一场比赛中每一个player的信息
-- 接下来这个界面是一个battle的信息，我感觉可以在上面显示两支战队参加这个battle的信息（即这场battle的总的信息）（这可以通过在上面的那个查询的where子句中加一个AND battle_id =的条件实现），然后在下面分别显示十个选手的信息
-- 这是找赢了的队伍的信息的，返回五条记录，mvp排在最前面
SELECT 
	battle_id,
    team_id,
	team_name,
	player_name,
    CONCAT(team_name, '.', player_name) AS team_player_name,  -- 拼接 team_name 和 player_name
    player_icon,
    hero_name,
    summoner_name,
    camp,
		CASE
        WHEN camp = 1 THEN '红'
        WHEN camp = 2 THEN '蓝'
        ELSE 'NULL' 
    END AS camp_color,  -- 根据 camp 映射为红或蓝
    participation_rate,
    is_mvp,
    mvp_score,
    kill_num,
    assist_num,
    death_num,
    gold,
    hurt_total,
    be_hurt_total,
    kda,
    hurt_total_rate,
    be_hurt_total_rate,
    hurt_to_hero_total,
    be_hurt_by_hero_total,
    hurt_to_hero_total_rate,
    be_hurt_by_hero_total_rate
FROM 
    a_player_plays_a_game 
NATURAL JOIN 
    Battle 
NATURAL JOIN 
    Team 
NATURAL JOIN 
    Hero
NATURAL JOIN 
    Summoner
NATURAL LEFT OUTER JOIN 
    player
WHERE 
    battle_id= '1054884368_34_1716027538'
	AND is_win = 1
ORDER BY
	is_mvp DESC;