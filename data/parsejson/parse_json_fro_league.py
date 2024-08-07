import json

# 示例 JSON 数据
json_data = '''
{
  "message": "",
  "code": 200,
  "request_id": "b03fcb1ab9ac28bc0a353e69bf000194",
  "results": [
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20190001",
      "start_time": "2019-03-06 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20190001.jpg",
      "is_top": 1,
      "end_time": "2019-06-02 23:59:00",
      "league_name": "2019KPL春季赛",
      "season": 1,
      "year": 2019,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "world_champion_cup",
      "league_id": "20190002",
      "start_time": "2019-06-06 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20190002.jpg",
      "is_top": 1,
      "end_time": "2019-06-09 23:59:00",
      "league_name": "2019世界冠军杯选拔赛",
      "season": 1,
      "year": 2019,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "world_champion_cup",
      "league_id": "20190003",
      "start_time": "2019-07-10 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20190003.jpg",
      "is_top": 1,
      "end_time": "2019-08-10 23:59:00",
      "league_name": "2019世界冠军杯正赛",
      "season": 1,
      "year": 2019,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20190004",
      "start_time": "2019-09-11 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20190004.jpg",
      "is_top": 1,
      "end_time": "2019-12-14 23:59:00",
      "league_name": "2019KPL秋季赛",
      "season": 2,
      "year": 2019,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "winter_champion_cup",
      "league_id": "20190006",
      "start_time": "2019-12-21 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20190006.png",
      "is_top": 1,
      "end_time": "2020-01-05 23:59:00",
      "league_name": "2019冬季冠军杯",
      "season": 1,
      "year": 2019,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20200001",
      "start_time": "2020-03-22 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20200001.jpg",
      "is_top": 1,
      "end_time": "2020-06-13 23:59:59",
      "league_name": "2020KPL春季赛",
      "season": 1,
      "year": 2020,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "world_champion_cup",
      "league_id": "20200002",
      "start_time": "2020-06-22 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20200002.jpg",
      "is_top": 1,
      "end_time": "2020-06-28 23:59:59",
      "league_name": "2020世界冠军杯选拔赛",
      "season": 1,
      "year": 2020,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "world_champion_cup",
      "league_id": "20200003",
      "start_time": "2020-07-15 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20200002.jpg",
      "is_top": 1,
      "end_time": "2020-08-16 23:59:59",
      "league_name": "2020世界冠军杯正赛",
      "season": 1,
      "year": 2020,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20200004",
      "start_time": "2020-09-16 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20200004.jpg",
      "is_top": 1,
      "end_time": "2020-12-19 23:59:59",
      "league_name": "2020KPL秋季赛",
      "season": 2,
      "year": 2020,
      "cc_league_id": "KPL2020S2",
      "live_room_address": "https://pvp.qq.com/match/kpl/KPL2020S2/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "winter_champion_cup",
      "league_id": "20200005",
      "start_time": "2021-01-06 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20200005.jpg",
      "is_top": 1,
      "end_time": "2021-01-23 23:59:59",
      "league_name": "2020冬季冠军杯",
      "season": 1,
      "year": 2020,
      "cc_league_id": "KCC2020W",
      "live_room_address": "https://pvp.qq.com/match/kpl/KCC2020W/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20210021",
      "start_time": "2021-03-11 15:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/league_2005864c8e1911ebb99320906f5a1b8f.png",
      "is_top": 1,
      "end_time": "2021-03-21 23:59:59",
      "league_name": "2021KPL春季赛季前赛",
      "season": 0,
      "year": 2021,
      "cc_league_id": "",
      "live_room_address": "https://pvp.qq.com/match/kpl//index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "202100201",
      "start_time": "2021-03-27 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/league_2005864c8e1911ebb99320906f5a1b8f.png",
      "is_top": 1,
      "end_time": "2021-06-25 23:59:59",
      "league_name": "2021KPL春季赛",
      "season": 1,
      "year": 2021,
      "cc_league_id": "KPL2021S1",
      "live_room_address": "https://pvp.qq.com/match/kpl/KPL2021S1/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "world_champion_cup",
      "league_id": "20210003",
      "start_time": "2021-07-05 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/league_75a3c08081a511eb81f6140564711851.png",
      "is_top": 1,
      "end_time": "2021-08-28 23:59:59",
      "league_name": "2021世界冠军杯",
      "season": 1,
      "year": 2021,
      "cc_league_id": "KCC2021S",
      "live_room_address": "https://pvp.qq.com/match/kpl/KCC2021S/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20210004",
      "start_time": "2021-09-22 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20210004.jpg",
      "is_top": 1,
      "end_time": "2021-12-25 23:59:59",
      "league_name": "2021KPL秋季赛",
      "season": 1,
      "year": 2021,
      "cc_league_id": "KPL2021S2",
      "live_room_address": "https://pvp.qq.com/match/kpl/KPL2021S2/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "winter_champion_cup",
      "league_id": "20210005",
      "start_time": "2021-12-31 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/20210005.jpg",
      "is_top": 1,
      "end_time": "2022-01-15 23:59:59",
      "league_name": "2021年王者荣耀挑战者杯",
      "season": 2,
      "year": 2021,
      "cc_league_id": "KCC2021S2",
      "live_room_address": "https://pvp.qq.com/match/kpl/KCC2021S2/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20220001",
      "start_time": "2022-02-09 00:00:00",
      "league_icon": "https://res.edata.qq.com/sgame/static/images/league/KPL2022S1.jpg",
      "is_top": 1,
      "end_time": "2022-05-08 23:59:59",
      "league_name": "2022年KPL春季赛",
      "season": 1,
      "year": 2022,
      "cc_league_id": "KPL2022S1",
      "live_room_address": "https://pvp.qq.com/match/kpl/KPL2022S1/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20220002",
      "start_time": "2022-06-08 00:00:00",
      "league_icon": "http://dldir1.qq.com/tgatv/wzry_tv/2022KPLsummer/2022KPLsummerkaisai.jpg",
      "is_top": 1,
      "end_time": "2022-09-08 13:26:05",
      "league_name": "2022年KPL夏季赛",
      "season": 2,
      "year": 2022,
      "cc_league_id": "KPL2022S2",
      "live_room_address": "https://pvp.qq.com/match/kpl/KPL2022S2/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "winter_champion_cup",
      "league_id": "20220003",
      "start_time": "2022-09-13 00:00:00",
      "league_icon": "http://dldir1.qq.com/tgatv/wzry_tv/2022challenger/kv/2022tiaozhanzhebei01.jpg",
      "is_top": 1,
      "end_time": "2022-10-08 00:00:05",
      "league_name": "2022年王者荣耀挑战者杯",
      "season": 1,
      "year": 2022,
      "cc_league_id": "KCC2022S1",
      "live_room_address": "https://pvp.qq.com/match/kpl/KCC2022S1/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20230001",
      "start_time": "2023-02-10 00:00:00",
      "league_icon": "https://smobatv-pic.tga.qq.com/d61f68a4aa435427392d070c80ef86e4.png",
      "is_top": 1,
      "end_time": "2023-06-02 00:00:05",
      "league_name": "2023年KPL春季赛",
      "season": 1,
      "year": 2023,
      "cc_league_id": "KPL2023S1",
      "live_room_address": "https://pvp.qq.com/match/kpl/KPL2023S1/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20230002",
      "start_time": "2023-06-14 00:00:00",
      "league_icon": "https://smobatv-pic.tga.qq.com/b1ecf9198a9277e437de5a707de13bef.png",
      "is_top": 1,
      "end_time": "2023-09-10 21:10:05",
      "league_name": "2023年KPL夏季赛",
      "season": 1,
      "year": 2023,
      "cc_league_id": "KPL2023S2",
      "live_room_address": "https://pvp.qq.com/match/kpl/KPL2023S2/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "winter_champion_cup",
      "league_id": "20230003",
      "start_time": "2023-10-13 00:00:00",
      "league_icon": "https://smobatv-pic.tga.qq.com/228037f3c775bb2158edbe3366541e0d.png",
      "is_top": 1,
      "end_time": "2023-11-05 23:59:59",
      "league_name": "2023年王者荣耀挑战者杯",
      "season": 1,
      "year": 2023,
      "cc_league_id": "KCC2023",
      "live_room_address": "https://pvp.qq.com/match/kpl/KCC2023/index.shtml"
    },
    {
      "status": 2,
      "league_type_name": "kpl",
      "league_id": "20240001",
      "start_time": "2024-01-31 00:00:00",
      "league_icon": "https://smobatv-pic.tga.qq.com/fbc42171de8c11964468fd98ac27fdae.png",
      "is_top": 1,
      "end_time": "2024-05-21 00:00:05",
      "league_name": "2024年KPL春季赛",
      "season": 1,
      "year": 2024,
      "cc_league_id": "KPL2024S1",
      "live_room_address": "https://pvp.qq.com/match/kpl/KPL2024S1/index.shtml"
    }
  ]
}
'''

# 解析 JSON 数据
data = json.loads(json_data)

# 准备 SQL 插入语句
sql_inserts = []
for result in data['results']:
    league_id = result['league_id']
    league_type_name = result['league_type_name']
    start_time = result['start_time']
    end_time = result['end_time']
    league_name = result['league_name']
    season = result['season']
    year = result['year']
    league_icon = result['league_icon']
    is_top = result['is_top']

    sql = f"INSERT INTO League (league_id, league_type_name, start_time, end_time, league_name, season, year, league_icon, is_top) VALUES ({league_id}, '{league_type_name}', '{start_time}', '{end_time}', '{league_name}', {season}, {year}, '{league_icon}', {is_top});"
    sql_inserts.append(sql)

# 将生成的 SQL 插入语句输出到文件
with open('league.sql', 'a', encoding='utf-8') as f:
    for sql_insert in sql_inserts:
        f.write(sql_insert + '\n')

print("SQL 插入语句已成功生成并写入文件 'insert_queries.sql'")
