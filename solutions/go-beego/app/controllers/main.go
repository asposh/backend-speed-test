package controllers

import (
    "bst_go_beego/service"
    "github.com/beego/beego/v2/server/web"
)

// MainController type
type MainController struct {
    web.Controller
}

// Index - Index controller
func (mc *MainController) Index() {
    mc.Data["json"] = map[string]string{"message": "Default index"}
    mc.ServeJSON()
}

// CycleSum - Cycle sum controller
func (mc *MainController) CycleSum() {
    number, _ := mc.GetInt("number")

    sum := service.CycleSum(number)

    mc.Data["json"] = map[string]int64{"cycle_sum": sum}
    mc.ServeJSON()
}

// Fib - Fibonacci controller
func (mc *MainController) Fib() {
    number, _ := mc.GetInt("number")
    mode := mc.GetString("mode")

    fibNumber := service.FibCalc(number, mode)

    mc.Data["json"] = map[string]int{"fib_number": fibNumber}
    mc.ServeJSON()
}
