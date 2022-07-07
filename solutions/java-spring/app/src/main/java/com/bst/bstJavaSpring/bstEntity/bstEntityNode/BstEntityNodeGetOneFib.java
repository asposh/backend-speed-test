package com.bst.bstJavaSpring.bstEntity.bstEntityNode;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Bst entity get one with fibonacci number node.
 */
public class BstEntityNodeGetOneFib extends BstEntityNodeName {

    /**
     * fibNumber.
     */
    @JsonProperty("fib_number")
    private int fibNumber;

    /**
     * Creates new BstEntityNodeGetOneFib.
     *
     * @param id
     * @param name
     * @param fibNumber
     */
    public BstEntityNodeGetOneFib(Long id, String name, int fibNumber) {
        super(id, name);
        this.fibNumber = fibNumber;
    }

    /**
     * Get BstEntityNodeGetOneFib fibNumber.
     *
     * @return fibNumber
     */
    public int getFibNumber() {
        return fibNumber;
    }
}
