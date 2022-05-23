package controllers

import (
	"bst_go_beego/models"
	"bst_go_beego/service"
	"github.com/beego/beego/v2/server/web"
)

// EntityController structure
type EntityController struct {
	web.Controller
}

// Add - Add entity
func (ec *EntityController) Add() {
	name := ec.GetString("name")
	number, _ := ec.GetInt("number")

	data := models.EntityPost{
		Name:   name,
		Number: number,
	}
	id := service.EntityAdd(data)

	ec.Data["json"] = map[string]int{"id": id}
	ec.ServeJSON()
}

// DeleteAll - delete all entities
func (ec *EntityController) DeleteAll() {
	service.EntityDeleteAll()

	ec.Data["json"] = map[string]string{"message": "Deleted"}
	ec.ServeJSON()
}

// GetOne - Get one entity
func (ec *EntityController) GetOne() {
	name := ec.Ctx.Input.Param(":name")
	entity := service.EntityGetOne(name)

	ec.Data["json"] = entity
	ec.ServeJSON()
}

// GetOneFibRecursive - Get one entity with recursive fibonacci number
func (ec *EntityController) GetOneFibRecursive() {
	name := ec.Ctx.Input.Param(":name")
	entity := service.EntityGetOneFib(name, "recursive")

	ec.Data["json"] = entity
	ec.ServeJSON()
}

// GetOneFibIterative - Get one entity with iterative fibonacci number
func (ec *EntityController) GetOneFibIterative() {
	name := ec.Ctx.Input.Param(":name")
	entity := service.EntityGetOneFib(name, "iterative")

	ec.Data["json"] = entity
	ec.ServeJSON()
}

// Index - Entity index
func (ec *EntityController) Index() {
	ec.Data["json"] = map[string]string{"message": "Entity controller"}
	ec.ServeJSON()
}
