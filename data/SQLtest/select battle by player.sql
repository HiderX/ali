-- 通过选手找这个选手打过的battle的信息，这里我默认按时间降序排序了，但其实也可以实现其他的排序的功能，比如按照击杀数排序，评分排序等等
WITH with_out_league_info AS(
SELECT 
	battle_id,
	match_id,
    team_id,
	team_name,
	player_name,
    CONCAT(team_name, '.', player_name) AS team_player_name,  -- 拼接 team_name 和 player_name
		matches.start_time,
		is_win,
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
NATURAL JOIN battle_belongs
NATURAL JOIN matches
WHERE 
  player_name like '%F%'
)
SELECT 
    battle_id,
    with_out_league_info.match_id,
	league_name,
    team_id,
    team_name,
    player_name,
    team_player_name,
	with_out_league_info.start_time,
	is_win,
    player_icon,
    hero_name,
    summoner_name,
    camp,
	camp_color,
    participation_rate,
    is_mvp,
    mvp_score,
    kill_num,
    assist_num,
    death_num,
	kda,
    gold,
    hurt_total,
    be_hurt_total,
    hurt_total_rate,
    be_hurt_total_rate,
    hurt_to_hero_total,
    be_hurt_by_hero_total,
    hurt_to_hero_total_rate,
    be_hurt_by_hero_total_rate
FROM with_out_league_info 
JOIN match_belongs ON with_out_league_info.match_id = match_belongs.match_id
JOIN league ON league.league_id = match_belongs.league_id
ORDER BY start_time DESC;