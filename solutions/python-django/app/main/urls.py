from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.index, name='index'),
    path('cycle_sum', controllers.cycle_sum, name='cycle_sum'),
    path('fib', controllers.fib, name='fib'),
]
