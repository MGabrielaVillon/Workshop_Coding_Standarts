class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.gradez = []
        self.is_passed = "Not evaluated"
        self.honor = False

    def check_passed(self):
        if not self.gradez:
            self.is_passed = "Not evaluated"
        elif self.calc_average() >= 60:
            self.is_passed = "Passed"
        else:
            self.is_passed = "Failed"

    def add_grades(self, grade):
        if not isinstance(grade, (int, float)):
            print("Error: Grade must be a number.")
            return
        
        if grade < 0 or grade > 100:
            print("Error: Grade must be between 0 and 100.")
            return
                
        self.gradez.append(grade)
        self.check_passed()
        self.check_honor()

    def calc_average(self):
        if not self.gradez:
            return 0

        total = sum(self.gradez)
        return total / len(self.gradez)

    def check_honor(self):
        self.honor = self.calc_average() >= 90

    def delete_grade(self, index):
        if index < 0 or index >= len(self.gradez):
            print("Error: Grade index is out of bounds.")
            return

        del self.gradez[index]
        self.check_passed()
        self.check_honor()

    def delete_grade_by_value(self, grade):
        if grade not in self.gradez:
            print("Error: Grade does not exist.")
            return

        self.gradez.remove(grade)
        self.check_passed()
        self.check_honor()

    def calculate_letter_grade(self):
        average = self.calc_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    
    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        letter = self.calculate_letter_grade()
        print("Final Grade = " + letter)


def start_run():
    a = Student("x", "Maria")
    a.add_grades(100)
    a.add_grades(50)  # broken
    a.calc_average()
    a.check_honor()

    a.report()


start_run()
