from .repository import EntityRepository
from entity.models import Entity
from main.calculation import Calculation


class EntityService():
    """
    Entity service
    """

    def __init__(self):
        self.repository = EntityRepository()

    async def add(self, data: dict) -> int:
        """ Add entity """

        id = await self.repository.add(data)
        return id

    async def delete_all(self) -> None:
        """ Delete all entities """

        await self.repository.delete_all()

    async def get_one(self, name: str) -> Entity:
        """ Get one entity by name """

        entity = await self.repository.get_one(name)
        return entity

    async def get_one_fib(self, name: str, mode: str) -> Entity:
        """ Get one entity with fibonacci number """

        entity = await self.get_one(name)
        entity.fib_number = await Calculation.fib(entity.number, mode)

        return entity
