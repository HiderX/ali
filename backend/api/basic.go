package api

import (
	"dbdemo/model"
	"github.com/gin-gonic/gin"
	"strconv"
)

func GetHero(c *gin.Context) {
	name := c.Query("name")
	pos := c.Query("pos")
	data, msg := model.GetHero(name, pos)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"data": data,
	})
}

func GetHeroInfo(c *gin.Context) {
	id, _ := strconv.Atoi(c.Query("id"))
	data, msg := model.GetHeroInfo(id)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"data": data,
	})
}

func GetSummoner(c *gin.Context) {
	name := c.Query("name")
	data, msg := model.GetSummoner(name)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"data": data,
	})
}

func GetItem(c *gin.Context) {
	name := c.Query("name")
	data, msg := model.GetItem(name)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"data": data,
	})
}

func GetMing(c *gin.Context) {
	name := c.Query("name")
	mtype := c.Query("type")
	grade, _ := strconv.Atoi(c.Query("grade"))
	data, msg := model.GetMing(name, mtype, grade)
	if msg != nil {
		c.JSON(200, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(200, gin.H{
		"data": data,
	})
}
