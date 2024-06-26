-- 通过战队找这个战队打过的match，按照时间降序排列，点一场match之后可以或许可以跳转到通过match找battle的页面
WITH win_los_team AS(
SELECT 
	tp1.match_id,
    tp1.team_id AS winning_team_id, 
    tp2.team_id AS losing_team_id,
	t1.team_name AS winning_team_name, 
    t2.team_name AS losing_team_name,
    tp1.score AS winning_score, 
    tp2.score AS losing_score
FROM 
    team_participate_in_match tp1
JOIN 
    team_participate_in_match tp2 
ON 
    tp1.match_id = tp2.match_id
CROSS JOIN team t1 CROSS JOIN team t2 
WHERE 
    tp1.is_win = 1 
    AND tp2.is_win = 0
		AND tp1.team_id = t1.team_id
		AND tp2.team_id = t2.team_id
		-- AND tp1.match_id = 2019000403
),
my_match_with_opponent AS(
SELECT 
    match_id,
--     team_id,
		team_name AS my_name,
--     CASE
--         WHEN team_id = winning_team_id THEN losing_team_id
--         ELSE winning_team_id 
--     END AS opponent_team_id,
		CASE
        WHEN team_id = winning_team_id THEN losing_team_name
        ELSE winning_team_name 
    END AS opponent_team_name,
		CASE
        WHEN team_id = winning_team_id THEN 1
        ELSE 0 
    END AS is_win,
		CASE
        WHEN team_id = winning_team_id THEN winning_score
        ELSE losing_score 
    END AS my_score,
		CASE
        WHEN team_id = winning_team_id THEN losing_score
        ELSE winning_score 
    END AS opponent_score
		
FROM 
    team, win_los_team
WHERE 
    team.team_id = 10001
    AND (winning_team_id = 10001 OR losing_team_id = 10001)
),
my_matches AS(
SELECT 
    match_id,
    my_name,
    opponent_team_name,
    is_win,
    my_score,
    opponent_score,
    bo,
    start_time,
    end_time,
    match_address
    FROM my_match_with_opponent NATURAL JOIN matches 
)
SELECT 
    league_name,
    my_matches.match_id,
    my_name,
    opponent_team_name,
    is_win,
    my_score,
    opponent_score,
    bo,
    my_matches.start_time,
    my_matches.end_time,
    match_address
FROM my_matches 
JOIN match_belongs ON my_matches.match_id = match_belongs.match_id
JOIN league ON league.league_id = match_belongs.league_id
ORDER BY my_matches.start_time DESC;