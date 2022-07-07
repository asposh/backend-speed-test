package com.bst.bstJavaSpring;

import com.bst.bstJavaSpring.bstEntity.BstEntity;
import com.bst.bstJavaSpring.bstEntity.BstEntityService;
import com.bst.bstJavaSpring.bstMain.BstCalculationService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.util.Assert;
import org.springframework.util.MultiValueMap;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.test.web.reactive.server.WebTestClient;
import org.springframework.web.reactive.function.BodyInserters;

/**
 * Bst Entity Tests.
 */
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class BstEntityTests {

    /**
     * Test number.
     */
    private static int testNumber = 7;

    /**
     * Test name.
     */
    private static String testName = "test_name";

    /**
     * Autowired bstEntityService.
     */
    @Autowired
    private BstEntityService bstEntityService;

    /**
     * Autowired webClient.
     */
    @Autowired
    private WebTestClient webClient;

    /**
     * Entity index test.
     */
    @Test
    public void indexTest() throws Exception {
        webClient.get().uri("/entity")
            .exchange()
            .expectHeader().valueEquals("Content-Type", "application/json")
            .expectStatus().isOk()
            .expectBody().jsonPath("message").isEqualTo("Entity controller");
    }

    /**
     * Add entity test.
     */
    @Test
    public void addTest() throws Exception {
        MultiValueMap<String, String> bodyValues = new LinkedMultiValueMap<>();
        bodyValues.add("name", testName);
        bodyValues.add("number", String.valueOf(testNumber));

        webClient.post().uri("/entity")
            .body(BodyInserters.fromFormData(bodyValues))
            .exchange()
            .expectHeader().valueEquals("Content-Type", "application/json")
            .expectStatus().isOk()
            .expectBody().jsonPath("id").isNotEmpty();

        BstEntity bstEntity = bstEntityService.getOne(testName);
        Assert.isTrue(bstEntity.getName().equals(testName));
        Assert.isTrue(bstEntity.getNumber() == testNumber);

        delete();
    }

    /**
     * Get one entity test.
     */
    @Test
    public void getOneTest() throws Exception {
        add();
        webClient.get().uri(
                builder -> builder.path("/entity/{testName}")
                    .build(testName)
            )
            .exchange()
            .expectHeader().valueEquals("Content-Type", "application/json")
            .expectStatus().isOk()
            .expectBody()
                .jsonPath("name").isEqualTo(testName)
                .jsonPath("number").isEqualTo(testNumber);

        delete();
    }

    /**
     * Get one entity with iterative fibonacci number test.
     */
    @Test
    private void fibIterativeEntityTest() throws Exception {
        fibEntityTest("iterative");
    }

    /**
     * Get one entity with recursive fibonacci number test.
     */
    @Test
    private void fibRecursiveEntityTest() throws Exception {
        fibEntityTest("recursive");
    }

    /**
     * Get fibonacci number by mode.
     *
     * @param mode
     */
    private void fibEntityTest(String mode) throws Exception {
        add();
        webClient.get().uri(
                builder -> builder.path("/fib_" + mode + "/{testName}")
                    .build(testName)
            )
            .exchange()
            .expectHeader().valueEquals("Content-Type", "application/json")
            .expectStatus().isOk()
            .expectBody()
                .jsonPath("name").isEqualTo(testName)
                .jsonPath("fib_number").isEqualTo(String.valueOf(BstCalculationService.fib(testNumber, "iterative")));

        delete();
    }

    /**
     * Add entity.
     */
    private void add() {
        delete();
        BstEntity bstEntity = new BstEntity(testName, testNumber);
        bstEntity = bstEntityService.add(bstEntity);
    }

    /**
     * Delete all entities.
     */
    private void delete() {
        bstEntityService.deleteAll();
    }
}
