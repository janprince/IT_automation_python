## Black Box vs. White Box Testing

### White-box testing
White-box testing also sometimes called clear-box or transparent testing relies on the test creators knowledge of the 
software being tested to construct the test cases. With a white-box test, the test creator knows how the 
code works and can write test cases that use the understanding to make sure that everything is performing
the way it's expected to.

### Black-box testing
On the other hand, in black-box testing, the software being tested is treated like an opaque box. 
In other words, the tester doesn't know the internals of how the software works. Black-box tests are written with an 
awareness of what the program is supposed to do, its requirements or specifications, but not how it does 
it.

f the unit tests are created before any code is written based on specifications of what the code is supposed to do, 
they can be considered **black-box unit test**. 

If unit tests are run alongside or after the code has been developed, the test cases are made with a knowledge of 
how software works. They are **white-box tests**. 

One way isn't strictly better than the other since each gives you a different path to make your code more reliable. 
Not everything is so black and white or as we'd say in the coding world, binary. 
As an IT specialist, you may need to test that software written by others behaves the way you expect it to. 
To do this, you can use the combination of black-box and white-box test.

### Other types of tests
1. Integration tests
2. Regression tests
3. Load tests
4. Smoke tests (Build verification tests)

keyword: Test Suite


## Test-Driven Development (TDD)
A process called test-driven development or TDD calls for creating the test before writing the code. This might seem a bit counter-intuitive, but it can make for more thoughtful well-written programs. 

he test-driven development cycle typically involves first writing a test then running it to make sure it fails. After all, you haven't written the code to make it passed yet. Once you've verified it fails, you write the code that will satisfy the test then run the tests again. If it passes you can continue on to the next part of your program. If it fails you Debug and run the test again. The cycle is repeated for each new feature of your script until it's up and running.

Remember that good tests help make any automation and script you write more robust, resilient, and less buggy. Having reliable automation makes life better for everyone. Many companies take testing a step further and combine it with our version control systems and development processes. When engineers submit their code, it's integrated into the main repository and tests are automatically run against it to spot bugs and errors in a process called Continuous Integration. Although useful, setting up a continuous integration process can be a big undertaking.