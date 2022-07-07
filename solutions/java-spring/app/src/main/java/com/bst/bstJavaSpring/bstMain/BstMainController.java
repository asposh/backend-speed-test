package com.bst.bstJavaSpring.bstMain;

import com.bst.bstJavaSpring.bstMain.bstMainNode.BstMainNodeCycleSum;
import com.bst.bstJavaSpring.bstMain.bstMainNode.BstMainNodeFibNumber;
import com.bst.bstJavaSpring.bstMain.bstMainNode.BstMainNodeMessage;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Bst main controller.
 */
@RestController
public class BstMainController {

    /**
     * Index controller.
     *
     * @return message
     */
    @GetMapping(path = "/", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public BstMainNodeMessage index() {
        BstMainNodeMessage message = new BstMainNodeMessage("Default index");
        return message;
    }

    /**
     * Fibonacci controller.
     *
     * @param number
     * @param mode
     * @return resultNumber
     */
    @GetMapping(path = "/fib", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public BstMainNodeFibNumber fib(
        @RequestParam(value = "number") int number,
        @RequestParam(value = "mode") String mode
    ) {
        int fibNumber = BstCalculationService.fib(number, mode);
        BstMainNodeFibNumber resultNumber = new BstMainNodeFibNumber(fibNumber);
        return resultNumber;
    }

    /**
     * Cycle sum controller.
     *
     * @param number
     * @return resultSum
     */
    @GetMapping(path = "/cycle_sum", produces = MediaType.APPLICATION_JSON_VALUE)
    @ResponseBody
    public BstMainNodeCycleSum cycleSum(@RequestParam(value = "number") int number) {
        Long sum = BstCalculationService.cycleSum(number);
        BstMainNodeCycleSum resultSum = new BstMainNodeCycleSum(sum);
        return resultSum;
    }
}
