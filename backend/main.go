package main

import (
	"dbdemo/model"
	"dbdemo/routers"
)

func main() {
	model.InitDb()
	routers.InitRouter()
}
