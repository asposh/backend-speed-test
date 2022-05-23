package database

import (
    "github.com/beego/beego/v2/client/orm"
    "github.com/beego/beego/v2/core/config"
    "os"

    // Initialise postgres DB driver
    _ "github.com/lib/pq"
)

// InitPostgres - Initialise postgres DB
func InitPostgres() {
    runMode := os.Getenv("RUN_MODE")
    mountDir := os.Getenv("CURRENT_MOUNT_DIR")
    if runMode == "" {
        runMode = "prod"
    }

    conf, _ := config.NewConfig("ini", mountDir+"/app/conf/app.conf")
    postgresURL, _ := conf.String(runMode + "::postgres_url")
    orm.RegisterDriver("postgres", orm.DRPostgres)

    _, err := orm.GetDB("default")
    if err != nil {
        orm.RegisterDataBase("default", "postgres", postgresURL)
    }
}
