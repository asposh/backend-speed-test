<?php

namespace App\Controller;

use App\Service\CalculationService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\{
    Response,
    Request
};
use Symfony\Component\Routing\Annotation\Route;

/**
 * Main controller
 */
class MainController extends AbstractController
{
    /**
     * Index controller
     *
     * @return Response
     *
     * @Route("/", methods={"GET"})
     */
    public function index(): Response
    {
        return $this->json([
            'message' => 'Default index'
        ]);
    }

    /**
     * Fibonacci controller
     *
     * @param Request $request
     * @return Response
     *
     * @Route("/fib", methods={"GET"})
     */
    public function fib(Request $request): Response
    {
        $data = [
            'number' => (int) $request->query->get('number'),
            'mode'   => (string) $request->query->get('mode'),
        ];

        $fib_number = CalculationService::fib($data['number'], $data['mode']);

        return $this->json([
            'fib_number' => $fib_number
        ]);
    }

    /**
     * Cycle sum controller
     *
     * @param Request $request
     * @return Response
     *
     * @Route("/cycle_sum", methods={"GET"})
     */
    public function cycleSum(Request $request): Response
    {
        $number = (int) $request->query->get('number');

        $sum = CalculationService::cycleSum($number);

        return $this->json([
            'cycle_sum' => $sum
        ]);
    }
}
