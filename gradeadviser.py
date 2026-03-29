#STUDENT GRADE ADVISER 
#DESCRIPTION : 

import csv
import os
from datetime import datetime

courses = [
    "Maths",
    "Artificial Intelligence and Machine Learning",
    "Python Programming",
    "Computational Physics",
    "Advanced Technical Communication",
]

topicwise_improvements = {
    "Maths": {
        "At Risk":   "Revise: Double Integration, Vector Calculus, Integration Formulae",
        "Average":   "Revise: Permuations and Combinations, Probability, 3D Geometry",
        "Good":      "Revise: Transform Techniques, Diescrete mathematics",
        "Excellent": "Explore: Binomial Theorem, Differentiation",
    },
    "Artificial Intelligence and Machine Learning": {
        "At Risk":   "Revise: What is AI, Types of Agents, Basic Definitions",
        "Average":   "Revise: Search Strategies, BFS, DFS, Problem Solving",
        "Good":      "Revise: Informed Search, Heuristics, Knowledge Representation",
        "Excellent": "Explore: Machine Learning Models, Neural Networks"
    },
    "Python Programming": {
        "At Risk":   "Revise: Variables, Data Types, Basic Input/Output",
        "Average":   "Revise: Loops, Conditionals, Functions",
        "Good":      "Revise: Lists, Dictionaries, File Handling",
        "Excellent": "Explore: OOP, Algorithms, Data Structures"
    },
    "Computational Physics": {
        "At Risk":   "Revise: Basic Units, Motion, Force",
        "Average":   "Revise: Laws of Motion, Energy, Work",
        "Good":      "Revise: Waves, Optics, Electricity",
        "Excellent": "Explore: Quantum Basics, Electromagnetism"
    },
    "Advanced Technical Communication": {
        "At Risk":   "Revise: Grammar Rules, Sentence Formation",
        "Average":   "Revise: Comprehension, Essay Writing",
        "Good":      "Revise: Technical Writing, Vocabulary",
        "Excellent": "Explore: Advanced Writing, Presentation Skills"
    }
}

def efficiency(score):
    if score < 40:
        return "At Risk"
    elif score < 50:
        return "Average"
    elif score < 70:
        return "Good"
    else:
        return "Excellent"
    
def grade_final(score_mean):
  
    if score_mean < 40:
        return "F grade — Fail"
    elif score_mean < 50:
        return "D grade — You must improve."
    elif score_mean < 60:
        return "C grade — Average, could do better."
    elif score_mean < 75:
        return "B grade — Good"
    elif score_mean < 90:
        return "A grade — Excellent"
    else:
        return "A+ grade — Outstanding"
    
def guidances(score_mean, weak_courses):
  
    if score_mean < 40:
        return " You are struggling to score. Please reach out to your professor for further advice."
    elif score_mean < 60:
        if weak_courses:
            return f" These subjects should be your priority. Give immediate attention to: {', '.join(weak_courses)}. Practice daily to maintain consistency and that should help."
        return " You are almost there... Keep Fighting!"
    elif score_mean < 80:
        if weak_courses:
            return f" Nice work! Focus on: {', '.join(weak_courses)} .Revising there topics will boost up your performance."
        return " You are doing great! keep pushing yourself further."
    else:
        return "Impressive! You can challenge yourself with advanced topics next."
    
    
def marks(subject):
  
    while True:
        try:
            score = float(input(f"Please enter your marks for {subject} (Range: 0 to 100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid. You must enter a number between 0-100.")
        except ValueError:
            print(" Invalid input. You must enter a number.")


def imput_name_of_student():
    while True:
        StudentName = input("Please enter your Name: ").strip()
        if StudentName:
            return StudentName
        print("Name cannot be left blank. Please try again.")



def display_report(StudentName, marks_list, avg_marks, finalgrade, feedback):
    print("\n" + "=" * 55)
    print(f"EVALUATION REPORT — {StudentName.upper()}")
    print(f"DATE:{datetime.now().strftime('%d %B %Y, %I:%M %p')}")
    print("=" * 55)

    print(f"\n{'Subject':<45} {'Marks':>6}  {'Level':<12}  Suggestion")
    print("-" * 110)

    for subject, score, level in marks_list:
        advice = topicwise_improvements[subject][level]
        print(f"{subject:<45} {score:>6.1f}  {level:<12}  {advice}")

    print("-" * 110)

    print("-" * 75)
    print(f"\n Average Score : {avg_marks:.1f} / 100")
    print(f"Overall Grade : {finalgrade}")
    print(f"\n Advisor Says  : {feedback}")
    print("=" * 55)
    
csvfile = "details.csv"

def save_to_csv(StudentName, marks_list, avg_marks, finalgrade):
    csvfile_available = os.path.isfile(csvfile)

    with open(csvfile, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not csvfile_available:
            header = ["Student Name", "Date"] + courses + ["Mean", "Final Grade"]
            writer.writerow(header)

        date = datetime.now().strftime("%d-%m-%Y %H:%M")
        score_subjectwise = [score for _, score, _ in marks_list]
        row = [date, StudentName] + score_subjectwise + [f"{avg_marks:.2f}", finalgrade]
        writer.writerow(row)

    print(f"\n Your report has been saved to '{csvfile}'.")
    
    
def check_histroy():
    if not os.path.isfile(csvfile):
        print("\n No previous record found.")
        return

    print("\n" + "=" * 55)
    print(" previous histroy/records")
    print("=" * 55)

    with open(csvfile, mode="r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                print("  " + " | ".join(f"{col:<12}" for col in row))
                print("  " + "-" * 80)
            else:
                print("  " + " | ".join(f"{col:<12}" for col in row))

    print("=" * 55)

#main program 

def main():
    print("\n" + "=" * 55)
    print("---<STUDENT GRADE ADVISOR>---")
    print("=" * 55)

    while True:
        print("\n  MENU")
        print("  1. Check my performance")
        print("  2. View previous results")
        print("  3. Quit")

        user_choices = input("\n Please enter a choice (1/2/3): ").strip()

        if user_choices == "1":
            print("\n Please enter Student Information \n")
            StudentName = imput_name_of_student()

            print(f"\n Hi {StudentName}! Please enter your score below. \n")
            marks_list = []
            weak_courses = []

            for subject in courses:
                score = marks(subject)
                level = efficiency(score)
                marks_list.append((subject, score, level))
                if level in ("At Risk", "Average"):
                    weak_courses.append(subject)


            total = sum(score for _, score, _ in marks_list)
            avg_marks = total / len(courses)
            finalgrade = grade_final(avg_marks)
            feedback = guidances(avg_marks, weak_courses)

            display_report(StudentName, marks_list, avg_marks, finalgrade, feedback)
            save_to_csv(StudentName, marks_list, avg_marks, finalgrade)

        elif user_choices == "2":
            check_histroy()
    

        elif user_choices == "3":
            print("\nSession complete. Thank you for using Student Grade Advisor.\n")
            break

        else:
            print("Invalid choice. Kindly enter 1/2/3.")
            
if __name__ == "__main__":
    main()
        
        