package com.bst.bstJavaSpring.bstEntity;

import org.springframework.data.repository.CrudRepository;

/**
 * Bst entity repository.
 */
public interface BstEntityRepository extends CrudRepository<BstEntity, Long> {

    /**
     * Get one Bst entity.
     *
     * @param name
     * @return bstEntity
     */
    BstEntity findByName(String name);
}
