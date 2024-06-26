package utils

import "gopkg.in/ini.v1"

var (
	AppMode      string
	HttpPort     string
	JwtKey       string
	Db           string
	DbHost       string
	DbPort       string
	DbUser       string
	DbPassWord   string
	DbName       string
	MaxOpenConns int
	MaxIdleConns int
)

func init() {
	file, err := ini.Load("./conf/config.ini")
	if err != nil {
		panic(err)
	}
	LoadServer(file)
	LoadData(file)
}

func LoadServer(file *ini.File) {
	AppMode = file.Section("server").Key("AppMode").MustString("debug")
	HttpPort = file.Section("server").Key("HttpPort").MustString(":3000")
	JwtKey = file.Section("server").Key("JwtKey").MustString("")
}

func LoadData(file *ini.File) {
	Db = file.Section("database").Key("Db").MustString("mysql")
	DbHost = file.Section("database").Key("DbHost").MustString("localhost")
	DbPort = file.Section("database").Key("DbPort").MustString("3306")
	DbUser = file.Section("database").Key("DbUser").MustString("root")
	DbPassWord = file.Section("database").Key("DbPassWord").MustString("123456")
	DbName = file.Section("database").Key("Dbname").MustString("dbcourse")
	MaxOpenConns = file.Section("database").Key("MaxOpenConns").MustInt(20)
	MaxIdleConns = file.Section("database").Key("MaxIdleConns").MustInt(10)
}
