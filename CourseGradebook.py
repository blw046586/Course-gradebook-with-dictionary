# CourseGradebook.py
import math
# Make sure Gradebook.py containing the base class definition exists
from Gradebook import Gradebook

class CourseGradebook(Gradebook):
    """
    Manages grade entries for a course using a nested dictionary structure:
    { assignment_name: { student_ID: score } }
    """
    def __init__(self):
        """
        Initializes the gradebook storage.
        Step 2: Choose and initialize attributes.
        """
        # Using a dictionary where keys are assignment names
        # and values are dictionaries mapping student IDs to scores.
        self.grades = {}

    # set_score() has parameters for the assignment name, student ID, and score.
    def set_score(self, assignment_name: str, student_id: int, score: float):
        """
        Sets the score for a given assignment and student ID.
        If the assignment doesn't exist, it's created.
        If the student doesn't have a score for the assignment, it's added.
        If the student already has a score, it's updated.
        Step 3: Implement set_score.
        """
        # Get the inner dict for the assignment, creating it if it doesn't exist
        assignment_scores = self.grades.setdefault(assignment_name, {})
        # Set/update the score for the student in the inner dict
        assignment_scores[student_id] = score

    # get_score() has parameters for the assignment name and student ID, and
    # returns a float for the corresponding score. math.nan is returned if
    # no such entry exists in the gradebook.
    def get_score(self, assignment_name: str, student_id: int) -> float:
        """
        Gets the score for a given assignment and student ID.
        Returns math.nan if the assignment or student score doesn't exist.
        Step 3: Implement get_score.
        """
        # Get the inner dict for the assignment, default to {} if assignment not found
        assignment_scores = self.grades.get(assignment_name, {})
        # Get the score from the inner dict, default to math.nan if student ID not found
        return assignment_scores.get(student_id, math.nan)

    # get_assignment_scores() takes a string for the assignment name and
    # returns a dictionary that maps a student ID to the student's
    # corresponding score for the assignment
    def get_assignment_scores(self, assignment_name: str) -> dict[int, float]:
        """
        Gets a dictionary of all scores for a given assignment name.
        Maps student ID (int) to score (float).
        Returns an empty dictionary if the assignment doesn't exist.
        Step 4: Implement get_assignment_scores.
        """
        # Get the inner dict, default to {}, and return a copy
        # Returning a copy prevents external modification of the internal gradebook data.
        return self.grades.get(assignment_name, {}).copy()

    # get_sorted_assignment_names() returns a list with all distinct assignment
    # names, sorted in ascending order
    def get_sorted_assignment_names(self) -> list[str]:
        """
        Returns a list of all unique assignment names, sorted alphabetically.
        Step 4: Implement get_sorted_assignment_names.
        """
        # Get all keys (assignment names) from the main dictionary
        assignment_names = list(self.grades.keys())
        # Sort and return the list
        assignment_names.sort() # Use sort() or sorted()
        return assignment_names
        # Alternatively: return sorted(list(self.grades.keys()))

    # get_sorted_student_IDs() returns a list with all distinct student IDs,
    # sorted in ascending order.
    def get_sorted_student_IDs(self) -> list[int]:
        """
        Returns a list of all unique student IDs present in the gradebook,
        sorted numerically.
        Step 4: Implement get_sorted_studentIDs.
        """
        all_student_ids = set()
        # Iterate through each assignment's score dictionary (the values of the outer dict)
        for student_scores in self.grades.values():
            # Add all student IDs (keys of the inner dict) from that assignment to the set
            # Using update() efficiently adds all elements from the iterable
            all_student_ids.update(student_scores.keys())
        # Convert the set of unique IDs to a list and sort it
        sorted_ids = list(all_student_ids)
        sorted_ids.sort() # Use sort() or sorted()
        return sorted_ids
        # Alternatively: return sorted(list(all_student_ids))

    # get_student_scores() gets all scores that exist in the gradebook for the
    # student whose ID equals the student_ID parameter. Scores are returned as
    # a dictionary that maps an assignment name to the student's corresponding
    # score for that assignment.
    def get_student_scores(self, student_id: int) -> dict[str, float]:
        """
        Gets a dictionary of all scores for a given student ID.
        Maps assignment name (str) to score (float).
        Returns an empty dictionary if the student ID has no scores.
        Step 4: Implement get_student_scores.
        """
        student_results = {}
        # Iterate through each assignment name and its associated scores dictionary
        for assignment_name, student_scores in self.grades.items():
            # Check if the student has a score recorded for this assignment
            score = student_scores.get(student_id) # Use get() for safe access
            if score is not None: # Check if student_id was found in the inner dict
                # If yes, add the assignment name and score to the result dict
                student_results[assignment_name] = score
        return student_results