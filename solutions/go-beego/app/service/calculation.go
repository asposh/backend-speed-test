package service

// CycleSum - calc cycle sum
func CycleSum(number int) int64 {
    sum := 0
    for i := 0; i < number; i++ {
        sum += i
    }
    return int64(sum)
}

// FibCalc - calc fibonacci number
func FibCalc(number int, mode string) int {
    if mode == "recursive" {
        return fibRecursive(number)
    }
    if mode == "iterative" {
        return fibIterative(number)
    }

    return 0
}

// Calc fibonacci recursive
func fibRecursive(number int) int {
    if number == 0 {
        return 0
    }
    if number == 1 {
        return 1
    }

    return fibRecursive(number-1) + fibRecursive(number-2)
}

// Calc fibonacci iterative
func fibIterative(number int) int {
    if number == 0 {
        return 0
    }

    temp := 0
    num1 := 0
    num2 := 1

    for i := 1; i < number; i++ {
        temp = num1
        num1 = num2
        num2 = temp + num1
    }

    return num2
}
