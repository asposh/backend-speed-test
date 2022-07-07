package com.bst.bstJavaSpring;

import com.bst.bstJavaSpring.bstMain.BstCalculationService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.test.web.reactive.server.WebTestClient;

/**
 * Bst Main Tests.
 */
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class BstMainTests {

    /**
     * Number.
     */
    private static int testNumber = 10;

    /**
     * webClient.
     */
    @Autowired
    private WebTestClient webClient;

    /**
     * Index test.
     */
    @Test
    public void indexTest() throws Exception {
        webClient.get().uri("/")
            .exchange()
            .expectHeader().valueEquals("Content-Type", "application/json")
            .expectStatus().isOk()
            .expectBody().jsonPath("message").isEqualTo("Default index");
    }

    /**
     * Cycle sum test.
     */
    @Test
    public void cycleSumTest() throws Exception {
        webClient.get().uri(
                builder -> builder.path("/cycle_sum")
                    .queryParam("number", testNumber)
                    .build()
            )
            .exchange()
            .expectHeader().valueEquals("Content-Type", "application/json")
            .expectStatus().isOk()
            .expectBody().jsonPath("cycle_sum").isEqualTo(String.valueOf(BstCalculationService.cycleSum(testNumber)));
    }

    /**
     * Fibonacci recursive test.
     */
    @Test
    public void fibRecursiveTest() throws Exception {
        fibModeTest(testNumber, "recursive");
    }

    /**
     * Fibonacci iterative test.
     */
    @Test
    public void fibIterativeTest() throws Exception {
        fibModeTest(testNumber, "iterative");
    }

    /**
     * Fibonacci test by mode.
     *
     * @param number
     * @param mode
     */
    private void fibModeTest(int number, String mode) throws Exception {
        webClient.get().uri(
                builder -> builder.path("/fib")
                    .queryParam("number", number)
                    .queryParam("mode", mode)
                    .build()
            )
            .exchange()
            .expectHeader().valueEquals("Content-Type", "application/json")
            .expectStatus().isOk()
            .expectBody().jsonPath("fib_number").isEqualTo(String.valueOf(BstCalculationService.fib(number, mode)));
    }
}
