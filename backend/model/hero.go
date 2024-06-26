package model

type Hero struct {
	HeroId   int    `json:"hero_id" db:"hero_id"`
	HeroName string `json:"hero_name" db:"hero_name"`
	Title    string `json:"title" db:"title"`
	HeroType string `json:"hero_type" db:"hero_type"`
	Pos      string `json:"pos" db:"pos"`
}

type HeroInfo struct {
	Hero
	Skills []HeroSkill
	Skin   []HeroSkin
}

type HeroSkill struct {
	SkillName   string `json:"skill_name" db:"skill_name"`
	CoolDown    string `json:"cool_down" db:"cooldown"`
	Cost        string `json:"cost" db:"cost"`
	Description string `json:"description" db:"description"`
	ImgUrl      string `json:"img_url" db:"image_source"`
}

type HeroSkin struct {
	SkinId   int    `json:"skin_id" db:"skin_id"`
	SkinName string `json:"skin_name" db:"skin_name"`
}

// 查询单条数据示例
//func queryRowDemo() {
//	sqlStr := "select id, name, age from user where id=?"
//	var u User
//	err := db.Get(&u, sqlStr, 1)
//	if err != nil {
//		fmt.Printf("get failed, err:%v\n", err)
//		return
//	}
//	fmt.Printf("id:%d name:%s age:%d\n", u.ID, u.Name, u.Age)
//}
//
//// 查询多条数据示例
//func queryMultiRowDemo() {
//	sqlStr := "select id, name, age from user where id > ?"
//	var users []User
//	err := db.Select(&users, sqlStr, 0)
//	if err != nil {
//		fmt.Printf("query failed, err:%v\n", err)
//		return
//	}
//	fmt.Printf("users:%#v\n", users)
//}

func GetHero(name, pos string) ([]Hero, interface{}) {
	sqlStr := "select hero_id, hero_name, title, hero_type,pos from hero NATURAL JOIN hero_pos where hero_name like ? and pos like ?"
	var hero []Hero
	err := db.Select(&hero, sqlStr, "%"+name+"%", "%"+pos+"%")
	if err != nil {
		return nil, err.Error()
	}
	if len(hero) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return hero, nil
}

func GetHeroInfo(id int) (HeroInfo, interface{}) {
	sqlStr := "select hero_id, hero_name, title, hero_type, pos from hero NATURAL JOIN hero_pos where hero_id = ?"
	var tmpHero []Hero
	var heroInfo HeroInfo
	err := db.Select(&tmpHero, sqlStr, id)
	if err != nil {
		return HeroInfo{}, err.Error()
	}
	if len(tmpHero) == 0 {
		return HeroInfo{}, "结果为空！更改搜索条件后重试"
	}
	sqlStr = "select skill_name, cooldown, cost, description, image_source from hero_skill where hero_id = ?"
	var skills []HeroSkill
	err = db.Select(&skills, sqlStr, id)
	if err != nil {
		return HeroInfo{}, err.Error()
	}
	sqlStr = "select skin_name,skin_id from hero_skin where hero_id = ?"
	var skins []HeroSkin
	err = db.Select(&skins, sqlStr, id)
	if err != nil {
		return HeroInfo{}, err.Error()
	}
	heroInfo = HeroInfo{
		Hero:   tmpHero[0],
		Skills: skills,
		Skin:   skins,
	}
	return heroInfo, nil
}
