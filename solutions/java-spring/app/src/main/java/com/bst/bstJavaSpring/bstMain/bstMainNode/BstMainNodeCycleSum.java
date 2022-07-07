package com.bst.bstJavaSpring.bstMain.bstMainNode;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * Bst fibonacci number node.
 */
public class BstMainNodeCycleSum {

    /**
     * cycleSum.
     */
    @JsonProperty("cycle_sum")
    private Long cycleSum;

    /**
     * Creates new BstMainNodeCycleSum.
     *
     * @param cycleSum
     */
    public BstMainNodeCycleSum(Long cycleSum) {
        this.cycleSum = cycleSum;
    }

    /**
     * Get fibonacci number.
     *
     * @return cycleSum
     */
    public Long getCycleSum() {
        return cycleSum;
    }
}
