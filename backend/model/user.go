package model

import (
	"encoding/base64"
	"golang.org/x/crypto/scrypt"
	"log"
)

type SignUpParam struct {
	Age        int    `json:"age" binding:"gte=16,lte=130"`
	Name       string `json:"name" binding:"required"`
	Email      string `json:"email" binding:"required,email"`
	Password   string `json:"password" binding:"required"`
	RePassword string `json:"re_password" binding:"required,eqfield=Password"`
	Agreement  bool   `json:"agreement" binding:"eq=true"`
}

type LoginParam struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

type User struct {
	UserID   int    `db:"user_id"`
	Username string `db:"username"`
	Password string `db:"password"`
	Email    string `db:"email"`
}

func CheckLogin(username string, password string) interface{} {
	sqlStr := "select * from user where username = ?"
	var user []User
	err = db.Select(&user, sqlStr, username)
	if err != nil {
		return err.Error()
	}
	if len(user) == 0 {
		return "用户不存在"
	}
	if user[0].Password != ScryptPw(password) {
		return "密码错误"
	}
	return nil
}

func SignUp(username, password, email string) interface{} {
	msg := CheckUser(username)
	if msg != nil {
		return msg
	}
	sqlStr := "insert into user(username,password,email) values(?,?,?)"
	_, err := db.Exec(sqlStr, username, ScryptPw(password), email)
	if err != nil {
		return err.Error()
	}
	return nil
}

func ScryptPw(password string) string {
	const KeyLen = 10
	salt := make([]byte, 8)
	salt = []byte{12, 32, 43, 54, 65, 76, 87, 98}
	key, err := scrypt.Key([]byte(password), salt, 1<<15, 8, 1, KeyLen)
	if err != nil {
		log.Fatal(err)
	}
	str := base64.StdEncoding.EncodeToString(key)
	return str
}

func CheckUser(username string) interface{} {
	var user []User
	sqlStr := "select * from user where username = ?"
	err = db.Select(&user, sqlStr, username)
	if err != nil {
		return err.Error()
	}
	if len(user) > 0 {
		return "用户名已存在"
	}
	return nil
}
