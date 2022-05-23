package models

import (
	"github.com/beego/beego/v2/client/orm"
)

// Entity structure
type Entity struct {
	ID     int    `json:"id"   orm:"column(id);pk;auto;"`
	Name   string `json:"name" orm:"unique;"`
	Number int    `json:"number"`
}

// EntityPost structure
type EntityPost struct {
	Name   string
	Number int
}

// EntityFib structure
type EntityFib struct {
	ID        int    `json:"id"`
	Name      string `json:"name"`
	FibNumber int    `json:"fib_number"`
}

func init() {
	orm.RegisterModel(new(Entity))
}
