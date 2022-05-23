<?php

namespace App\Tests\Controller;

use App\Service\CalculationService;
use App\Controller\IndexController;
use Symfony\Bundle\FrameworkBundle\Test\WebTestCase;

/**
 * Main controller test
 */
class MainControllerTest extends WebTestCase
{
    /**
     * @var string
     */
    private const TEST_NUMBER = 10;

    /**
     * Index controller test
     *
     * @return void
     */
    public function testIndex(): void
    {
        $client = static::createClient();
        $request = $client->request('GET', '/');
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertEquals(
            'Default index',
            $response_array['message']
        );
    }

    /**
     * Cycle sum controller test
     *
     * @return void
     */
    public function testCycleSum(): void
    {
        $client = static::createClient();
        $data = [
            'number' => static::TEST_NUMBER,
        ];
        $request = $client->request('GET', '/cycle_sum', $data);
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertEquals(
            CalculationService::cycleSum(static::TEST_NUMBER),
            $response_array['cycle_sum']
        );
    }

    /**
     * Fibonacci controller test recursive
     *
     * @return void
     */
    public function testFibRterative(): void
    {
        $this->fibTestByMode('recursive');
    }

    /**
     * Fibonacci controller test iterative
     *
     * @return void
     */
    public function testFibIterative(): void
    {
        $this->fibTestByMode('iterative');
    }

    /**
     * Fibonacci test by mode
     *
     * @return void
     */
    private function fibTestByMode($mode): void
    {
        $client = static::createClient();
        $data = [
            'number' => static::TEST_NUMBER,
            'mode'   => $mode
        ];
        $request = $client->request('GET', '/fib', $data);
        $response_array = Helper::getResponceArray($client);

        $this->assertResponseIsSuccessful();
        $this->assertEquals(
            CalculationService::fib(static::TEST_NUMBER, "iterative"),
            $response_array['fib_number']
        );
    }
}
