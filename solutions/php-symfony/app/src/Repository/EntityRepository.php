<?php

namespace App\Repository;

use Exception;
use App\Entity\Entity;
use Doctrine\Bundle\DoctrineBundle\Repository\ServiceEntityRepository;
use Doctrine\Persistence\ManagerRegistry;
use Symfony\Component\HttpKernel\Exception\NotFoundHttpException;

/**
 * Entity repository
 */
class EntityRepository extends ServiceEntityRepository
{
    /**
     * @param ManagerRegistry $registry
     */
    public function __construct(ManagerRegistry $registry)
    {
        parent::__construct($registry, Entity::class);
    }

    /**
     * Add entity
     *
     * @param array $data
     * @return mixed
     */
    public function add(array $data): mixed
    {
        $entity = new Entity();
        $entity->setName($data['name']);
        $entity->setNumber((int) $data['number']);

        $entityManager = $this->getEntityManager();
        $entityManager->persist($entity);
        $entityManager->flush();

        return $entity->getId();
    }

    /**
     * Get one entity
     *
     * @param string $name
     * @return Entity
     */
    public function getOne(string $name): Entity
    {
        $entity = $this->findOneBy([
            'name' => $name
        ]);

        if (!$entity) {
            throw new NotFoundHttpException('Entity not found');
        }

        return $entity;
    }

    /**
     * Delete all entities
     *
     * @return void
     */
    public function deleteAll(): void
    {
        $entityManager = $this->getEntityManager();

        $db = $entityManager->createQuery('
            DELETE FROM App\Entity\Entity
        ');

        $db->execute();
    }
}
