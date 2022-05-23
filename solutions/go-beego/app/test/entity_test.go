package test

import (
	"bst_go_beego/models"
	"bst_go_beego/service"
	"fmt"
	"github.com/stretchr/testify/assert"
	"testing"
)

var (
	testName   = "test_name"
	testNumber = 10
)

// Entity index controller test
func TestEntityIndex(t *testing.T) {
	cl := Client{
		Method: "GET",
		URL:    "https://localhost/entity/",
	}
	statusCode, jsonData := cl.Request()

	assert.Equal(t, statusCode, 200)
	assert.Equal(t, jsonData["message"], "Entity controller")
}

// Add entity test
func TestEntityAdd(t *testing.T) {
	service.EntityDeleteAll()

	data := map[string]interface{}{
		"name":   testName,
		"number": fmt.Sprintf("%v", testNumber),
	}
	cl := Client{
		Method: "POST",
		URL:    "https://localhost/entity/",
		Data:   data,
	}
	statusCode, jsonData := cl.Request()

	assert.Equal(t, statusCode, 200)
	assert.Contains(t, jsonData, "id")

	testEntity := service.EntityGetOne(testName)
	assert.Equal(t, testEntity.Name, testName)
	assert.Equal(t, testEntity.Number, testNumber)
}

// Delete all entities test
func TestEntityDeleteAll(t *testing.T) {
	cl := Client{
		Method: "GET",
		URL:    "https://localhost/entity/delete_all",
	}
	statusCode, jsonData := cl.Request()

	assert.Equal(t, statusCode, 200)
	assert.Equal(t, jsonData["message"], "Deleted")
}

// Get one entity test
func TestEntityGetOne(t *testing.T) {
	add()
	cl := Client{
		Method: "GET",
		URL:    "https://localhost/entity/" + testName,
	}
	statusCode, jsonData := cl.Request()

	assert.Equal(t, statusCode, 200)
	assert.Contains(t, jsonData, "id")
	assert.Equal(t, jsonData["name"], testName)
	assert.EqualValues(t, jsonData["number"], testNumber)
}

// Get one entity with recursive fibonacci number
func TestEntityGetOneFibRecursive(t *testing.T) {
	add()
	cl := Client{
		Method: "GET",
		URL:    "https://localhost/entity/fib_recursive/" + testName,
	}
	statusCode, jsonData := cl.Request()

	assert.Equal(t, statusCode, 200)
	assert.Contains(t, jsonData, "id")
	assert.Equal(t, jsonData["name"], testName)
	assert.EqualValues(t, jsonData["fib_number"], service.FibCalc(testNumber, "iterative"))
}

// Get one entity with iterative fibonacci number
func TestEntityGetOneFibIterative(t *testing.T) {
	add()
	cl := Client{
		Method: "GET",
		URL:    "https://localhost/entity/fib_iterative/" + testName,
	}
	statusCode, jsonData := cl.Request()

	assert.Equal(t, statusCode, 200)
	assert.Contains(t, jsonData, "id")
	assert.Equal(t, jsonData["name"], testName)
	assert.EqualValues(t, jsonData["fib_number"], service.FibCalc(testNumber, "iterative"))
}

// Add entity
func add() {
	service.EntityDeleteAll()
	service.EntityAdd(models.EntityPost{
		Name:   testName,
		Number: testNumber,
	})
}
