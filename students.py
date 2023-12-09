import statistics as stats


class Students:

    def __init__(self):
        """
        Initializes a Students object with empty lists for names and grades and sets total to 0.
        """
        self.__student_names = []
        self.__student_grades = []
        self.__total = 0

    def get_total(self) ->int:
        """
        Returns the total number of students.

        Returns:
            int: The total number of students.
        """
        return self.__total

    def get_names(self) -> list:
        """
        Returns a list of student names.

        Returns:
            list: A list containing the names of all students.
        """
        return self.__student_names

    def get_grades(self) -> list:
        """
        Returns a list of student grades.

        Returns:
            list: A list containing the grades of all students.
        """
        return self.__student_grades

    def clear(self):
        """
        Clears the list of student names, grades, and resets the total count.
        """
        self.__student_names = []
        self.__student_grades = []
        self.__total = 0

    def add_student(self, name: str, grade: float) -> bool:
        """
        Adds a new student with the given name and grade.

        Args:
            name (str): The name of the student.
            grade (int): The grade of the student.

        Returns:
            bool: True if the student was successfully added, False otherwise.
        """
        if isinstance(name, str) and isinstance(grade,float):
            self.__student_names.append(name)
            self.__student_grades.append(grade)
            self.__total += 1
        else:
            return False

    def delete_student(self):
        """
        Deletes the last added student from the list.
        """
        if self.__total != 0:
            del self.__student_names[-1]
            del self.__student_grades[-1]
            self.__total -= 1

    def get_average(self) -> float:
        """
        Calculates and returns the average grade of all students.

        Returns:
            float: The average grade of all students.
        """
        grades = self.__student_grades
        average = stats.mean(grades)
        return float(average)

    def __str__(self) -> str:
        """
        Returns a string representation of the Students object.

        Returns:
            str: A string representation of the Students object.
        """
        return f"Students = {self.__student_names}, Grades = {self.__student_grades}"
