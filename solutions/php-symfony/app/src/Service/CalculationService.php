<?php

namespace App\Service;

/**
 * Calculation service
 */
class CalculationService
{
    /**
     * Calc cycle sum
     *
     * @param int $number
     * @return int
     */
    public static function cycleSum(int $number): int
    {
        $sum = 0;
        for ($i = 0; $i < $number; $i++) {
             $sum += $i;
        }

        return $sum;
    }

    /**
     * Calc fibonacci number
     *
     * @param int $number
     * @return int
     */
    public static function fib(int $number, string $mode): int
    {
        if ($mode == 'recursive') {
            return self::fibRecursive($number);
        }

        if ($mode == 'iterative') {
            return self::fibIterative($number);
        }

        return 0;
    }

    /**
     * Calc fibonacci recursive
     *
     * @param int $number
     * @return int
     */
    private static function fibRecursive(int $number): int
    {
        if ($number == 0) {
            return 0;
        }

        if ($number == 1) {
            return 1;
        }

        return self::fibRecursive($number - 1) + self::fibRecursive($number - 2);
    }

    /**
     * Calc fibonacci iterative
     *
     * @param int $number
     * @return int
     */
    private static function fibIterative(int $number)
    {
        if ($number == 0) {
            return 0;
        }

        $num1 = 0;
        $num2 = 1;

        for ($i = 1; $i < $number; $i++) {
            $temp = $num1;
            $num1 = $num2;
            $num2 =  $temp + $num1;
        }

        return $num2;
    }
}
