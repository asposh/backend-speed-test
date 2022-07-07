package com.bst.bstJavaSpring.bstMain.bstMainNode;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Bst fibonacci number node.
 */
public class BstMainNodeFibNumber {

    /**
     * fibNumber.
     */
    @JsonProperty("fib_number")
    private int fibNumber;

    /**
     * Creates new BstMainNodeFibNumber.
     *
     * @param fibNumber
     */
    public BstMainNodeFibNumber(int fibNumber) {
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
