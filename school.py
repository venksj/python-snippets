import sys

class Member:
    def __init__(self, name, age, address=None):
        self.name = name
        self.age = age
        self.address = address
        print "Initialized Member %s" %name

    def __str__(self):
        return "Name: " + self.name + "; Age: " + str(self.age) + "; Address: " + str(self.address)


class Teacher(Member):
    def __init__(self, name, age, salary, address=None, courses=None, leaves=20):
        Member.__init__(self, name, age, address)
        self.salary = salary
        self.courses = courses
        self.leaves = leaves
        print "Initialized Teacher %s" %name


class Student(Member):
    number = 0
    def __init__(self, name, age, fees, address=None):
        Member.__init__(self, name, age, address)
        Student.number += 1
        self.rollno = Student.number + 1000
        self.fees = fees
        print "Initialized Student %s" %name


if __name__ == '__main__':
    t1 = Teacher("T1", 40, 40000) 
    print t1

    s1 = Student("S1", 20, 5000)
    print s1

