<?php

namespace App\Controller;

use App\Service\EntityService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\{
    Response,
    Request
};
use Symfony\Component\Routing\Annotation\Route;

/**
 * Entity controller
 */
class EntityController extends AbstractController
{
    /**
     * Entity add
     *
     * @param EntityService $service
     * @param Request $request
     * @return Response
     *
     * @Route("/entity/", methods={"POST"})
     */
    public function add(EntityService $service, Request $request): Response
    {
        $data = [
            'name' => $request->request->get('name'),
            'number' => $request->request->get('number'),
        ];

        $id = $service->add($data);

        return $this->json([
            'id' => $id,
        ]);
    }

    /**
     * Delete all entities
     *
     * @param EntityService $service
     * @return Response
     *
     * @Route("/entity/delete_all", methods={"GET"})
     */
    public function deleteAll(EntityService $service): Response
    {
        $service->deleteAll();

        return $this->json([
            'message' => 'Deleted'
        ]);
    }

    /**
     * Get one entity by name
     *
     * @param string $name
     * @param EntityService $service
     * @return Response
     *
     * @Route("/entity/{name}", methods={"GET"})
     */
    public function getOne(string $name, EntityService $service): Response
    {
        $entity = $service->getOne($name);

        return $this->json([
            'id' => $entity->getId(),
            'name' => $entity->getName(),
            'number' => $entity->getNumber(),
        ]);
    }

    /**
     * Get one entity with recursive fibonacci number
     *
     * @param string $name
     * @param EntityService $service
     * @return Response
     *
     * @Route("/entity/fib_recursive/{name}", methods={"GET"})
     */
    public function getOneFibRecursive(string $name, EntityService $service): Response
    {
        $entity = $service->getOneFib($name, 'recursive');

        return $this->json([
            'id' => $entity->getId(),
            'name' => $entity->getName(),
            'fib_number' => $entity->getFibNumber(),
        ]);
    }

    /**
     * Get one entity with iterative fibonacci number
     *
     * @param string $name
     * @param EntityService $service
     * @return Response
     *
     * @Route("/entity/fib_iterative/{name}", methods={"GET"})
     */
    public function getOneFibIterative(string $name, EntityService $service): Response
    {
        $entity = $service->getOneFib($name, 'iterative');

        return $this->json([
            'id' => $entity->getId(),
            'name' => $entity->getName(),
            'fib_number' => $entity->getFibNumber(),
        ]);
    }

    /**
     * Entity index
     *
     * @return Response
     *
     * @Route("/entity", methods={"GET"})
     */
    public function index(): Response
    {
        return $this->json([
            'message' => 'Entity controller'
        ]);
    }
}
