# Ali

## 简介

本项目实现了一个王者荣耀数据平台，用户可以通过此平台查询王者荣耀游戏中的英雄、铭文、装备、皮肤等信息，也可以查询历史赛事信息、战队统计数据、选手统计数据等。

本项目旨在帮助用户快速了解、熟悉王者荣耀的游戏内容，一键查看赛事相关信息。支持模糊查询等新手友好功能，帮助他们快速上手游戏。

本项目的原始数据通过python脚本从互联网爬取，通过使用线程池实现并发，提高效率。

本项目通过python脚本将爬虫得到的原始数据进行解析，自动化的生成数据插入的INSERT语句，提高效率。

本项目采用前后端分离架构，符合Restful API规范以及MVC设计模式。

前端部分使用html+css+javascript三件套编写，没有使用vue、react等复杂框架，保证了代码的简洁性。

本项目的后端部分使用Golang作为语言，Gin作为框架，并借助Github Actions实现了容器化自动构建、自动部署到服务器。

本项目使用Mysql作为数据库，结构化的存储各种数据。Mysql的事务支持和ACID特性确保了数据的一致性和完整性。此外，我们还利用了Mysql的备份和恢复功能，以防数据丢失，确保数据的安全性。

我们通过语雀实现多人协作编写文档，你也可以在[语雀](https://www.yuque.com/nil./ev4o1l/zoo5lms0vzfqseas?singleDoc#)查看本报告

本项目已开源到GitHub，你可以在[Github](https://github.com/HiderX/ali)查看本项目的所有代码。

## 目录结构

```
.
├── README.md
├── backend
│   ├── Dockerfile
│   ├── README.md
│   ├── api
│   ├── conf
│   ├── go.mod
│   ├── go.sum
│   ├── main.go
│   ├── middleware
│   ├── model
│   ├── routers
│   └── utils
├── data
│   ├── SQLinsert
│   ├── SQLtest
│   ├── datasource
│   ├── parsejson
│   └── spider&washer
└── frontend
    ├── battle.html
    ├── battle_player.html
    ├── css
    ├── hero.html
    ├── hero_detail.html
    ├── index.html
    ├── item.html
    ├── js
    ├── league.html
    ├── login.html
    ├── match.html
    ├── media
    ├── ming.html
    ├── player_status.html
    ├── summoner.html
    └── team_status.html
```

backend为后端

data为数据相关内容，包括数据爬取、处理、解析、插入、测试等部分，以及数据源

frontend为前端

## 快速部署

### 前端

将frontend目录中的所有内容上传到服务器的网站目录的index目录下即可

### 数据库
使用NAVICAT或者其他工具连接到服务器的数据库 

右键你希望使用的数据库，选择`运行SQL文件`选项，将`create.sql`导入并运行，创建19张空数据表。 

接下来在按照`create.sql`中的建表顺序，依次将`SQL_INSERT`文件夹下的19个SQL文件同样通过`运行SQL文件`的方式导入数据库。  

顺序如下：

1. league.sql
2. matches.sql
3. match_belongs.sql
4. battle.sql
5. battle_belongs.sql
6. team_remover.sql
7. team_participate_in_match.sql
8. team_participate_in_battle.sql
9. player_removed.sql
10. hero.sql
11. hero_skin.sql
12. item.sql
13. Summoner.sql
14. ming.sql
15. a_player_plays_a_game.sql
16. use_item.sql
17. hero_skill.sql
18. hero_pos.sql
19. item_pos.sql


### 后端

本项目支持两种部署方式：可执行文件部署和docker部署

#### 可执行文件部署

将本项目克隆到本地后，进入backend目录，执行`go build`，生成可执行文件

对于不同的系统，build的参数可以参考https://go.dev/doc/tutorial/compile-install

在生成可执行文件之后，直接将可执行文件上传到服务器运行即可

#### Docker部署

本项目已经推送到DockerHub，在服务器上执行`docker pull d1caprio/dbdemo`即可拉取最新的镜像

在服务器终端执行`docker run -d --name dbdemo -p 3000:3000 d1caprio/dbdemo`命令启动容器，端口可以自行修改

- 针对国内拉取不到Docker镜像的问题，可以搜索相关教程替换国内镜像源
- 请确认你的服务器已经安装了Docker