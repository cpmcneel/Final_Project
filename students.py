import statistics as stats


class Students:

    def __init__(self):
        self.__student_names = []
        self.__student_grades = []
        self.__total = 0

    def get_total(self):
        return self.__total

    def get_names(self):
        return self.__student_names

    def get_grades(self):
        return self.__student_grades

    def clear(self):
        self.__student_names = []
        self.__student_grades = []
        self.__total = 0

    def add_student(self, name, grade):
        if isinstance(name, str) or isinstance(grade, int):
            self.__student_names.append(name)
            self.__student_grades.append(grade)
            self.__total += 1
        else:
            return False

    def delete_student(self):
        if self.__total != 0:
            del self.__student_names[-1]
            del self.__student_grades[-1]
            self.__total -= 1

    def get_average(self):
        grades = self.__student_grades
        average = stats.mean(grades)
        return float(average)

    def __str__(self):
        return f"Students = {self.__student_names}, Grades = {self.__student_grades}"
