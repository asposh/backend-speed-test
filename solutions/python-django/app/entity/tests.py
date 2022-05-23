from asgiref.sync import async_to_sync
from django.test import TestCase, Client
from main.calculation import Calculation
from .service import EntityService


class EntityTestCase(TestCase):
    """
    Entity test
    """

    def setUp(self) -> None:
        self.entity_service = EntityService()
        self.test_entity = {
            'name': 'test_name',
            'number': 6,
        }

    def test_index(self) -> None:
        """ Index entity test """

        c = Client()
        json_response = c.get('/entity/').json()

        assert json_response['message'] == 'Entity controller'

    def test_add(self) -> None:
        """ Add entity test """

        c = Client()
        json_response = c.post('/entity/', self.test_entity).json()
        self.assertIn('id', json_response)
        get_one = async_to_sync(self.entity_service.get_one)
        entity = get_one(self.test_entity['name'])

        assert entity.name == self.test_entity['name']
        assert entity.number == self.test_entity['number']

    def test_delete_all(self) -> None:
        """ Delete all entities test """

        c = Client()
        json_response = c.get('/entity/delete_all').json()

        assert json_response['message'] == 'Deleted'

    def test_get_one(self) -> None:
        """ Get one entity test """

        self.__add()
        c = Client()
        json_response = c.get('/entity/' + self.test_entity['name']).json()

        self.assertIn('id', json_response)
        assert json_response['name'] == self.test_entity['name']
        assert json_response['number'] == self.test_entity['number']

    def test_get_one_fib_recursive(self) -> None:
        """ Get one entity with recursive fibonacci number test """

        self.__add()
        c = Client()
        json_response = c.get(
            '/entity/fib_recursive/' + self.test_entity['name']
        ).json()

        self.assertIn('id', json_response)
        assert json_response['name'] == self.test_entity['name']

        fibonacci_calc = async_to_sync(Calculation.fib)
        test_fib = fibonacci_calc(self.test_entity['number'], "iterative")
        assert json_response['fib_number'] == test_fib

    def test_get_one_fib_iterative(self) -> None:
        """ Get one entity with iterative fibonacci number """

        self.__add()
        c = Client()
        json_response = c.get(
            '/entity/fib_iterative/' + self.test_entity['name']
        ).json()

        self.assertIn('id', json_response)
        assert json_response['name'] == self.test_entity['name']

        fibonacci_calc = async_to_sync(Calculation.fib)
        test_fib = fibonacci_calc(self.test_entity['number'], "iterative")
        assert json_response['fib_number'] == test_fib

    def __add(self) -> None:
        """ Add entity """

        self.__delete()
        add_entity = async_to_sync(self.entity_service.add)
        add_entity({
            'name': self.test_entity['name'],
            'number': self.test_entity['number'],
        })

    def __delete(self) -> None:
        """ Delete all entities """

        delete_all = async_to_sync(self.entity_service.delete_all)
        delete_all()
