from entity.models import Entity
from asgiref.sync import sync_to_async


class EntityRepository():
    """
    Entity repository
    """

    @sync_to_async
    def add(self, data: dict) -> int:
        """ Add entity """

        entity = Entity(name=data["name"], number=data["number"])
        entity.save()

        return entity.id

    @sync_to_async
    def delete_all(self) -> None:
        """ Delete all entities """

        Entity.objects.all().delete()

    @sync_to_async
    def get_one(self, name: str) -> Entity:
        """ Get one entity by name """

        entity = Entity.objects.get(name=name)
        return entity
