-- 通过league找match，通过赛事id查找，返回比赛id,bo信息，起止时间，地点，胜利和失败的队伍的id,名称,比分
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
)
SELECT
	match_id,
	bo,
	start_time,
	end_time,
	match_address,
	winning_team_id,
	winning_team_name,
	winning_score,
	losing_team_id,
	losing_team_name,
	losing_score
FROM match_belongs 
NATURAL JOIN win_los_team NATURAL JOIN matches 
where league_id = 20190004;