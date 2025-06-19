import sys
import os
import re


# პერსონ კლასი არის სტუდენტის parent კლასი და ამ კლასში ხდება სახელის ინიციალიზაცია
class Person:
    def __init__(self, name):
        self.__name = name  

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name



# სტუდენტ კლასში გაწერილია ძირითადი ფუნქციონალი
class Student(Person):
    students = [] # აქ ხდება სტუდენტის ობიექტების შენახვა
    def __init__(self, name, roll_number, grade): # აქ ხდება უშუალოდ ინიციალიზაცია ყველა ატრიბუტის
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
    
    # ამ მეთოდით ხდება ნიშნის განახლება
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
        
    # ეს მეთოდი უბრალოდ სტუდენტ ლისტში არსებულ ყველა სტუდენტს პრინტავს
    @staticmethod
    def see_students(students):
        if students:
            for i in students:
                print(i)
        else:
            print("no students found")


    
    # ამ მეთოდით ხდება სტუდენტის პოვნა roll_number-ით 
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
    

    # ამ მეთოდით ხდება უშუალოდ ახალი სტუდენტის დამატება
    @classmethod
    def add_new_student(cls):
        try:
            name = input("name: ").strip()
            roll_number = int(input("roll_number: "))
            grade = input("grade: ").strip().upper()
            if not re.match(r'^(?:[A-DF])[+-]?$',grade):
                print("not right grade")
                return
            for student in cls.students:
                if student.roll_number == roll_number:
                    print("Student with same roll number is already registered.")
                    return
            cls.students.append(Student(name, roll_number, grade))
            print("student added")
        except ValueError:
            print("please enter integer.")
    

    # ამ მეთოდით ხდება სტუდენტის წაშლა 
    @classmethod
    def deleteStudent(self,roll_number):
        for i in self.students:
            if i.roll_number == roll_number:
                self.students.remove(i)
                return
        print("no student found with that roll number")
        

    #ამ მეთოდით ხდება "კარგი სტუდენტების" დაბეჭდვა
    @staticmethod
    def filter_by_grade(students):
        print("students with good grades: ")
        for student in students:
            for i in ["A","B"]:
                if i in student.grade:
                    print(student)

    # ეს მეთოდი გამოყენებულია როდესაც მომხმარებელი გადაწყვეტს რომ პროგრამა გამორთოს და ის ანახლებს students.txt
    @staticmethod
    def write_to_file(students):
        with open("students.txt","w") as f:
                for i in students:
                    f.write(f"{i.name}:{i.roll_number}:{i.grade}\n")
                
    # ეს ფუნქცია გამოიყენება პროგრამის დასაწყისში და მოაქვს ინფორმაცია students.txt-დან
    @staticmethod
    def read_file(students):
        with open("students.txt","r") as file:
            for i in file:
                name,roll_number,grade = i.replace("\n","").split(":")
                if not any(s.roll_number == int(roll_number) for s in students):
                    students.append(Student(name, int(roll_number), grade))
                

                
           


if __name__ == "__main__":
    Student.read_file(Student.students)
    actions = [ # აქ ყველა ფუნქცია დიქტში მაქვს ჩაწერილი
           lambda:Student.add_new_student(),
           lambda:Student.see_students(Student.students),
           lambda:Student.find_student(),
           lambda:Student.update_grade(),
           lambda:Student.filter_by_grade(Student.students) ,
           lambda:Student.deleteStudent(int(input("roll number to delete: "))),
           lambda:sys.exit()
    ]

    # და აქ არის while loop რომელშიც მომხმარებელი ირჩევს თუ რისი გაკეთება უნდა.
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
name2 = Person("asfsaf")