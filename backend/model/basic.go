package model

type Summoner struct {
	SummonerID          int    `db:"summoner_id" json:"summoner_id"`
	SummonerName        string `db:"summoner_name" json:"summoner_name"`
	SummonerRank        string `db:"summoner_rank" json:"summoner_rank"`
	SummonerDescription string `db:"summoner_description" json:"summoner_description"`
}

type Item struct {
	ItemID     int    `db:"item_id" json:"item_id"`
	ItemName   string `db:"item_name" json:"item_name"`
	ItemType   string `db:"item_type" json:"item_type"`
	Price      int    `db:"price" json:"price"`
	TotalPrice int    `db:"total_price" json:"total_price"`
	Pos        string `db:"pos" json:"pos"`
}

type Ming struct {
	MingID    int    `db:"ming_id" json:"ming_id"`
	MingName  string `db:"ming_name" json:"ming_name"`
	MingType  string `db:"ming_type" json:"ming_type"`
	MingGrade int    `db:"ming_grade" json:"ming_grade"`
	MingDes   string `db:"ming_des" json:"ming_des"`
}

func GetSummoner(name string) ([]Summoner, interface{}) {
	sqlStr := "select * from Summoner where summoner_name like ?"
	var summoner []Summoner
	err := db.Select(&summoner, sqlStr, "%"+name+"%")
	if err != nil {
		return nil, err.Error()
	}
	if len(summoner) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return summoner, nil
}

func GetItem(name string) ([]Item, interface{}) {
	sqlStr := "select item_id, item_name, total_price, price, pos from item NATURAL JOIN item_pos where item_name like ?"
	var item []Item
	err := db.Select(&item, sqlStr, "%"+name+"%")
	if err != nil {
		return nil, err.Error()
	}
	if len(item) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return item, nil
}

func GetMing(name, mtype string, grade int) ([]Ming, interface{}) {
	var err error
	sqlStr := "select ming_id, ming_name,ming_type, ming_grade, ming_des from ming where ming_name like ?"
	var ming []Ming
	if grade == 0 {
		if mtype == "" {
			err = db.Select(&ming, sqlStr, "%"+name+"%")
		} else {
			sqlStr = sqlStr + " and ming_type = ?"
			err = db.Select(&ming, sqlStr, "%"+name+"%", mtype)
		}
	} else {
		sqlStr = sqlStr + " and ming_grade like ?"
		if mtype == "" {
			err = db.Select(&ming, sqlStr, "%"+name+"%", grade)
		} else {
			sqlStr = sqlStr + " and ming_type = ?"
			err = db.Select(&ming, sqlStr, "%"+name+"%", grade, mtype)
		}
	}
	if err != nil {
		return nil, err.Error()
	}
	if len(ming) == 0 {
		return nil, "结果为空！更改搜索条件后重试"
	}
	return ming, nil
}
