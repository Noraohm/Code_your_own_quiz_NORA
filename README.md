# Code_your_own_quiz_NORA
Project of intro to programming (Udacity). Code your own quiz


**project overview**

For this project we built a fill-in-the-blanks quiz. The quiz will prompt a user with a sentence containing several blanks.
The user should fill in each blank appropriately to complete the sentence.
_**(text from Udacity Project page)**_


## Prerequisites
To run the code you need below:
1) Python 2 or 3 version from [click here](https://www.python.org/downloads/).
2) Google & github to search if you stuck in any steps [click here](https://github.com/).


## Installing:

follow the instruction in the download page for installing the programs.

### Steps:

1) Download and install (Python).

2) To start writing this question. Think about the Idea, organize it then start to code.
For this you need to decide first the vocabulary you want to use. The code will be flexible and reply to the user input so you should use if statement to give a “correct” for the correct guessing and “false , try again” with false answers.
The game as rubric instructor the game has to have 3 levels (easy ,medium , hard). Give the user attempt to try again at least 3 times .
3) Assign the sentence (wisdom in my app) into a variable both sentence & answers to use it later to compare if the input write or not.


## For coding::


1)	There has to be welcome page (first page). Put instruction there for the user & display the question so the user can choose what level he wants to play. 
Use raw_input method “This method will display and give a chance to the user to type his selection”

```
Welcome_page = raw_input('challenge yourself and select a level (For \ easy press 1 ,medium press 2 , hard press 3): '.title())  
    
if Welcome_page == '1':

   print Blank_Question(easy_Answers, Easy_Level)

```

2)	In my code I gave the chance to the user to select how many attempts he need to fill the blank correctly.

 ```
attempts = raw_input('Challenge yourself and add the attempt you need to fill overall the 4 blanks: ')
```

3)	Once the user solved it, the full result has to come on the screen then close the game or retry it. 



## Authors
Nora Almotairy
