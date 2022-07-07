package com.bst.bstJavaSpring.bstEntity.bstEntityNode;

/**
 * Bst entity node get one.
 */
public class BstEntityNodeGetOne extends BstEntityNodeName {

    /**
     * number.
     */
    private int number;

    /**
     * Creates new BstEntityNodeGetOne.
     *
     * @param id
     * @param name
     * @param number
     */
    public BstEntityNodeGetOne(Long id, String name, int number) {
        super(id, name);
        this.number = number;
    }

    /**
     * Get BstEntityNodeGetOne number.
     *
     * @return number
     */
    public int getNumber() {
        return number;
    }
}
