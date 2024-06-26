package api

import (
	"dbdemo/model"
	"github.com/gin-gonic/gin"
	"strconv"
)

func GetLeague(c *gin.Context) {
	year, _ := strconv.Atoi(c.Query("year"))
	league, msg := model.GetLeague(year)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"league": league,
	})
}

func GetMatch(c *gin.Context) {
	id, _ := strconv.Atoi(c.Query("league_id"))
	match, msg := model.GetMatch(id)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"match": match,
	})
}

func GetBattle(c *gin.Context) {
	id, _ := strconv.Atoi(c.Query("match_id"))
	battle, msg := model.GetBattle(id)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"battle": battle,
	})
}

func GetPlayerBattleInfo(c *gin.Context) {
	id := c.Query("battle_id")
	battleInfo, msg := model.GetPlayerBattleInfo(id)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"battleInfo": battleInfo,
	})
}

func GetPlayerInfo(c *gin.Context) {
	name := c.Query("name")
	playerInfo, msg := model.GetPlayerInfo(name)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"playerInfo": playerInfo,
	})
}

func GetTeamInfo(c *gin.Context) {
	name := c.Query("name")
	teamInfo, msg := model.GetTeamInfo(name)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"teamInfo": teamInfo,
	})
}
