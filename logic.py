from PyQt6.QtWidgets import *
from gui import *
from students import Students
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Initialize the Logic class by setting up the UI and connecting button signals.
        """
        super().__init__()
        self.setupUi(self)

        self.button_enter.clicked.connect(lambda: self.enter())
        self.button_done.clicked.connect(lambda: self.done())
        self.button_delete.clicked.connect(lambda: self.delete())
        self.s = Students()
        self.final_string = ""

    def grade_students(self) -> dict:
        """
                Assign letter grades to student scores based on a certain criteria.

                Returns:
                    dict: A dictionary mapping student scores to their corresponding letter grades.
                """
        scores = self.s.get_grades()
        if len(scores) > 0:
            best = max(scores)
            grades = {}
            for grade in self.s.get_grades():
                if grade >= best - 10:
                    grades[grade] = 'A'
                elif grade >= best - 20:
                    grades[grade] = 'B'
                elif grade >= best - 30:
                    grades[grade] = 'C'
                elif grade >= best - 40:
                    grades[grade] = 'D'
                else:
                    grades[grade] = 'F'
            return grades
        else:
            return None

    def grade_average(self) -> dict:
        """
                Assign a letter grade to the average score based on a certain criteria.

                Returns:
                    dict: A dictionary mapping the average score to its corresponding letter grade.
                """
        scores = self.s.get_grades()
        if len(scores) > 0:
            best = max(scores)
            average = self.s.get_average()
            average_dict = {}

            if average >= best - 10:
                average_dict[average] = 'A'
            elif average >= best - 20:
                average_dict[average] = 'B'
            elif average >= best - 30:
                average_dict[average] = 'C'
            elif average >= best - 40:
                average_dict[average] = 'D'
            else:
                average_dict[average] = 'F'

            return average_dict
        else:
            return None

    def enter(self):
        """
        Handle the 'Enter' button click event, add student information, and update the UI.
        """
        try:
            name = str(self.input_name.text())
            grade = float(self.input_grade.text())
        except ValueError:
            self.error_label.setText(f"Name must be text and grade must be a positive number")
            return

        if grade > 0:
            self.s.add_student(name, grade)
            names = self.s.get_names()
            scores = self.s.get_grades()
        else:
            self.error_label.setText(f"Name must be text and grade must be a positive number")
            return

        output_string = ""

        if self.s.get_total() > 0:
            for i in range(self.s.get_total()):
                output_string += f"{names[i]}, {scores[i]}\n"

        self.final_string = ""
        self.input_name.setFocus()
        self.error_label.setText("")
        self.total_count.setText(f"{self.s.get_total()}")
        self.input_name.setText("")
        self.input_grade.setText("")
        self.output.setText(output_string)

    def done(self):
        """
        Handle the 'Done' button click event, display the final information, save to CSV, and clear data.
        """
        if self.s.get_total() > 0:
            names = self.s.get_names()
            scores = self.s.get_grades()
            grades = self.grade_students()
            average = self.s.get_average()
            average_grade = self.grade_average()

            for i in range(0, self.s.get_total()):
                self.final_string += f"Student {names[i]}'s score is {scores[i]} and their grade is {grades[scores[i]]}\n"

            self.final_string += f"The average score is {average:.2f}, a grade of {average_grade[average]}"

            self.output.setText(self.final_string)
            self.save(names, scores, grades, average, average_grade)
            self.s.clear()
            self.total_count.setText(f"{self.s.get_total()}")


        else:
            self.output.setText("")

    def save(self, names: list, scores: list, grades: dict, average: float, average_grade: dict):
        """
        Save student information, scores, and grades to a CSV file.

        Args:
            names (list): List of student names.
            scores (list): List of student scores.
            grades (dict): Dictionary mapping student scores to their corresponding letter grades.
            average (float): Average student score.
            average_grade (dict): Dictionary mapping the average score to its corresponding letter grade.
        """
        with open("grades.csv", "w") as csv_write:
            csv_writer = csv.writer(csv_write)
            csv_writer.writerow(['Name', 'Grade', 'Letter'])

            for i in range(self.s.get_total()):
                csv_writer.writerow([names[i], scores[i], grades[scores[i]]])

            csv_writer.writerow(["Average", average, average_grade[average]])

    def delete(self):
        """
        Handle the 'Delete' button click event, delete a student, and update the UI.
        """
        self.s.delete_student()

        names = self.s.get_names()
        scores = self.s.get_grades()

        output_string = ""

        if self.s.get_total() > 0:
            for i in range(self.s.get_total()):
                output_string += f"{names[i]}, {scores[i]}\n"

        self.final_string = ""
        self.output.setText(output_string)
        self.input_name.setFocus()
        self.error_label.setText("")
        self.total_count.setText(f"{self.s.get_total()}")
        self.input_name.setText("")
        self.input_grade.setText("")
