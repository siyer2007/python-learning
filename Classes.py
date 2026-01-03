class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_puppy(self):
        if self.age < 2:
            return True

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    
    def passed(self):
        if self.mark >= 50:
            return True
        else:
            return False
        
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

class Employee:
    def __init__(self, name, hourly_rate, total_hours):
        self.name = name
        self.hourly_rate = hourly_rate
        self.total_hours = total_hours

    def add_hours(self, hours):
        self.total_hours += hours
    
    def weekly_pay(self):
        (self.total_hours) * (self.hourly_rate)


class Student:
    def __init__(self, name, studentID):
        self.name = name
        self.studentID = studentID

class Course:
    def __init__(self, course_name, student):
        self.course_name = course_name
        self.student = student

    def student_name(self):
        return self.student.name