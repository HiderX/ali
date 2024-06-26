package api

import (
	"dbdemo/middleware"
	"dbdemo/model"
	"dbdemo/utils"
	"github.com/gin-gonic/gin"
	"net/http"
)

func Test(c *gin.Context) {
	c.String(200, "Hello world")
}

func ShowInfo(c *gin.Context) {
	c.JSON(200, gin.H{
		"message":  "ok",
		"AppMode":  utils.AppMode,
		"HttpPort": utils.HttpPort,
		"Db":       utils.Db,
		"DbHost":   utils.DbHost,
		"DbPort":   utils.DbPort,
	})
}

func SignUp(c *gin.Context) {
	var u model.SignUpParam
	err := c.ShouldBindJSON(&u)
	msg := utils.Validate(err)
	if msg != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": msg,
		})
		return
	}
	msg = model.SignUp(u.Name, u.Password, u.Email)
	if msg != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": msg,
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"Age":   u.Age,
		"Email": u.Email,
		"Name":  u.Name,
		"msg":   "ok",
	})
}

func Auth(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{
		"msg":   "ok",
		"token": c.GetHeader("Authorization")[7:],
	})
}

func Login(c *gin.Context) {
	var data model.LoginParam
	err := c.ShouldBindJSON(&data)
	msg := utils.Validate(err)
	if msg != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": msg,
		})
		return
	}
	msg = model.CheckLogin(data.Username, data.Password)
	if msg != nil {
		c.JSON(http.StatusOK, gin.H{
			"msg": msg,
		})
		return
	}
	token, msg := middleware.GenerateJWT(data.Username)
	c.JSON(http.StatusOK, gin.H{
		"msg":   msg,
		"token": token,
	})
}
