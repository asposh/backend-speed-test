package test

import (
    "bst_go_beego/service"
    "fmt"
    "github.com/stretchr/testify/assert"
    "testing"
)

var (
    testNumberFib = 10
)

// Test index
func TestIndex(t *testing.T) {
    cl := Client{
        Method: "GET",
        URL:    "https://localhost",
        Data:   nil,
    }
    statusCode, jsonData := cl.Request()

    assert.Equal(t, statusCode, 200)
    assert.Equal(t, jsonData["message"], "Default index")
}

// Test cycle sum
func TestCycleSum(t *testing.T) {
    requestNumber := fmt.Sprintf("%v", testNumberFib)

    cl := Client{
        Method: "GET",
        URL:    "https://localhost/cycle_sum?number=" + requestNumber,
        Data:   nil,
    }
    statusCode, jsonData := cl.Request()

    assert.Equal(t, statusCode, 200)
    assert.EqualValues(t, jsonData["cycle_sum"], service.CycleSum(testNumberFib))
}

//  Fibonacci controller test recursive
func TestFibRecursive(t *testing.T) {
    fibTestByMode(testNumberFib, "recursive", t)
}

//  Fibonacci controller test iterative
func TestFibIterative(t *testing.T) {
    fibTestByMode(testNumberFib, "iterative", t)
}

// fibTestByMode - Fibonacci test by mode
func fibTestByMode(number int, mode string, t *testing.T) {
    requestNumber := fmt.Sprintf("%v", number)

    cl := Client{
        Method: "GET",
        URL:    "https://localhost/fib?number=" + requestNumber + "&mode=" + mode,
        Data:   nil,
    }
    statusCode, jsonData := cl.Request()

    assert.Equal(t, statusCode, 200)
    assert.EqualValues(t, jsonData["fib_number"], service.FibCalc(number, mode))
}
