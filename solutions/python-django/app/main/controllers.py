from django.http import JsonResponse
from .calculation import Calculation


async def index(request) -> JsonResponse:
    """ Index main controller """

    return JsonResponse({'message': 'Default index'})


async def cycle_sum(request) -> JsonResponse:
    """ Cycle sum controller """

    number = int(request.GET.get("number", 0))
    cycle_sum = await Calculation.cycle_sum(number)

    return JsonResponse({'cycle_sum': cycle_sum})


async def fib(request) -> JsonResponse:
    """ Fibonacci controller """

    number = int(request.GET.get("number", 0))
    mode = request.GET.get("mode", "")
    fib_number = await Calculation.fib(number, mode)

    return JsonResponse({'fib_number': fib_number})
