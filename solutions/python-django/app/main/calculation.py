class Calculation():
    """
    Calculation number service
    """

    async def cycle_sum(number: int) -> int:
        """ Calc cycle sum """

        cycle_sum = 0
        for i in range(number):
            cycle_sum += i
        return cycle_sum

    async def fib(number: int, mode: str) -> int:
        """ Calc fibonacci number """

        if mode == 'recursive':
            return await Calculation.__fib_recursive(number)

        if mode == 'iterative':
            return await Calculation.__fib_iterative(number)

    async def __fib_recursive(number: int) -> int:
        """ Calc fibonacci recursive """

        if number == 0:
            return 0

        if number == 1:
            return 1

        return (
            await Calculation.__fib_recursive(number - 1)
            + await Calculation.__fib_recursive(number - 2)
        )

    async def __fib_iterative(number: int) -> int:
        """ Calc fibonacci iterative """

        if number == 0:
            return 0

        num1 = 0
        num2 = 1

        for n in range(1, number):
            temp = num1
            num1 = num2
            num2 = temp + num1

        return num2
