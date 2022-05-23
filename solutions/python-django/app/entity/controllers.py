from django.http import JsonResponse
from .service import EntityService

entity_service = EntityService()


async def index(request) -> JsonResponse:
    """ Entity index controller """

    # Add entity
    if request.method == 'POST':
        name = request.POST.get("name", "")
        number = request.POST.get("number", 0)

        id = await entity_service.add({
            'name': name,
            'number': number,
        })

        return JsonResponse({'id': id})

    # Default entity index controller
    return JsonResponse({'message': 'Entity controller'})


async def delete_all(request) -> JsonResponse:
    """ Delete all entities """

    await entity_service.delete_all()
    return JsonResponse({'message': 'Deleted'})


async def get_one(request, name: str = "") -> JsonResponse:
    """ Get one entity """

    entity = await entity_service.get_one(name)

    return JsonResponse({
        'id': entity.id,
        'name': entity.name,
        'number': entity.number,
    })


async def get_one_fib_recursive(request, name: str = "") -> JsonResponse:
    """ Get one entity with recursive fibonacci number """

    entity = await entity_service.get_one_fib(name, 'recursive')

    return JsonResponse({
        'id': entity.id,
        'name': entity.name,
        'fib_number': entity.fib_number,
    })


async def get_one_fib_iterative(request, name: str = "") -> JsonResponse:
    """ Get one entity with iterative fibonacci number """

    entity = await entity_service.get_one_fib(name, 'iterative')

    return JsonResponse({
        'id': entity.id,
        'name': entity.name,
        'fib_number': entity.fib_number,
    })
