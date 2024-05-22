from pathlib import Path
import requests

import requestparams

if __name__ == '__main__':
   print()
   # payload={'season_id':'43','team_id':'all','start_date':'2023-10-13','end_date':'2023-11-05','acctype':'qq','location':'cn'}
   # url='https://smobac.odp.qq.com/datamore/smobac/season/games'
   # response=requests.get(url=url,headers=headers,params=payload)
   # path = Path("response.json")
   # path.write_text(response.text)

   # url='https://pvp.qq.com/web201605/js/item.json'
   # response=requests.get(url=url,headers=headers)
   # path=Path("items.json")
   # path.write_text(response.text)

   # url="https://pvp.qq.com/web201605/js/summoner.json"
   # response=requests.get(url=url,headers=requestparams.headers)
   # path=Path("summoner.json")
   # path.write_text(response.text)

   # url="https://pvp.qq.com/web201605/js/herolist.json"
   # response=requests.get(url=url,headers=requestparams.headers)
   # path=Path("heroes.json")
   # path.write_text(response.text)

   # url="https://pvp.qq.com/web201605/js/ming.json"
   # response=requests.get(url=url,headers=requestparams.headers)
   # path=Path("ming.json")
   # path.write_text(response.text)

   url="https://prod.comp.smoba.qq.com/leaguesite/leagues/open"
   response=requests.get(url=url,headers=requestparams.headers)
   path=Path("leagues.json")
   path.write_text(response.text)