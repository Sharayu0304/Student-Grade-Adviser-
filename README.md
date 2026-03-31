# Student-Grade-Adviser-
### An AI based Evaluation System

## Project Overview
A Python based command line application that takes marks as input from the users(students) , categorrises performances of each subject and then provides the user with suggestions and guideances along with assigning overall grade. Additionally,, it stores all records of previous performances in a CSV file.


Course : Fundamentals of AI and Ml
Course Code : CSA2001
Instituition : VIT Bhopal University 

## Features of this Project 
1. Project : A rule-based intelligent agent.
2. Takes marks as input from users/studeents for various subjects.
3. Suggests topicwise improvements that can be made by the  user.
4. Calculates an Overall Grade based on the average marks scored by the user.
5. Categorises performances - "At Risk", "Good", "Excellent"
6. Gives feedback according to how the user performs.
7. Previous records are stored in  CSV file.


## About THe Project
It is python based command line project that helps users(students/others) to assess their study perdormance. It collects  subject-wise marks from the user  and caluclates its mean score, a grade and calculates the final grade. The apllication also provides with a feedback based on the final grade and also provides with topic-wise improvement suggestions to improve their weak areas. In addition to these, it also keeps a csv file which keeps a record of all the past data, allowing users to track their progress over time. This project shows the practical use of python and AI based concepts.

## Project Structure
Student-Grade-Adviser/

|----gradeadviser.py -----> main python program, (run this on terminal)
|----history.csv------>  it is automatically created after running the python file
|-----README.md-----> Project explanation


## Concepts applied (AI BASED)
+ This project uses intelligent agent, which perceives marks of the user as input , uses reasoning based rules and actos on the environment by proving the user with a PERFORMANCE REPORT.

+ PERFORMANCE MEASURE : the score_mean is used to calculate the users final grade. 

+ This project works on the cocnept of RULE-BASED-REASONING. It classifies each subject into categories such as - At Risk, Average, Good, Excellent using If-Else Conditional Statements.

+ PEAS REPRESENTATION : 
1. Performance = Clear and Readable Evaluation Report, accuracy in calculation of mean score
2. Environment = Terminal, data stored in CSV File
3. Sensors = Student, Subjectwise marks
4.  Actuators = Performance report on terminal, transfers all records of data into history.csv

## How it works 
**Choice 1 — Check my performance**

Asks for your and marks subject-wise.
+ Categorises each subject int -  At Risk, Average, Good, or Excellent
+ Show subject-wise topic suggestions on where the user should focus on.
+ Calculates the mean score and provides with a final grade.
+ Gives suggestions and guidances on where the user can improve
+ Results get recorded into history.csv.

**Choice 2 — View previous results**

Shows all previous records directly into the terminal imported from hostroy.csv

**Choice 3 — Quit** 
Stops and quits the programs



## How to set up
1. Make sure you have Python 3 installed in your PC.
2. Clone the repository : git clone < repository link>
3. write : cd student-grade-advisor
4. Python modules like csv, os and datetime are already imported so no external libraries are required.


## How to use it/ How to run 
+ Clone the repository : git clone < repository link>
+ write : cd student-grade-advisor
+ Open your terminal and go to the gradeadviser.py python file. 
+ Run the program.

## Terminal (Screenshot)
[terminal1](<terminal 1 upper.png>)
![terminal2](<terminal 2 .png>)
![terminal3](<terminal 3 .png>)

## Author
+ Name : Sharayu Sunil
+ Branch : Computer Science Engineering (Artifical Intelligence and Machine Learning)
