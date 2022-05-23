package service

import (
    "bst_go_beego/models"
    "bst_go_beego/repository"
)

// EntityAdd - Add entity
func EntityAdd(data models.EntityPost) int {
    return repository.EntityAdd(data)
}

// EntityDeleteAll - Delete all entities
func EntityDeleteAll() {
    repository.EntityDeleteAll()
}

// EntityGetOne - Get one entity
func EntityGetOne(name string) models.Entity {
    return repository.EntityGetOne(name)
}

// EntityGetOneFib - Get one entity with fibonacci number
func EntityGetOneFib(name string, mode string) models.EntityFib {
    entity := repository.EntityGetOne(name)
    fibNumber := FibCalc(entity.Number, mode)

    entityFib := models.EntityFib{
        ID:        entity.ID,
        Name:      entity.Name,
        FibNumber: fibNumber,
    }

    return entityFib
}
