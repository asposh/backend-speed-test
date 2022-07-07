package com.bst.bstJavaSpring.bstEntity.bstEntityNode;

/**
 * Bst entity node with name.
 */
public class BstEntityNodeName extends BstEntityNode {

    /**
     * name.
     */
    private String name;

    /**
     * Creates new BstEntityNodeName.
     *
     * @param id
     * @param name
     */
    public BstEntityNodeName(Long id, String name) {
        super(id);
        this.name = name;
    }

    /**
     * Get name.
     *
     * @return name
     */
    public String getName() {
        return name;
    }
}
