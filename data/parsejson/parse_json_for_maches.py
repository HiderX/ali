import json

# JSON 数据
#    json_data =''''''
json_data ='''
{
    "message": "",
    "code": 200,
    "request_id": "ff60905d03d6670bf05fddd583ba501a",
    "results": [
        {
            "match_id": "2019030601",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "camp2": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-06 18:00:00",
            "end_time": "2019-03-06 20:39:26",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_12_1551868207",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_13_1551871421",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_14_1551873507",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019030602",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-06 20:00:00",
            "end_time": "2019-03-06 23:28:35",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_15_1551877985",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_16_1551880550",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_17_1551883074",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_18_1551884806",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019030701",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-07 18:00:00",
            "end_time": "2019-03-07 19:23:14",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_21_1551952263",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_22_1551954081",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_23_1551955900",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019030702",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-07 20:00:00",
            "end_time": "2019-03-07 21:57:38",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_16_1551961726",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_17_1551963360",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_18_1551965531",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019030801",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-08 18:00:00",
            "end_time": "2019-03-08 19:35:42",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_20_1552038652",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_21_1552040746",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_22_1552042708",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019030802",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-08 20:00:00",
            "end_time": "2019-03-08 22:07:16",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_2_1552046800",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_3_1552048893",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_4_1552051051",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1552052780",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019030901",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-09 15:00:00",
            "end_time": "2019-03-09 17:38:17",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_7_1552115698",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_8_1552117725",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_9_1552119342",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_10_1552120892",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_11_1552122911",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019030902",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-09 18:00:00",
            "end_time": "2019-03-09 21:13:20",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_12_1552126219",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_13_1552128490",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_14_1552131396",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_15_1552133463",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_16_1552135848",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019030903",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-09 20:00:00",
            "end_time": "2019-03-10 00:10:15",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_24_1552138973",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_25_1552141344",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_26_1552143376",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_27_1552145542",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031001",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-10 15:00:00",
            "end_time": "2019-03-10 17:17:45",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_19_1552202189",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_20_1552205702",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_21_1552207955",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031002",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-10 18:00:00",
            "end_time": "2019-03-10 19:47:07",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_29_1552211713",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_30_1552213388",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_31_1552216810",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031003",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-10 20:00:00",
            "end_time": "2019-03-10 21:39:22",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_32_1552219936",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_33_1552221815",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_34_1552223380",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031301",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-13 18:00:00",
            "end_time": "2019-03-13 19:51:54",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_2_1552470672",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_3_1552472081",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_4_1552474337",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_5_1552475938",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031302",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-13 20:00:00",
            "end_time": "2019-03-13 23:21:54",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_3_1552479826",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_4_1552482199",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1552485609",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_6_1552488695",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031401",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-14 18:00:00",
            "end_time": "2019-03-14 20:36:46",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_8_1552557236",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_9_1552559410",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_10_1552561216",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_11_1552563666",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_12_1552565768",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031402",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-14 20:00:00",
            "end_time": "2019-03-15 00:10:00",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_7_1552568743",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_8_1552571238",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_9_1552573566",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_10_1552575692",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_11_1552577963",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031501",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "camp2": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-15 18:00:00",
            "end_time": "2019-03-15 19:16:31",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_13_1552643439",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_14_1552644997",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_15_1552646647",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031502",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-15 20:00:00",
            "end_time": "2019-03-15 22:15:31",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_17_1552652658",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_18_1552654450",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_19_1552656195",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_20_1552657984",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031601",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-16 15:00:00",
            "end_time": "2019-03-16 18:43:36",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_17_1552720240",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_18_1552722882",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_19_1552725008",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_20_1552727278",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_21_1552729368",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031602",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "camp2": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-16 18:00:00",
            "end_time": "2019-03-16 21:18:54",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_23_1552734719",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_24_1552736824",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_25_1552739368",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_26_1552741188",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031603",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-16 20:00:00",
            "end_time": "2019-03-16 23:30:21",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_27_1552743974",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_28_1552746974",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_29_1552749105",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031701",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-17 15:00:00",
            "end_time": "2019-03-17 17:44:31",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_31_1552806777",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_32_1552810263",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_33_1552812558",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_34_1552814422",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031702",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-17 18:00:00",
            "end_time": "2019-03-17 19:48:25",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_23_1552817429",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_24_1552819865",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_25_1552821808",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019031703",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "camp2": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-17 20:00:00",
            "end_time": "2019-03-17 21:57:17",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_26_1552824931",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_27_1552827045",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_28_1552829684",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032001",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-20 18:00:00",
            "end_time": "2019-03-20 20:02:21",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_31_1553077610",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_32_1553079783",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_33_1553081516",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032002",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-20 20:00:00",
            "end_time": "2019-03-20 22:38:10",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_37_1553085187",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_38_1553087188",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_39_1553089658",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_40_1553091411",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032101",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-21 18:00:00",
            "end_time": "2019-03-21 20:44:02",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_45_1553163762",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_46_1553165964",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_47_1553167948",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_48_1553171133",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032102",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-21 20:00:00",
            "end_time": "2019-03-21 22:41:19",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_35_1553173996",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_36_1553175722",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_37_1553177638",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032201",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-22 18:00:00",
            "end_time": "2019-03-22 19:26:02",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_39_1553248253",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_40_1553250698",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_41_1553252557",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032202",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-22 20:00:00",
            "end_time": "2019-03-22 22:00:35",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_52_1553255689",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_53_1553257819",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_54_1553259843",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_55_1553262021",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032301",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-23 15:00:00",
            "end_time": "2019-03-23 17:13:09",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_43_1553325367",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_45_1553328568",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_47_1553330767",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032302",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-23 18:00:00",
            "end_time": "2019-03-23 20:57:23",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_59_1553336828",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_60_1553340184",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_61_1553342411",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_62_1553344619",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032303",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-23 20:00:00",
            "end_time": "2019-03-24 00:14:31",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_63_1553347529",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_64_1553349525",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_65_1553351890",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_66_1553353938",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_67_1553356265",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032401",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "camp2": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-24 15:00:00",
            "end_time": "2019-03-24 17:01:04",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_69_1553411639",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_70_1553413491",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_71_1553415104",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_72_1553416957",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032402",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-24 18:00:00",
            "end_time": "2019-03-24 20:23:33",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_73_1553421218",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_74_1553424216",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_75_1553426664",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_76_1553428534",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032403",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-24 20:00:00",
            "end_time": "2019-03-24 23:21:07",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_50_1553431781",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_51_1553433812",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_52_1553435588",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_53_1553437500",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_54_1553439486",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032701",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "camp2": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-27 18:00:00",
            "end_time": "2019-03-27 20:14:58",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_2_1553680228",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_3_1553682937",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_4_1553685215",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_5_1553687096",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032702",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-27 20:00:00",
            "end_time": "2019-03-27 23:57:20",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_3_1553690637",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_4_1553693671",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1553696226",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_6_1553698369",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_7_1553700701",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032801",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-28 18:00:00",
            "end_time": "2019-03-28 19:24:13",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_7_1553766622",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_8_1553768459",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_9_1553770847",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032802",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-28 20:00:00",
            "end_time": "2019-03-28 22:16:50",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_9_1553774164",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_10_1553776563",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_11_1553778805",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_12_1553780956",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032901",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-29 18:00:00",
            "end_time": "2019-03-29 20:35:02",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_15_1553855167",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_16_1553856918",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_17_1553858448",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_18_1553860246",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019032902",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-29 20:00:00",
            "end_time": "2019-03-29 23:23:04",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_11_1553864614",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_12_1553866944",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_13_1553868929",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_14_1553870745",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019033001",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-30 15:00:00",
            "end_time": "2019-03-30 17:31:14",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_16_1553929840",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_17_1553931735",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_18_1553934211",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_19_1553936333",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019033002",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-30 18:00:00",
            "end_time": "2019-03-30 20:11:35",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_22_1553942736",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_23_1553944466",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_24_1553946499",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019033003",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-30 20:00:00",
            "end_time": "2019-03-30 22:33:29",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_25_1553949535",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_26_1553951464",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_27_1553954113",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019033101",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-03-31 15:00:00",
            "end_time": "2019-03-31 17:21:08",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_21_1554016232",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_22_1554018332",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_23_1554020544",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_24_1554022682",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019033102",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-31 18:00:00",
            "end_time": "2019-03-31 19:41:28",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_25_1554025855",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_26_1554027943",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_27_1554030439",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019033103",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-03-31 20:00:00",
            "end_time": "2019-03-31 23:12:14",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_29_1554034279",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_30_1554035985",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_31_1554039044",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_32_1554040684",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_33_1554043632",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040301",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "camp2": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-03 18:00:00",
            "end_time": "2019-04-03 20:26:26",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_33_1554287034",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_34_1554288977",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_35_1554291258",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_36_1554292966",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040302",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-03 20:00:00",
            "end_time": "2019-04-03 23:22:50",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_41_1554296064",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_42_1554299169",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_43_1554301230",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_44_1554303431",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040401",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-04 18:00:00",
            "end_time": "2019-04-04 20:02:42",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_47_1554371693",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_48_1554373340",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_49_1554375612",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_50_1554377800",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040402",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-04 20:00:00",
            "end_time": "2019-04-04 22:41:53",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_46_1554380958",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_47_1554383024",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_48_1554385159",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_49_1554387513",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040501",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-05 18:00:00",
            "end_time": "2019-04-05 21:02:22",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_52_1554457894",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_54_1554462634",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_55_1554465375",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_56_1554467482",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040502",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-05 20:00:00",
            "end_time": "2019-04-05 23:20:54",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_53_1554471088",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_54_1554473774",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_55_1554476014",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040601",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-06 15:00:00",
            "end_time": "2019-04-06 17:19:09",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_57_1554534746",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_58_1554536917",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_59_1554539308",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_60_1554541166",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040602",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-06 18:00:00",
            "end_time": "2019-04-06 19:17:16",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_58_1554543916",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_59_1554545632",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_60_1554547721",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040603",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-06 20:00:00",
            "end_time": "2019-04-06 22:26:56",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_62_1554552812",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_63_1554554838",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_64_1554556981",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_65_1554558840",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040701",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-07 15:00:00",
            "end_time": "2019-04-07 17:56:51",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_67_1554621026",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_68_1554623289",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_69_1554625313",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_70_1554627497",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_71_1554629350",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040702",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-07 18:00:00",
            "end_time": "2019-04-07 21:25:21",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_72_1554632489",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_73_1554634601",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_74_1554636431",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_75_1554639076",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_76_1554641591",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019040703",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "bo": 5,
            "win_camp": 0,
            "status": 2,
            "start_time": "2019-04-07 20:00:00",
            "end_time": "2019-04-07 23:00:00",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_63_1554645237",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_64_1554647330",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_65_1554649519",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_66_1554652167",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041001",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-10 18:00:00",
            "end_time": "2019-04-10 19:57:31",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_78_1554889700",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_79_1554892505",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_80_1554894202",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_81_1554896052",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041002",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-10 20:00:00",
            "end_time": "2019-04-10 22:24:57",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_2_1554899270",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_3_1554901003",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_4_1554903182",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1554905177",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041101",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-11 18:00:00",
            "end_time": "2019-04-11 19:55:25",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_84_1554978639",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_85_1554980203",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_86_1554982193",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041102",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-11 20:00:00",
            "end_time": "2019-04-11 23:43:27",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_8_1554985463",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_9_1554987530",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_10_1554989988",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_11_1554993128",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_12_1554995415",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041201",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-12 18:00:00",
            "end_time": "2019-04-12 20:13:36",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_88_1555062539",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_89_1555064459",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_90_1555066103",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_91_1555067719",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_92_1555069462",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041202",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-12 20:00:00",
            "end_time": "2019-04-12 22:52:21",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_14_1555072851",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_15_1555074791",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_16_1555076830",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_17_1555079109",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041301",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "camp2": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-13 15:00:00",
            "end_time": "2019-04-13 16:56:24",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_95_1555139330",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_96_1555141895",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_97_1555143911",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041302",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 0,
            "status": 2,
            "start_time": "2019-04-13 18:00:00",
            "end_time": "2019-04-13 21:00:00",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_19_1555149171",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_20_1555151372",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_21_1555153749",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041303",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-13 20:00:00",
            "end_time": "2019-04-13 23:24:27",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_24_1555161111",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_25_1555162826",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_26_1555165145",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_27_1555167541",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041401",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-14 15:00:00",
            "end_time": "2019-04-14 17:38:19",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_29_1555226024",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_30_1555227846",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_31_1555231334",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_32_1555233429",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041402",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-14 18:00:00",
            "end_time": "2019-04-14 20:54:47",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_104_1555236250",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_105_1555238252",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_106_1555240278",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_107_1555242794",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_108_1555244891",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041403",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-14 20:00:00",
            "end_time": "2019-04-15 00:08:11",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_109_1555247901",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_110_1555249755",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_111_1555251358",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_112_1555253240",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_113_1555255770",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041701",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-17 18:00:00",
            "end_time": "2019-04-17 21:19:40",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_1_1555495343",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_2_1555497697",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_3_1555500412",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_4_1555503012",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1555505313",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041702",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-17 20:00:00",
            "end_time": "2019-04-17 23:23:13",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_3_1555508739",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_4_1555510778",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_5_1555513320",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041801",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-18 18:00:00",
            "end_time": "2019-04-18 20:12:26",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_5_1555583831",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_6_1555586068",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_7_1555588152",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041802",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-18 20:00:00",
            "end_time": "2019-04-19 00:11:49",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_7_1555591370",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_8_1555593704",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_9_1555596256",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_10_1555598280",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_11_1555601631",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041901",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-19 18:00:00",
            "end_time": "2019-04-19 20:01:52",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_13_1555669799",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_14_1555671647",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_15_1555673485",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019041902",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-19 20:00:00",
            "end_time": "2019-04-19 22:13:43",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_14_1555676943",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_15_1555679614",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_16_1555681690",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042001",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-20 15:00:00",
            "end_time": "2019-04-20 17:39:01",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_18_1555744207",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_19_1555745851",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_20_1555747755",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_21_1555749468",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_22_1555751392",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042002",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-20 18:00:00",
            "end_time": "2019-04-20 21:00:36",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_19_1555754808",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_20_1555756734",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_21_1555758734",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_22_1555760916",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_23_1555763664",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042003",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-20 20:00:00",
            "end_time": "2019-04-21 00:01:11",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_24_1555766699",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_25_1555768743",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_26_1555771409",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_27_1555773796",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042101",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-21 15:00:00",
            "end_time": "2019-04-21 16:48:03",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_29_1555830822",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_30_1555832872",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_31_1555834922",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042102",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "camp2": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-21 18:00:00",
            "end_time": "2019-04-21 19:54:01",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_24_1555840147",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_25_1555843006",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_26_1555845745",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042103",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "camp2": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-21 20:00:00",
            "end_time": "2019-04-21 22:31:50",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_27_1555849077",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_28_1555850867",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_29_1555852866",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_30_1555855826",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042401",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "camp2": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-24 18:00:00",
            "end_time": "2019-04-24 20:40:16",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_5_1556099367",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_6_1556101324",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_8_1556103485",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_9_1556105916",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_10_1556107985",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042402",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-24 20:00:00",
            "end_time": "2019-04-24 23:37:29",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_2_1556110891",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_3_1556114126",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_4_1556115971",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1556118170",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042501",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-25 18:00:00",
            "end_time": "2019-04-25 19:53:15",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_3_1556185867",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_4_1556188684",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_5_1556191049",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042502",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-25 20:00:00",
            "end_time": "2019-04-25 22:05:08",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_3_1556194813",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_4_1556196980",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1556199214",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042601",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-26 18:00:00",
            "end_time": "2019-04-26 20:20:03",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_8_1556273894",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_9_1556275728",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_10_1556277605",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_11_1556279441",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042602",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-26 20:00:00",
            "end_time": "2019-04-26 23:49:38",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_10_1556282530",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_11_1556284827",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_12_1556286821",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_13_1556289832",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_14_1556292053",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042701",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-27 15:00:00",
            "end_time": "2019-04-27 17:07:12",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_13_1556348912",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_14_1556350489",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_15_1556352338",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_16_1556354042",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042702",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "camp2": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-27 18:00:00",
            "end_time": "2019-04-27 20:06:58",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_17_1556360728",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_18_1556362732",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_19_1556364538",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042703",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-27 20:00:00",
            "end_time": "2019-04-27 23:43:57",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_20_1556368691",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_21_1556370849",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_22_1556373745",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_23_1556376737",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_24_1556378572",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042801",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-28 15:00:00",
            "end_time": "2019-04-28 17:15:42",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_18_1556435287",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_19_1556437598",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_20_1556439197",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_21_1556441714",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042802",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "camp2": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-28 18:00:00",
            "end_time": "2019-04-28 19:23:01",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_22_1556444449",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_23_1556446762",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_24_1556448970",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042803",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-28 20:00:00",
            "end_time": "2019-04-28 21:21:59",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_26_1556452186",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_27_1556454134",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_28_1556456417",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042901",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-29 18:00:00",
            "end_time": "2019-04-29 20:15:24",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_26_1556531270",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_27_1556533159",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_28_1556534971",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_29_1556536483",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_30_1556538750",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019042902",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-04-29 20:00:00",
            "end_time": "2019-04-29 22:56:31",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_32_1556541466",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_33_1556543216",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_34_1556545484",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_35_1556547795",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019043001",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "camp2": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-30 18:00:00",
            "end_time": "2019-04-30 19:33:52",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_34_1556617637",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_35_1556619774",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_36_1556622564",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019043002",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-04-30 20:00:00",
            "end_time": "2019-04-30 22:15:07",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_38_1556625794",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_39_1556628214",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_40_1556630143",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_41_1556631958",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019050101",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10019",
                "team_name": "TOPM",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10019.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "TOPM"
            },
            "camp2": {
                "team_id": "10017",
                "team_name": "广州TTG",
                "team_icon": "https://smobatv-pic.tga.qq.com/6b580d2f97ee81f4206a2bfba5b98ad5.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "TTG"
            },
            "bo": 5,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-05-01 18:00:00",
            "end_time": "2019-05-01 20:26:05",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_43_1556704395",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_44_1556707136",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_45_1556709977",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_46_1556712354",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019050102",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10008",
                "team_name": "深圳DYG",
                "team_icon": "https://smobatv-pic.tga.qq.com/f61386c210a6dc3081dc48bc36c7c2da.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DYG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-01 20:00:00",
            "end_time": "2019-05-01 23:09:18",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_39_1556714962",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_40_1556716865",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_41_1556719460",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_42_1556721845",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019050201",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "camp2": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-02 15:00:00",
            "end_time": "2019-05-02 17:09:16",
            "match_address": "成都",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_45_1556780928",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_46_1556782691",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_47_1556784466",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_48_1556786093",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019050202",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-02 18:00:00",
            "end_time": "2019-05-02 21:22:38",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_49_1556790724",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_50_1556793980",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_51_1556796597",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_52_1556799068",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_53_1556801568",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019050203",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10004",
                "team_name": "BA黑凤梨",
                "team_icon": "https://res.edata.qq.com/sgame/static/images/team/10004.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "BA"
            },
            "camp2": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-02 20:00:00",
            "end_time": "2019-05-02 23:41:48",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "常规赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_54_1556804754",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_55_1556807260",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_56_1556809843",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019050401",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10005",
                "team_name": "苏州KSG",
                "team_icon": "https://smobatv-pic.tga.qq.com/b18d511c93127872c81e0af9b74c424e.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "KSG"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 5,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-04 20:00:00",
            "end_time": "2019-05-04 22:26:30",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "regular_season",
            "match_stage_desc": "match_stage_desc",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_77_1556973595",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_78_1556976174",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_79_1556978572",
                    "battle_seq": 3,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019050901",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "camp2": {
                "team_id": "10020",
                "team_name": "厦门VG",
                "team_icon": "https://smobatv-pic.tga.qq.com/384921f944c10613c5eb0e565a982235.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "VG"
            },
            "bo": 7,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-05-09 18:00:00",
            "end_time": "2019-05-09 20:38:13",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_89_1557396752",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_90_1557399350",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_91_1557401345",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_92_1557404218",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019051001",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10002",
                "team_name": "上海EDG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/ce590057218a0626f25702b5b720517d.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "EDG.M"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 7,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-10 18:00:00",
            "end_time": "2019-05-10 21:19:32",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_94_1557483193",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_95_1557486056",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_96_1557488398",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_97_1557490993",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_98_1557492899",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019051101",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10010",
                "team_name": "西安WE",
                "team_icon": "https://smobatv-pic.tga.qq.com/066011922e30584cf66604ca930640dd.png",
                "is_win": false,
                "score": 3,
                "rank": 0,
                "team_abbreviation": "WE"
            },
            "bo": 7,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-05-11 18:00:00",
            "end_time": "2019-05-11 22:08:18",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_101_1557569563",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_102_1557571398",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_103_1557573099",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_104_1557575380",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_105_1557577493",
                    "battle_seq": 5,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_106_1557579669",
                    "battle_seq": 6,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_107_1557581544",
                    "battle_seq": 7,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019051201",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "camp2": {
                "team_id": "10003",
                "team_name": "北京WB",
                "team_icon": "https://smobatv-pic.tga.qq.com/d8be5361004a0636c1c545fbd7730e4e.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "WB"
            },
            "bo": 7,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-05-12 18:00:00",
            "end_time": "2019-05-12 21:59:03",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_112_1557655971",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_113_1557658066",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_114_1557660395",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_115_1557663858",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_116_1557666123",
                    "battle_seq": 5,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_117_1557668294",
                    "battle_seq": 6,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019051601",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "bo": 7,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-16 18:00:00",
            "end_time": "2019-05-16 20:46:27",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_4_1558002692",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1558004855",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_6_1558006688",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_7_1558009430",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019051701",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "camp2": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "bo": 7,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-17 18:00:00",
            "end_time": "2019-05-17 21:43:05",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_12_1558087931",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_13_1558091039",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_14_1558093222",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_15_1558095792",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_16_1558098856",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019051801",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10001",
                "team_name": "重庆狼队",
                "team_icon": "https://smobatv-pic.tga.qq.com/b7668d1eecd13d64875a960b15a4941d.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "狼队"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 7,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-18 18:00:00",
            "end_time": "2019-05-18 21:12:19",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_21_1558174401",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_22_1558176494",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_23_1558179086",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_24_1558181793",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_25_1558183572",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019051901",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10007",
                "team_name": "南京Hero久竞",
                "team_icon": "https://smobatv-pic.tga.qq.com/9cf8e7d989f6d72b9940babcf938a11f.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "Hero"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 7,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-19 18:00:00",
            "end_time": "2019-05-19 21:24:36",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_29_1558260738",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_30_1558262986",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_31_1558265358",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_32_1558268066",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_33_1558270930",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019052401",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10016",
                "team_name": "佛山DRG",
                "team_icon": "https://smobatv-pic.tga.qq.com/203f77f44f24f446f073c7b11fb56f99.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "DRG"
            },
            "bo": 7,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-05-24 18:00:00",
            "end_time": "2019-05-24 20:57:20",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_4_1558692831",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_5_1558695198",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_6_1558697546",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_7_1558701066",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019052501",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": false,
                "score": 1,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "camp2": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "bo": 7,
            "win_camp": 2,
            "status": 2,
            "start_time": "2019-05-25 18:00:00",
            "end_time": "2019-05-25 21:19:47",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_10_1558779240",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_11_1558781629",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_12_1558784574",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_13_1558787341",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_14_1558789115",
                    "battle_seq": 5,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019052601",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": true,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "camp2": {
                "team_id": "10018",
                "team_name": "济南RW侠",
                "team_icon": "https://smobatv-pic.tga.qq.com/fbbbb260fb5c1ac7bd06bc6de2523deb.png",
                "is_win": false,
                "score": 0,
                "rank": 0,
                "team_abbreviation": "RW侠"
            },
            "bo": 7,
            "win_camp": 1,
            "status": 2,
            "start_time": "2019-05-26 18:00:00",
            "end_time": "2019-05-26 20:54:16",
            "match_address": "上海",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "34406944_19_1558865669",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_20_1558867962",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "34472480_4_1558870491",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "34406944_22_1558873380",
                    "battle_seq": 4,
                    "video_list": []
                }
            ]
        },
        {
            "match_id": "2019061501",
            "league_id": "20190001",
            "camp1": {
                "team_id": "10009",
                "team_name": "上海RNG.M",
                "team_icon": "https://smobatv-pic.tga.qq.com/198bee22f35580a28cfa53d4458f154c.png",
                "is_win": false,
                "score": 2,
                "rank": 0,
                "team_abbreviation": "RNG.M"
            },
            "camp2": {
                "team_id": "10006",
                "team_name": "武汉eStarPro",
                "team_icon": "https://smobatv-pic.tga.qq.com/c5d3d46808c5997591cf94b1ba2f9173.png",
                "is_win": false,
                "score": 4,
                "rank": 0,
                "team_abbreviation": "ES"
            },
            "bo": 7,
            "win_camp": 0,
            "status": 2,
            "start_time": "2019-06-15 17:30:00",
            "end_time": "2019-06-15 21:00:00",
            "match_address": "西安",
            "match_desc": "",
            "match_stage_seq": 0,
            "match_stage_name": "playoff",
            "match_stage_desc": "季后赛",
            "cc_match_id": "",
            "match_battle_video_list": [
                {
                    "battle_id": "118293024_19_1559468822",
                    "battle_seq": 1,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_20_1559471300",
                    "battle_seq": 2,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_11_1560595977",
                    "battle_seq": 3,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_12_1560598194",
                    "battle_seq": 4,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_13_1560600030",
                    "battle_seq": 5,
                    "video_list": []
                },
                {
                    "battle_id": "118293024_14_1560602314",
                    "battle_seq": 6,
                    "video_list": []
                }
            ]
        }
    ]
}
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 生成 SQL 插入语句
sql_inserts = []
for match in data['results']:
    match_id = match['match_id']
    bo = match['bo']
    start_time = match['start_time']
    end_time = match['end_time']
    match_address = match['match_address']
    win_camp = match['win_camp']
    sql_insert = f"INSERT INTO matches (match_id, bo, start_time, end_time, match_address, win_camp) VALUES ({match_id}, {bo}, '{start_time}', '{end_time}', '{match_address}', {win_camp});"
    sql_inserts.append(sql_insert)

# 打印 SQL
# 将SQL插入语句写入文件（追加模式）
with open('matches.sql', 'a', encoding='utf-8') as f:
    for sql_insert in sql_inserts:
        f.write(sql_insert + '\n')
