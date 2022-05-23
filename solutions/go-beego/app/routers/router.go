package routers

import (
    "bst_go_beego/controllers"
    "github.com/beego/beego/v2/server/web"
)

func init() {
    web.Router("/", &controllers.MainController{}, "get:Index")
    web.Router("/cycle_sum", &controllers.MainController{}, "get:CycleSum")
    web.Router("/entity/delete_all", &controllers.EntityController{}, "get:DeleteAll")
    web.Router("/entity/fib_recursive/:name", &controllers.EntityController{}, "get:GetOneFibRecursive")
    web.Router("/entity/fib_iterative/:name", &controllers.EntityController{}, "get:GetOneFibIterative")
    web.Router("/entity/:name", &controllers.EntityController{}, "get:GetOne")
    web.Router("/entity", &controllers.EntityController{}, "get:Index;post:Add")
    web.Router("/fib", &controllers.MainController{}, "get:Fib")
}
