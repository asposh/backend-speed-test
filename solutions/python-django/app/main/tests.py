from asgiref.sync import async_to_sync
from django.test import TestCase, Client
from main.calculation import Calculation


class IndexTestCase(TestCase):
    """
    Index test
    """

    def setUp(self) -> None:
        self.number = 10

    def test_index(self) -> None:
        """ Index test """

        c = Client()
        json_response = c.get('').json()
        assert json_response['message'] == 'Default index'

    def test_cycle_sum(self) -> None:
        """ Cycle sum controller test """

        c = Client()
        data = {
            "number": self.number
        }
        json_response = c.get('/cycle_sum', data).json()

        cycle_sum_calc = async_to_sync(Calculation.cycle_sum)
        cycle_sum = cycle_sum_calc(self.number)
        assert json_response['cycle_sum'] == cycle_sum

    def test_fib_recursive(self) -> None:
        """ Fibonacci controller test recursive """

        self.__fib_by_mode_test(self.number, "recursive")

    def test_fib_iterative(self) -> None:
        """ Fibonacci controller test iterative """

        self.__fib_by_mode_test(self.number, "iterative")

    def __fib_by_mode_test(self, number: int, mode: str) -> None:
        """ Fibonacci test by mode """

        c = Client()
        data = {
            "number": number,
            "mode": mode,
        }
        json_response = c.get('/fib', data).json()

        fibonacci_calc = async_to_sync(Calculation.fib)
        test_fib = fibonacci_calc(self.number, "iterative")
        assert json_response['fib_number'] == test_fib
