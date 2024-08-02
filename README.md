# README 

## Overall File Structure
- analysis: Contains all the files used within this study for the statistical analysis of the dataset. This includes making dataframes for statistical analysis, data cleaning; generally organizing the data into formats that are useful for analysis. There is python code, R code, and external files.
- open_coding: Contains the resources used for the open coding done in this study. There are spreadsheets containing the actual dataset and decisions, in addition to the python code used to create it.
- pr_interface: Contains screenshots of each pull request from an example repository that is exactly the same as the students saw. The screenshots show the overall PR view in addition to the diff view that each student would see if this was there repository.
- processing: Contains the code and files used for processing student responses and turning them into initial dataset. These files use the Github API and the PyGithub library in python to process the results. 
- questionaire: Contains the questions and answers to the post-study that participants answered.
- tasks: Contains all the tasks used in the the study in both their nonequivalent and equivalent form.

## Notes:
- GitHub API is used through the PyGithub Library
- mysql.connector is used as a convenient way to store and access data
- Any code that is in R has been modified and may have been used for multiple purposes.

### analysis
- code: contains the python code
    - add_order_remove_D.py: adds order to the dataframe and removes Task D
    - anon_study.py: anonimizes the post-study responses
    - B_accuacy.py: creates a csv file that only contains Task B out of all partcipant responses
    - characteristics.py: creates a csv file that compiles partcipant characteristics along with their average accuracy to analyze.
    - dataframe.py: The major python file used to create the dataframe for statistics analysis
    - gen_ai.py: Inserts generative AI data from post study into MySQL
    - open.py: gets all the usernames and all the links to the open pull requests
    - order.py: Retrieves the order in which partcipants saw the tasks and writes it out
    - sections.py: seperates the tasks by class sections and outputs them into csvs
- files:
    - blocks.csv: displays the blocks that were assigned to students
    - order.txt: displays the anon usernames and the order in which they saw the tasks. Ex: ncsu-1, 3,4,5,6,8
    username = ncsu-1, saw Task A 3rd, Task B 4th, etc...
- manual_verf:
    - Atrust.csv: files used to manually verify the tasks that were not fully trusted.
    - etc....
- R_code:
    - B_accuracy.R: checks if education affects the accuracy of Task B
    - characeristics.R: reads in the characertistics dataframe
    - person_model.R: Runs the linear model checking for Modality significance.
    - problem_model.R: Runs the linear model with contrasts as well as checking the values of trusted and untrusted tasks
    - prop_test.R: tests whether the proportions of the barriers removed from this study to previous study
    - sections.R: Tests whether the accuracy of the two sections are different

### open_coding
- Card Sorting.xlsx: the excel spreadsheet that contains the open_coding decisions
   - Master: the master dataset
   - easy_1: Card sorting by the first sorter for question 3c
   - difficult_1: Card sorting by the first sorter for question 3b
   - easy_2: Card sorting by the second sorter for question 3c
   - difficult_2: Card sorting by the second sorter for question 3b
   - easy_combined: combined agreed card sorting on question 3c
   - difficult_combined: combined agreed card sorting on question 3b
   - Easy_pivot: Pivot table for categories in question 3c
   - Difficult_pivot: Pivot table for categories in question 3b
   - Sig: Sheet showing the percentages of barriers showing up in this work versus previous work.
- card_sort.csv: the master card sorting dataset
- making_cards.py: Code to make the cards and match them to the anonimzied username

### pr_interface
- PR1: the first pull request in this example repository
   - PR1_diff.png: picture of the diff in the example repository
- PR2: the second pull request in this example repository
    - PR2_diff.png: picture of the diff in the example repository
- etc...

### processing
- anon.py: anonimizes the username
- patterns_users.py: Inserts the block and the username into the MySQL database used for storage
- processing.py: Through Github API calls, iterated through all survey responses and stored them within a MySQL database. Checked all PR for each partcipant, checking for merge, comments, requesting changes, approving changes, etc... The bulk of all processing work to form the datasets for this study was this file.
- rate.py: Check the rate limit for the GitHub API
- test.py: Proof of Concept that the Github API and PyGithub could be used to retrieve the information we wanted, precursor to processing.py


### questionaire
- post_study_answers.csv: contains the questions, answers and anonimzed IDs to the post study
- post-study.txt: contains the questions to the post study


### tasks
- A: Task A for the study
    - Eq: Equivalent Pair
        - newV.java: updated version of code, code being merged from the PR
        - oldV.java: original version of the code
    - Neq: NonEquivalent Pair
        - newV.java: updated version of code, code being merged from the PR
        - oldV.java: original version of the code
- B: Task B for the study
    - Eq: Equivalent Pair
        - newV.java: updated version of code, code being merged from the PR
        - oldV.java: original version of the code
    - Neq: NonEquivalent Pair
        - newV.java: updated version of code, code being merged from the PR
        - oldV.java: original version of the code
- etc....

