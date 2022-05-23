<?php

namespace App\Tests\Controller;

use App\Service\CalculationService;
use App\Service\EntityService;
use App\Controller\IndexController;
use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;
use Symfony\Bundle\FrameworkBundle\KernelBrowser;

/**
 * Entity controller test
 */
class EntityControllerTest extends WebTestCase
{
    /**
     * @var string
     */
    private const TEST_NAME = 'test_name';

    /**
     * @var int
     */
    private const TEST_NUMBER = 10;

    /**
     * Entity index controller test
     *
     * @return void
     */
    public function testIndex(): void
    {
        $client = static::createClient();
        $request = $client->request('GET', '/entity');
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertEquals(['message' => 'Entity controller'], $response_array);
    }

    /**
     * Add entity test
     *
     * @return void
     */
    public function testAdd(): void
    {
        $client = static::createClient();

        // Delete old
        $this->delete();

        $data = [
            'name' => static::TEST_NAME,
            'number' => static::TEST_NUMBER,
        ];
        $request = $client->request('POST', '/entity/', $data);
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertArrayHasKey('id', $response_array);

        $service = $this->getServiceContainer();
        $entity = $service->getOne(static::TEST_NAME);

        $this->assertEquals(static::TEST_NAME, $entity->getName());
        $this->assertEquals(static::TEST_NUMBER, $entity->getNumber());
    }

    /**
     * Delete all entities test
     *
     * @return void
     */
    public function testDeleteAll(): void
    {
        $client = static::createClient();
        $request = $client->request('GET', '/entity/delete_all');
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertEquals(['message' => 'Deleted'], $response_array);
    }

    /**
     * Get one entity test
     *
     * @return void
     */
    public function testGetOne(): void
    {
        $client = static::createClient();

        // Add new
        $this->add();

        $request = $client->request('GET', '/entity/' . static::TEST_NAME);
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertArrayHasKey('id', $response_array);
        $this->assertEquals(static::TEST_NAME, $response_array['name']);
        $this->assertEquals(static::TEST_NUMBER, $response_array['number']);
    }

    /**
     * Get one entity with recursive fibonacci number test
     *
     * @return void
     */
    public function testGetOneFibRecursive(): void
    {
        $client = static::createClient();

        // Add new
        $this->add();

        $request = $client->request('GET', '/entity/fib_recursive/' . static::TEST_NAME);
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertArrayHasKey('id', $response_array);
        $this->assertEquals(static::TEST_NAME, $response_array['name']);
        $this->assertEquals(
            CalculationService::fib(static::TEST_NUMBER, "iterative"),
            $response_array['fib_number']
        );
    }

    /**
     * Get one entity with iterative fibonacci number test
     *
     * @return void
     */
    public function testGetOneFibIterative(): void
    {
        $client = static::createClient();

        // Add new
        $this->add();

        $request = $client->request('GET', '/entity/fib_iterative/' . static::TEST_NAME);
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertArrayHasKey('id', $response_array);
        $this->assertEquals(static::TEST_NAME, $response_array['name']);
        $this->assertEquals(
            CalculationService::fib(static::TEST_NUMBER, "iterative"),
            $response_array['fib_number']
        );
    }

    /**
     * Get service container
     *
     * @return null|object
     */
    private function getServiceContainer(): mixed
    {
        $container = static::getContainer();
        $service = $container->get(EntityService::class);
        return $service;
    }

    /**
     * Delete all entities
     *
     * @return void
     */
    private function delete(): void
    {
        $service = $this->getServiceContainer();
        $service->deleteAll();
    }

    /**
     * Add entity
     *
     * @return void
     */
    private function add(): void
    {
        $service = $this->getServiceContainer();
        $service->deleteAll();

        $data = [
            'name' => static::TEST_NAME,
            'number' => static::TEST_NUMBER,
        ];

        $service->add($data);
    }
}
