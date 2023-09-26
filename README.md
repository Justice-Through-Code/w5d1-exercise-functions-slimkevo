# Tip Calculator

## W5D1 - Exercise - Tip Calculator

This coding assessment challenges you to create a *basic tip calculator* program.

### Estimated Time to Complete

45 minutes

---

## Exercise Overview

The user's input at the command line for:

* Cost of the food
* Number of people splitting the bill
* Percentage of the tip

Then, the script should output:
* The total bill (including tip and tax)
* The amount each person should pay (assume each person people will split the bill evenly)

**Note:** 
Your calculator should be able to handle a bill of any amount of many money, with any number of people splitting the bill, and with any tip percentage (including 0% tip)

## Cases your program should be able to handle:

#### A meal for 1

Inputs
* Food costs $15
* 1 person paying
* 20% tip

Expected output:
* `Total bill: $19.50`

#### A feast to remember

Inputs
* Food costs $25000000
* 3 people paying
* 31% tip

Expected output:
* `Total bill: $35,250,000.00`
* `Each person should pay $11,750,000.00`

#### No tip

Inputs
* Food costs $78.99
* 6 people paying
* 0 tip

Expected output:
* `Total bill: $86.89`
* `Each person should pay $14.48`

#### Sharing the bill among many

Inputs:
* Food costs $5000
* 876 people paying
* 12% tip

Expected output:
* `Total bill: $6,100.00`
* `Each person should pay $6.96`

## Getting Started

0. Accept the challenge via the GitHub Classroom link (if you're already here, you've done this part!)
1. Clone the repository to your computer.
2. Follow the instructions in `tip_calculator.py`.

## Unit Testing

In the `test_tip_calculator.py` file, you will find unittests for the functions you implemented. Make sure your functions pass these tests.

3. From the main folder of the challenge, run your computer's version of `python3 -m unittest` to see if your code works as expected.

REMEMBER: Comment out or delete the calls to your functions -- the test will not run with them!

## Git Local

4. Perform commands for `git add`, `git status`, `git commit`, `git push`.

## Git Remote

5. Access your GitHub Repository: Go to the GitHub website and log in to your account.
6. Navigate to the repository for this exercise.
7. Watch for the Red X (or yellow dot as the test runs) to change to the green check mark. The green check mark on a GitHub repository indicates that the commit or pull request has been tested and meets the defined criteria for correctness.
8. If there's a red "X" instead, it means the tests have failed. You'll need to investigate and fix the issues in VScode, then perform the `git add`, `git commit`, and `git push` steps again.


## Submit URL & Screenshot in Canvas

9. Navigate to the exercise in Canvas.
    A. Comment Section
        Submit a screenshot of your terminal showing the results of your unit test.
    B. URL submission Box
        GitHub remote repository exercise URL

## Grade in Canvas

10. The status in Canvas does not change to Complete until an Instructor has reviewed your assignment. This process is similar to the Code review process in a real work scenario. A code review by an instructor or a senior developer after unit tests pass is an important step in the software development process. It helps ensure that the code not only functions correctly but also adheres to best practices, coding standards, and maintainability guidelines.

Submit and then you are set!
