package routers

import (
	"dbdemo/api"
	"dbdemo/middleware"
	"dbdemo/utils"
	"github.com/gin-gonic/gin"
)

func InitRouter() {
	gin.SetMode(utils.AppMode)
	//r := gin.New()
	r := gin.Default()
	r.Use(gin.Recovery())
	r.Use(middleware.Cors())

	router := r.Group("api")
	{
		// User module routing
		router.POST("/signup", api.SignUp)
		router.POST("/login", api.Login)
	}

	auth := r.Group("api")
	auth.Use(middleware.JwtToken())
	{
		auth.GET("/hero", api.GetHero)
		auth.GET("/heroinfo", api.GetHeroInfo)
		auth.GET("/summoner", api.GetSummoner)
		auth.GET("/item", api.GetItem)
		auth.GET("/ming", api.GetMing)
		auth.GET("/league", api.GetLeague)
		auth.GET("/match", api.GetMatch)
		auth.GET("/battle", api.GetBattle)
		auth.GET("/playerbattleinfo", api.GetPlayerBattleInfo)
		auth.GET("/player", api.GetPlayerInfo)
		auth.GET("/teaminfo", api.GetTeamInfo)
	}
	err := r.Run(utils.HttpPort)
	if err != nil {
		return
	}
}
