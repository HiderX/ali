package model

type League struct {
	LeagueId       int    `json:"league_id" db:"league_id"`
	LeagueName     string `json:"league_name" db:"league_name"`
	Season         int    `json:"season" db:"season"`
	LeagueTypeName string `json:"league_type_name" db:"league_type_name"`
	StartTime      string `json:"start_time" db:"start_time"`
	EndTime        string `json:"end_time" db:"end_time"`
	Year           int    `json:"year" db:"year"`
	LeagueIcon     string `json:"league_icon" db:"league_icon"`
}

type Match struct {
	MatchID         string `json:"match_id" db:"match_id"`
	BO              int    `json:"bo" db:"bo"`
	StartTime       string `json:"start_time" db:"start_time"`
	EndTime         string `json:"end_time" db:"end_time"`
	MatchAddress    string `json:"match_address" db:"match_address"`
	WinningTeamId   int    `json:"winning_team_id" db:"winning_team_id"`
	WinningTeamName string `json:"winning_team_name" db:"winning_team_name"`
	WinningScore    int    `json:"winning_score" db:"winning_score"`
	LosingTeamId    int    `json:"losing_team_id" db:"losing_team_id"`
	LosingTeamName  string `json:"losing_team_name" db:"losing_team_name"`
	LosingScore     int    `json:"losing_score" db:"losing_score"`
}

type Battle struct {
	BattleID               string  `json:"battle_id" db:"battle_id"`
	BattleSeq              int     `json:"battle_seq" db:"battle_seq"`
	Camp                   int     `json:"camp" db:"camp"`
	CampColor              string  `json:"camp_color" db:"camp_color"`
	TeamID                 int     `json:"team_id" db:"team_id"`
	TeamName               string  `json:"team_name" db:"team_name"`
	TeamIcon               string  `json:"team_icon" db:"team_icon"`
	IsWin                  bool    `json:"is_win" db:"is_win"`
	KillNum                int     `json:"kill_num" db:"kill_num"`
	AssistNum              int     `json:"assist_num" db:"assist_num"`
	DeathNum               int     `json:"death_num" db:"death_num"`
	Kda                    float64 `json:"kda" db:"kda"`
	Gold                   int     `json:"gold" db:"gold"`
	PushTowerNum           int     `json:"push_tower_num" db:"push_tower_num"`
	KillBigDragonNum       int     `json:"kill_big_dragon_num" db:"kill_big_dragon_num"`
	KillTyrantNum          int     `json:"kill_tyrant_num" db:"kill_tyrant_num"`
	KillDarkTyrantNum      int     `json:"kill_dark_tyrant_num" db:"kill_dark_tyrant_num"`
	KillProphetDragonNum   int     `json:"kill_prophet_dragon_num" db:"kill_prophet_dragon_num"`
	KillShadowDragonNum    int     `json:"kill_shadow_dragon_num" db:"kill_shadow_dragon_num"`
	KillStormDragonKingNum int     `json:"kill_storm_dragon_king_num" db:"kill_storm_dragon_king_num"`
}

type TotalInfo struct {
	WinTeam  []PlayerBattleInfo
	LoseTeam []PlayerBattleInfo
}

type PlayerBattleInfo struct {
	PlayerName            string  `json:"player_name" db:"player_name"`
	TeamPlayerName        string  `json:"team_player_name" db:"team_player_name"`
	PlayerIcon            string  `json:"player_icon" db:"player_icon"`
	HeroName              string  `json:"hero_name" db:"hero_name"`
	SummonerName          string  `json:"summoner_name" db:"summoner_name"`
	Camp                  int     `json:"camp" db:"camp"`
	CampColor             string  `json:"camp_color" db:"camp_color"`
	ParticipationRate     float64 `json:"participation_rate" db:"participation_rate"`
	IsMVP                 bool    `json:"is_mvp" db:"is_mvp"`
	MVPScore              float64 `json:"mvp_score" db:"mvp_score"`
	KillNumber            int     `json:"kill_num" db:"kill_num"`
	AssistNumber          int     `json:"assist_num" db:"assist_num"`
	DeathNumber           int     `json:"death_num" db:"death_num"`
	Gold                  int     `json:"gold" db:"gold"`
	TotalHurt             int     `json:"hurt_total" db:"hurt_total"`
	TotalBeHurt           int     `json:"be_hurt_total" db:"be_hurt_total"`
	KDA                   float64 `json:"kda" db:"kda"`
	HurtTotalRate         float64 `json:"hurt_total_rate" db:"hurt_total_rate"`
	BeHurtTotalRate       float64 `json:"be_hurt_total_rate" db:"be_hurt_total_rate"`
	TotalHurtToHero       int     `json:"hurt_to_hero_total" db:"hurt_to_hero_total"`
	TotalBeHurtByHero     int     `json:"be_hurt_by_hero_total" db:"be_hurt_by_hero_total"`
	HurtToHeroTotalRate   float64 `json:"hurt_to_hero_total_rate" db:"hurt_to_hero_total_rate"`
	BeHurtByHeroTotalRate float64 `json:"be_hurt_by_hero_total_rate" db:"be_hurt_by_hero_total_rate"`
}

type PlayerInfo struct {
	StartTime string `json:"start_time" db:"start_time"`
	IsWin     bool   `json:"is_win" db:"is_win"`
	PlayerBattleInfo
}

type TeamInfo struct {
	TeamID                     int     `json:"team_id" db:"team_id"`
	TeamName                   string  `json:"team_name" db:"team_name"`
	TotalGames                 int     `json:"total_games" db:"total_games"`
	AverageWinRate             float64 `json:"average_win_rate" db:"average_win_rate"`
	AverageKDA                 float64 `json:"average_kda" db:"average_kda"`
	AverageKills               float64 `json:"average_kills" db:"average_kills"`
	AverageDeaths              float64 `json:"average_deaths" db:"average_deaths"`
	AverageAssists             float64 `json:"average_assists" db:"average_assists"`
	AverageGold                float64 `json:"average_gold" db:"average_gold"`
	AveragePushTower           float64 `json:"average_push_tower" db:"average_push_tower"`
	AverageKillBigDragon       float64 `json:"average_kill_big_dragon" db:"average_kill_big_dragon"`
	AverageKillTyrant          float64 `json:"average_kill_tyrant" db:"average_kill_tyrant"`
	AverageKillDarkTyrant      float64 `json:"average_kill_dark_tyrant" db:"average_kill_dark_tyrant"`
	AverageKillProphetDragon   float64 `json:"average_kill_prophet_dragon" db:"average_kill_prophet_dragon"`
	AverageKillShadowDragon    float64 `json:"average_kill_shadow_dragon" db:"average_kill_shadow_dragon"`
	AverageKillStormDragonKing float64 `json:"average_kill_storm_dragon_king" db:"average_kill_storm_dragon_king"`
}

func GetLeague(year int) ([]League, interface{}) {
	sqlStr := "select league_id,league_name,league_type_name,start_time,end_time,year,season,league_icon from league where year like ?"
	var league []League
	var err error
	if year == 0 {
		sqlStr = "select league_id,league_name,league_type_name,start_time,end_time,year,season,league_icon from league"
		err = db.Select(&league, sqlStr)
	} else {
		err = db.Select(&league, sqlStr, year)
	}
	if err != nil {
		return nil, err.Error()
	}
	if len(league) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return league, nil
}

func GetMatch(id int) ([]Match, interface{}) {
	sqlStr := "WITH win_los_team AS(SELECT tp1.match_id,tp1.team_id AS winning_team_id,tp2.team_id AS losing_team_id,t1.team_name AS winning_team_name,t2.team_name AS losing_team_name,tp1.score AS winning_score,tp2.score AS losing_score FROM team_participate_in_match tp1 JOIN team_participate_in_match tp2 ON tp1.match_id = tp2.match_id CROSS JOIN team t1 CROSS JOIN team t2 WHERE tp1.is_win = 1 AND tp2.is_win = 0 AND tp1.team_id = t1.team_id AND tp2.team_id = t2.team_id) SELECT match_id,bo,start_time,end_time,match_address,winning_team_id,winning_team_name,winning_score,losing_team_id,losing_team_name,losing_score FROM match_belongs NATURAL JOIN win_los_team NATURAL JOIN matches where league_id = ?"
	var match []Match
	err := db.Select(&match, sqlStr, id)
	if err != nil {
		return nil, err.Error()
	}
	if len(match) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return match, nil
}

func GetBattle(id int) ([]Battle, interface{}) {
	sqlStr := "SELECT battle_id,battle_seq,camp,CASE WHEN camp = 1 THEN '红' WHEN camp = 2 THEN '蓝' ELSE 'NULL' END AS camp_color,team_id,team_name,team_icon,is_win,kill_num,assist_num,death_num,kda,gold,push_tower_num,kill_big_dragon_num,kill_tyrant_num,kill_dark_tyrant_num,kill_prophet_dragon_num,kill_shadow_dragon_num,kill_storm_dragon_king_num FROM team_participate_in_battle NATURAL JOIN battle_belongs NATURAL JOIN battle NATURAL JOIN team WHERE match_id = ? ORDER BY battle_seq, camp"
	var battle []Battle
	err := db.Select(&battle, sqlStr, id)
	if err != nil {
		return nil, err.Error()
	}
	if len(battle) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return battle, nil
}

func GetPlayerBattleInfo(id string) (TotalInfo, interface{}) {
	sqlStr := "SELECT player_name,CONCAT(team_name, '.', player_name) AS team_player_name,COALESCE(player_icon, '') as player_icon,hero_name,summoner_name,camp,CASE WHEN camp = 1 THEN '红' WHEN camp = 2 THEN '蓝' ELSE 'NULL' END AS camp_color,participation_rate,is_mvp,mvp_score,kill_num,assist_num,death_num,gold,hurt_total,be_hurt_total,kda,hurt_total_rate,be_hurt_total_rate,hurt_to_hero_total,be_hurt_by_hero_total,hurt_to_hero_total_rate,be_hurt_by_hero_total_rate FROM a_player_plays_a_game NATURAL JOIN Battle NATURAL JOIN Team NATURAL JOIN Hero NATURAL JOIN Summoner NATURAL LEFT OUTER JOIN player WHERE battle_id= ? AND is_win = 1 ORDER BY is_mvp DESC"
	var totalInfo TotalInfo
	var WinTeam []PlayerBattleInfo
	var LoseTeam []PlayerBattleInfo
	err := db.Select(&WinTeam, sqlStr, id)
	if err != nil {
		return totalInfo, err.Error()
	}
	sqlStr = "SELECT player_name,CONCAT(team_name, '.', player_name) AS team_player_name,COALESCE(player_icon, '') as player_icon,hero_name,summoner_name,camp,CASE WHEN camp = 1 THEN '红' WHEN camp = 2 THEN '蓝' ELSE 'NULL' END AS camp_color,participation_rate,is_mvp,mvp_score,kill_num,assist_num,death_num,gold,hurt_total,be_hurt_total,kda,hurt_total_rate,be_hurt_total_rate,hurt_to_hero_total,be_hurt_by_hero_total,hurt_to_hero_total_rate,be_hurt_by_hero_total_rate FROM a_player_plays_a_game NATURAL JOIN Battle NATURAL JOIN Team NATURAL JOIN Hero NATURAL JOIN Summoner NATURAL LEFT OUTER JOIN player WHERE battle_id= ? AND is_win = 0 ORDER BY mvp_score DESC"
	err = db.Select(&LoseTeam, sqlStr, id)
	if err != nil {
		return totalInfo, err.Error()
	}
	totalInfo.WinTeam = WinTeam
	totalInfo.LoseTeam = LoseTeam
	return totalInfo, nil
}

func GetPlayerInfo(name string) ([]PlayerInfo, interface{}) {
	var playerInfo []PlayerInfo
	sqlStr := "WITH with_out_league_info AS (SELECT battle_id, match_id, team_id, team_name, player_name, CONCAT(team_name, '.', player_name) AS team_player_name, matches.start_time, is_win, COALESCE(player_icon, '') as player_icon, hero_name, summoner_name, camp, CASE WHEN camp = 1 THEN '红' WHEN camp = 2 THEN '蓝' ELSE 'NULL' END AS camp_color, participation_rate, is_mvp, mvp_score, kill_num, assist_num, death_num, gold, hurt_total, be_hurt_total, kda, hurt_total_rate, be_hurt_total_rate, hurt_to_hero_total, be_hurt_by_hero_total, hurt_to_hero_total_rate, be_hurt_by_hero_total_rate FROM a_player_plays_a_game NATURAL JOIN Battle NATURAL JOIN Team NATURAL JOIN Hero NATURAL JOIN Summoner NATURAL LEFT OUTER JOIN player NATURAL JOIN battle_belongs NATURAL JOIN matches WHERE player_name LIKE ?) SELECT player_name, team_player_name, with_out_league_info.start_time, is_win, player_icon, hero_name, summoner_name, camp, camp_color, participation_rate, is_mvp, mvp_score, kill_num, assist_num, death_num, kda, gold, hurt_total, be_hurt_total, hurt_total_rate, be_hurt_total_rate, hurt_to_hero_total, be_hurt_by_hero_total, hurt_to_hero_total_rate, be_hurt_by_hero_total_rate FROM with_out_league_info JOIN match_belongs ON with_out_league_info.match_id = match_belongs.match_id JOIN league ON league.league_id = match_belongs.league_id ORDER BY start_time DESC"
	err := db.Select(&playerInfo, sqlStr, "%"+name+"%")
	if err != nil {
		return nil, err.Error()
	}
	if len(playerInfo) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return playerInfo, nil
}

func GetTeamInfo(name string) ([]TeamInfo, interface{}) {
	sqlStr := "WITH team_game_stats AS (SELECT battle_id, battle_seq, camp, CASE WHEN camp = 1 THEN '红' WHEN camp = 2 THEN '蓝' ELSE 'NULL' END AS camp_color, team_id, team_name, team_icon, is_win, kill_num, assist_num, death_num, (kill_num + assist_num) / NULLIF(death_num, 1) AS kda, gold, push_tower_num, kill_big_dragon_num, kill_tyrant_num, kill_dark_tyrant_num, kill_prophet_dragon_num, kill_shadow_dragon_num, kill_storm_dragon_king_num FROM team_participate_in_battle NATURAL JOIN battle_belongs NATURAL JOIN battle NATURAL JOIN team ORDER BY battle_seq, camp) SELECT team_id, team_name, COUNT(battle_id) AS total_games, AVG(is_win) AS average_win_rate, AVG(kda) AS average_kda, AVG(kill_num) AS average_kills, AVG(death_num) AS average_deaths, AVG(assist_num) AS average_assists, AVG(gold) AS average_gold, AVG(push_tower_num) AS average_push_tower, AVG(kill_big_dragon_num) AS average_kill_big_dragon, AVG(kill_tyrant_num) AS average_kill_tyrant, AVG(kill_dark_tyrant_num) AS average_kill_dark_tyrant, AVG(kill_prophet_dragon_num) AS average_kill_prophet_dragon, AVG(kill_shadow_dragon_num) AS average_kill_shadow_dragon, AVG(kill_storm_dragon_king_num) AS average_kill_storm_dragon_king FROM team_game_stats WHERE team_name like ? GROUP BY team_id, team_name ORDER BY COUNT(battle_id) DESC"
	var teamInfo []TeamInfo
	err := db.Select(&teamInfo, sqlStr, "%"+name+"%")
	if err != nil {
		return nil, err.Error()
	}
	if len(teamInfo) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return teamInfo, nil
}
