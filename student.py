import sys
import os
class Person:
    def __init__(self, name):
        self.__name = name  

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Student(Person):
    students = [] 
    def __init__(self, name, roll_number, grade):
        super().__init__(name)
        self.__roll_number = roll_number
        self.__grade = grade
    

    @property
    def roll_number(self):
        return self.__roll_number

    @roll_number.setter
    def roll_number(self, roll_number):
        self.__roll_number = roll_number

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    def __str__(self):
        return f"name: {self.name}, roll number: {self.roll_number}, grade: {self.grade}"
    
    @classmethod
    def update_grade(cls):
        try:

            roll_number = int(input("roll number: "))
            new_grade = input("new grade: ").strip()
            for i in cls.students:
                if i.roll_number == roll_number:
                        i.grade = new_grade
                        return
            print("student not found")
        except ValueError:
            print("please enter integer.")
        
    @staticmethod
    def see_students(students):
        if students:
            for i in students:
                print(i)
        else:
            print("no students found")

    @classmethod
    def find_student(cls):
        try:
            roll_number = int(input("roll number: "))
            for i in cls.students:
                if i.roll_number == roll_number:
                    print(i)
                    return

            print("not found")
        except ValueError:
            print("please enter integer.")
    
    @classmethod
    def add_new_student(cls):
        try:
            name = input("name: ").strip()
            roll_number = int(input("roll_number: "))
            grade = input("grade: ").strip()
            for student in cls.students:
                if student.roll_number == roll_number:
                    print("Student with same roll number is already registered.")
                    return
            cls.students.append(Student(name, roll_number, grade))
            print("student added")
        except ValueError:
            print("please enter integer.")
    
    @classmethod
    def deleteStudent(self,roll_number):
        for i in self.students:
            if i.roll_number == roll_number:
                self.students.remove(i)
                return
        print("no student found with that roll number")
        


    @staticmethod
    def filter_by_grade(students):
        print("students with good grades: ")
        for student in students:
            for i in ["A","B"]:
                if i in student.grade:
                    print(student)


    @staticmethod
    def write_to_file(students):
        with open("students.txt","w") as f:
                for i in students:
                    f.write(f"{i.name}:{i.roll_number}:{i.grade}\n")
                

    @staticmethod
    def read_file(students):
        with open("students.txt","r") as file:
            for i in file:
                name,roll_number,grade = i.replace("\n","").split(":")
                if not any(s.roll_number == int(roll_number) for s in students):
                    students.append(Student(name, int(roll_number), grade))
                

                
           


if __name__ == "__main__":
    Student.read_file(Student.students)
    actions = [
           lambda:Student.add_new_student(),
           lambda:Student.see_students(Student.students),
           lambda:Student.find_student(),
           lambda:Student.update_grade(),
           lambda:Student.filter_by_grade(Student.students) ,
           lambda:Student.deleteStudent(int(input("roll number to delete: "))),
           lambda:sys.exit()
    ]
    while True:
            for i in ["0.add new student","1.see all students","2.find student by roll number","3.update grade","4.filter by grade","5.delete student","6.exit"]:
                print(i)
            try:
                action = int(input("your choice: "))
            except ValueError:
                print("action should be int")
                continue
            if 0 <= action < len(actions):
                if action == 6:
                    Student.write_to_file(Student.students)
                actions[action]()
            else:
                print("not right option")

        