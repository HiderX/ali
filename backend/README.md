# README

本项目是ECNU2024春季数据库课设的后端部分，采用Golang作为语言，Gin作为框架

## 项目结构

```
.
├── Dockerfile
├── README.md
├── api
│   ├── basic.go
│   ├── league.go
│   └── user.go
├── conf
│   └── config.ini
├── go.mod
├── go.sum
├── main.go
├── middleware
│   ├── cors.go
│   └── jwt.go
├── model
│   ├── basic.go
│   ├── db.go
│   ├── hero.go
│   ├── league.go
│   └── user.go
├── routers
│   └── router.go
└── utils
    ├── cfg.go
    ├── token.go
    └── validator.go
```

## 接口文档
参考[接口文档](https://apifox.com/apidoc/shared-b2e68d52-4d00-4a1a-89e6-5a4f71c9094b)

## ToDo
- [ ] 日志导出
- [ ] 更改Token为Session