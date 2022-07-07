package com.bst.bstJavaSpring.bstMain;

/**
 * Bst calculation service.
 */
public class BstCalculationService {

    /**
     * Calc cycle sum.
     *
     * @param number
     * @return sum
     */
    public static Long cycleSum(int number) {
        Long sum = 0L;
        for (int i = 0; i < number; i++) {
             sum += i;
        }

        return sum;
    }

    /**
     * Calc fibonacci number.
     *
     * @param number
     * @param mode
     * @return fibonacci number
     */
    public static int fib(int number, String mode) {
        if (mode.equals("recursive")) {
            return fibRecursive(number);
        }

        if (mode.equals("iterative")) {
            return fibIterative(number);
        }

        return 0;
    }

    /**
     * Calc fibonacci number recursive.
     *
     * @param number
     * @return fibonacci number
     */
    public static int fibRecursive(int number) {
        if (number == 0) {
            return 0;
        }
        if (number == 1) {
            return 1;
        }

        return fibRecursive(number - 1) + fibRecursive(number - 2);
    }

    /**
     * Calc fibonacci number iterative.
     *
     * @param number
     * @return fibonacci number
     */
    public static int fibIterative(int number) {
        if (number == 0) {
            return 0;
        }

        int temp = 0;
        int num1 = 0;
        int num2 = 1;

        for (int i = 1; i < number; i++) {
            temp = num1;
            num1 = num2;
            num2 = temp + num1;
        }

        return num2;
    }
}
