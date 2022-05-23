package repository

import (
    "bst_go_beego/database"
    "bst_go_beego/models"
    "github.com/beego/beego/v2/client/orm"

    // Initialise models
    _ "bst_go_beego/models"
)

func init() {
    database.InitPostgres()
}

// EntityAdd - Add entity
func EntityAdd(data models.EntityPost) int {
    o := orm.NewOrm()
    entity := &models.Entity{
        Name:   data.Name,
        Number: data.Number,
    }
    id64, _ := o.Insert(entity)
    id := int(id64)

    return id
}

// EntityDeleteAll - Delete all entities
func EntityDeleteAll() {
    o := orm.NewOrm()
    o.Raw("DELETE FROM entity").Exec()
}

// EntityGetOne - Get one entity
func EntityGetOne(name string) models.Entity {
    o := orm.NewOrm()
    entity := models.Entity{}
    err := o.QueryTable("entity").Filter("Name", name).RelatedSel().One(&entity)

    if err != nil {
        panic(err)
    }

    return entity
}
