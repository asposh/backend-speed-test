package com.bst.bstJavaSpring.bstEntity;

import javax.persistence.Id;
import javax.persistence.Index;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Table;
import javax.persistence.Transient;


/**
 * Bst entity.
 */
@Entity
@Table(indexes = @Index(columnList = "name"))
public class BstEntity {

    /**
     * id.
     */
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    /**
     * name.
     */
    @Column(unique = true, length = 255)
    private String name;

    /**
     * number.
     */
    private int number;

    /**
     * fibNumber.
     */
    @Transient
    private int fibNumber;

    /**
     * Default constructor.
     */
    public BstEntity() {

    }

    /**
     * Creates new Bst entity.
     *
     * @param name
     * @param number
     */
    public BstEntity(String name, int number) {
        this.name = name;
        this.number = number;
    }

    /**
     * Returns entity id.
     *
     * @return id
     */
    public Long getId() {
        return id;
    }

    /**
     * Get name.
     *
     * @return name
     */
    public String getName() {
        return name;
    }

    /**
     * Set name.
     *
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Get number.
     *
     * @return number
     */
    public int getNumber() {
        return number;
    }

    /**
     * Set number.
     *
     * @param number
     */
    public void setNumber(int number) {
        this.number = number;
    }

    /**
     * Set fibonacci number.
     *
     * @param fibNumber
     */
    public void setFibNumber(int fibNumber) {
        this.fibNumber = fibNumber;
    }

    /**
     * Get fibonacci number.
     *
     * @return fibNumber
     */
    public int getFibNumber() {
        return fibNumber;
    }
}
