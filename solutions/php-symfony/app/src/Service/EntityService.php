<?php

namespace App\Service;

use App\Entity\Entity as EntityObject;
use App\Repository\EntityRepository;

/**
 * Entity service
 */
class EntityService
{
    /**
     * @var EntityRepository
     */
    private EntityRepository $repository;

    /**
     * @param EntityRepository $entityRepository
     */
    public function __construct(EntityRepository $entityRepository)
    {
        $this->repository = $entityRepository;
    }

    /**
     * Add entity
     *
     * @param array $data
     * @return int
     */
    public function add(array $data): int
    {
        $id = $this->repository->add($data);
        return  $id;
    }

    /**
     * Get one entity
     *
     * @param string $name
     * @return EntityObject
     */
    public function getOne(string $name): EntityObject
    {
        $entity = $this->repository->getOne($name);

        return $entity;
    }

    /**
     * Get one entity with fibonacci number
     *
     * @param string $name
     * @return EntityObject
     */
    public function getOneFib(string $name, string $mode): EntityObject
    {
        $entity = $this->getOne($name);

        $fib_number = CalculationService::fib($entity->getNumber(), $mode);
        $entity->setFibNumber($fib_number);

        return $entity;
    }

    /**
     * Delete all entities
     *
     * @return void
     */
    public function deleteAll(): void
    {
        $this->repository->deleteAll();
    }
}
