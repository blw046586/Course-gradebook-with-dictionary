# Course-gradebook-with-dictionary
Step 1: Inspect the Gradebook base class
The read-only Gradebook.py file has a declaration for the Gradebook base class. The Gradebook class stores a collection of entries for a course. Conceptually, a gradebook entry is an (assignment name, student ID, score) triplet. Each entry's assignment name is a string, student ID is an Integer, and score is a float. A score is entered into the gradebook via the set_score() method.

The Gradebook class has six methods that must be implemented in a derived class.


Step 2: Implement the CourseGradebook class's __init__() method
The CourseGradebook class inherits from Gradebook and is declared in CourseGradebook.py. Inspect each method that must be implemented. Choose one or more attributes to store gradebook data, and add the attributes to the CourseGradebook class by implementing the __init__() method. Several options exist, so grading does not analyze the choice of attributes.


Step 3: Implement CourseGradebook's set_score() and get_score() methods
Implement the set_score() method to enter a single entry into the gradebook. set_score() has parameters for the assignment name, student ID, and score. How the entry is stored depends on the attributes chosen in step 2.

Implement the get_score() method to return a single score from the gradebook. get_score() has parameters for the assignment name and student ID, and returns a float for the corresponding score. math.nan is returned if no such entry exists in the gradebook.

Code in main.py calls test_get_score_and_set_score() to test both methods. Run your program and ensure that the test passes before proceeding further.


Step 4: Implement the remaining CourseGradebook methods
Implement the remaining methods according to the specifications below.

get_assignment_scores() takes a string for the assignment name and returns a dictionary that maps a student ID to the student's corresponding score for the assignment. An entry exists in the returned dictionary only if a score has been entered with the set_score() method. An empty dictionary is returned if no such assignment exists in the grade book.
get_sorted_assignment_names() returns a list with all distinct assignment names, sorted in ascending order.
get_sorted_studentIDs() returns a list with all distinct student IDs, sorted in ascending order.
get_student_scores() gets all scores that exist in the gradebook for the student whose ID equals the method argument. Scores are returned as a dictionary that maps an assignment name to the student's corresponding score for that assignment.
