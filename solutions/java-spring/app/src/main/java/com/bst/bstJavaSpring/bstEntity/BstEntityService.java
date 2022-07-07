package com.bst.bstJavaSpring.bstEntity;

import com.bst.bstJavaSpring.bstMain.BstCalculationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

/**
 * Bst entity service.
 */
@Component
public class BstEntityService {

    /**
     * Autowired BstEntityRepository.
     */
    @Autowired
    private BstEntityRepository bstEntityRepository;

    /**
     * Add Bst entity.
     *
     * @param entity
     * @return entity
     */
    public BstEntity add(BstEntity entity) {
        entity = bstEntityRepository.save(entity);
        return entity;
    }

    /**
     * Get one Bst entity.
     *
     * @param name
     * @return entity
     */
    public BstEntity getOne(String name) {
        BstEntity entity = bstEntityRepository.findByName(name);
        return entity;
    }

    /**
     * Get one Bst entity with fibonacci number.
     *
     * @param name
     * @param mode
     * @return entity
     */
    public BstEntity getOneFib(String name, String mode) {
        BstEntity entity = getOne(name);
        int fibNumber = BstCalculationService.fib(entity.getNumber(), mode);
        entity.setFibNumber(fibNumber);
        return entity;
    }

    /**
     * Get all entities.
     */
    public void deleteAll() {
        bstEntityRepository.deleteAll();
    }
}
