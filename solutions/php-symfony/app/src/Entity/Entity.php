<?php

namespace App\Entity;

use App\Repository\EntityRepository;
use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity(repositoryClass=EntityRepository::class)
 */
class Entity
{
    /**
     * @var int
     *
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     */
    private int $id;

    /**
     * @var string
     *
     * @ORM\Column(type="string", length=255, unique=true)
     */
    private string $name;

    /**
     * @var int
     *
     * @ORM\Column(type="integer")
     */
    private int $number;

    /**
     * @var int
     */
    private int $fib_number;

    /**
     * Get entity id
     *
     * @return int
     */
    public function getId(): ?int
    {
        return $this->id;
    }

    /**
     * Get entity name
     *
     * @return string
     */
    public function getName(): ?string
    {
        return $this->name;
    }

    /**
     * Set entity name
     *
     * @param string $name
     * @return Entity
     */
    public function setName(string $name): self
    {
        $this->name = $name;

        return $this;
    }

    /**
     * Get entity number
     *
     * @return int
     */
    public function getNumber(): ?int
    {
        return $this->number;
    }

    /**
     * Set entity number
     *
     * @param int $number
     * @return Entity
     */
    public function setNumber(int $number): self
    {
        $this->number = $number;

        return $this;
    }

    /**
     * Get entity fibonacci number
     *
     * @return int
     */
    public function getFibNumber(): ?int
    {
        return $this->fib_number;
    }

    /**
     * Set entity fibonacci number
     *
     * @param int $number
     * @return Entity
     */
    public function setFibNumber(int $number): self
    {
        $this->fib_number = $number;

        return $this;
    }
}
