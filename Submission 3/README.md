# Submission 3

## IP3: Test Plan and Cases

### Instructions

There are multiple techniques for detecting errors in programs and in intermediate documentation: 

- *Testing*, which is the process of designing test cases, executing the program in a controlled environment, and verifying that the output is correct.
- Inspection and reviews, which can be applied to a program or to intermediate software artifacts. Inspections and reviews require the involvement of more than one person in addition to the original creator of the product and are very cost intensive. Reviews and inspections have been found to be most cost effective when applied to requirements specifications.

- *Formal methods*, which are mathematical techniques used to “prove” that a program is correct. These are rarely applied in business and commercial industries.

- *Static analysis*, which is the process of analyzing the static structure of a program or intermediate software product. This analysis is usually automated and can detect errors or error-prone conditions.

The focus of this project is on the Testing stage. Each student will create a test plan including test cases for the system they designed for the previous assignments. 

The student will indicate and explain the model to be used for the development of the system and the justification of why that model should be used for this type of development.  The test plan will be developed to be consistent with the process model. 

The plan must include an overview of the approach to testing including the project test philosophy. 

The plan must include needed Unit, Integration, System, and Acceptance test cases. The plan must assign responsibilities for each test. 

The student will develop example test cases for required tests.  The test cases must be consistent with the test plan approach and requirements. 

<br>
<br>

Students can use any form of documentation or any of the popular options for Test Management tools. Some options may include: 

- Enterprise Level:
    - [Gurock TestRail](https://www.gurock.com/testrail/test-management/)
- Free and Open Source
    - [TestLink](https://testlink.org/)
    - [Chef Inspec](https://docs.chef.io/inspec/)
    - [Selenium](https://www.selenium.dev/) 

**Bonus tools:** 
As the use of APIs in software development has skyrocketed in the past years, services that help develop, manage and test APIs for service providers or consumers can be very beneficial. Postman is an API platform that has two types of services: [Postman Enterprise](https://www.postman.com/api-network/) and [Postman free API testing](https://www.postman.com/api-network/). [Karate](https://github.com/karatelabs/karate) is an open-source framework that combines test automation, mocks, performance testing, and UI automation. 


#### Start Date
May 6, 2022 11:59 PM
#### Due Date
May 22, 2022 11:59 PM

<br>
<br>

### Research Links
https://www.guru99.com/test-driven-development.html
https://realpython.com/python-testing/

<br>
<br>

### Research Notes
>To have a complete set of manual tests, all you need to do is make a list of all the features your application has, the different types of input it can accept, and the expected results. Now, every time you make a change to your code, you need to go through every single item on that list and check it \([source]\)(https://realpython.com/python-testing/).

**Tic Tac Toe v2.0 Features:**

- [ ] create a gameboard
- [ ] display the updated gameboard at the end of each turn
- [ ] place marker on gameboard in specified positions

- [ ] players choose their marker (X or O)
- [ ] markers are assigned as player/opponent values

- [ ] first player is determined randomly 
- [ ] swap player switches **current_player** between X and O each turn

- [ ] check if there is a winner after each turn
    - [ ] win by row
    - [ ] win by column
    - [ ] win by diagonal
        - [ ] descending
        - [ ] ascending
- [ ] check if there is a draw after each turn

- [ ] AI code generates random, valid moves
- [ ] players input moves by entering 1-9 (referencing open squares)
- [ ] player move input must be translated to the grid coordinates of the gameboard

- [ ] game mode 1 - PvP
- [ ] game mode 2 - PvE (random AI)

- [ ] start up menu creation
- [ ] start up menu display
- [ ] ability to choose gamemode to initiate desired gameplay loop