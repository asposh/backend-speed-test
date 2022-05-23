from django.urls import path
from . import controllers

urlpatterns = [
    path(
        '',
        controllers.index,
        name='entity_index'
    ),
    path(
        'delete_all',
        controllers.delete_all,
        name='entity_delete_all'
    ),
    path(
        'fib_recursive/<str:name>',
        controllers.get_one_fib_recursive,
        name='entity_get_one_fib_recursive'
    ),
    path(
        'fib_iterative/<str:name>',
        controllers.get_one_fib_iterative,
        name='entity_get_one_fib_iterative'
    ),
    path(
        '<str:name>',
        controllers.get_one,
        name='entity_get_one'
    ),
]
