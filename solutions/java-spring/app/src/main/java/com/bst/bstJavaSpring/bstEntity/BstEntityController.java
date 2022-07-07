package com.bst.bstJavaSpring.bstEntity;

import com.bst.bstJavaSpring.bstEntity.bstEntityNode.BstEntityNode;
import com.bst.bstJavaSpring.bstEntity.bstEntityNode.BstEntityNodeGetOne;
import com.bst.bstJavaSpring.bstEntity.bstEntityNode.BstEntityNodeGetOneFib;
import com.bst.bstJavaSpring.bstMain.bstMainNode.BstMainNodeMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;


/**
 * Bst entity controller.
 */
@RestController
public class BstEntityController {

    /**
     * Autowired bstEntityService.
     */
    @Autowired
    private BstEntityService bstEntityService;

    /**
     * Delete all Bst entities controller.
     *
     * @return message
     */
    @GetMapping(path = "/entity/delete_all", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public BstMainNodeMessage deleteAll() {
        bstEntityService.deleteAll();
        BstMainNodeMessage message = new BstMainNodeMessage("Deleted");
        return message;
    }

    /**
     * Get one Bst entity with fibonacci recursive controller.
     *
     * @param name
     * @return node
     */
    @GetMapping(path = "/entity/fib_recursive/{name}", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public BstEntityNodeGetOneFib getOneFibRecursive(@PathVariable(value = "name") String name) {
        BstEntity bstEntity = bstEntityService.getOneFib(name, "recursive");
        BstEntityNodeGetOneFib node = new BstEntityNodeGetOneFib(
            bstEntity.getId(),
            bstEntity.getName(),
            bstEntity.getFibNumber()
        );
        return node;
    }

    /**
     * Get one Bst entity with fibonacci iterative controller.
     *
     * @param name
     * @return node
     */
    @GetMapping(path = "/entity/fib_iterative/{name}", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public BstEntityNodeGetOneFib getOneFibIterative(@PathVariable(value = "name") String name) {
        BstEntity bstEntity = bstEntityService.getOneFib(name, "iterative");
        BstEntityNodeGetOneFib node = new BstEntityNodeGetOneFib(
            bstEntity.getId(),
            bstEntity.getName(),
            bstEntity.getFibNumber()
        );
        return node;
    }

    /**
     * Get one Bst entity controller.
     *
     * @param name
     * @return node
     */
    @GetMapping(path = "/entity/{name}", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public BstEntityNodeGetOne getOne(@PathVariable(value = "name") String name) {
        BstEntity bstEntity = bstEntityService.getOne(name);
        BstEntityNodeGetOne node = new BstEntityNodeGetOne(
            bstEntity.getId(),
            bstEntity.getName(),
            bstEntity.getNumber()
        );
        return node;
    }

    /**
     * Add Bst entity controller.
     *
     * @param bstEntity
     * @return node
     */
    @PostMapping(
        path = "/entity",
        produces = MediaType.APPLICATION_JSON_VALUE
    )
    @ResponseBody
    public BstEntityNode add(BstEntity bstEntity) {
        bstEntity = bstEntityService.add(bstEntity);
        BstEntityNode node = new BstEntityNode(bstEntity.getId());
        return node;
    }

    /**
     * Entity index controller.
     *
     * @return message
     */
    @GetMapping(path = "/entity", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public BstMainNodeMessage index() {
        BstMainNodeMessage message = new BstMainNodeMessage("Entity controller");
        return message;
    }
}
