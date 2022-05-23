package main

import (
    "os"
    "github.com/beego/beego/v2/client/orm"
    "github.com/beego/beego/v2/client/orm/migration"
    _ "github.com/lib/pq"
)

func init() {
    orm.RegisterDataBase("default", "postgres", "postgresql://bst:bst@bst-db-postgres:5432/bst_go_beego?sslmode=disable")
}

func main() {
    task := "upgrade"
    switch task {
    case "upgrade":
        if err := migration.Upgrade(1649610800); err != nil {
            os.Exit(2)
        }
    case "rollback":
        if err := migration.Rollback("Entity20220410_171320"); err != nil {
            os.Exit(2)
        }
    case "reset":
        if err := migration.Reset(); err != nil {
            os.Exit(2)
        }
    case "refresh":
        if err := migration.Refresh(); err != nil {
            os.Exit(2)
        }
    }
}
