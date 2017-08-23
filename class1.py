class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def exclaim(self):
        print ("My name is: %s and I'm %d years old" %(self.name, self.age))


class EmailPerson(Person):
    def __init__(self, name, age, email):
        # python 2: works
        Person.__init__(self, name, age)

        # python 2: doesn't work
        #super(Person, self).__init__(name, age)

        # python 3: works
        #super().__init__(name, age)

        self.email = email

    def addon(self):
        print ("My email is: %s" %(self.email))

p1 = Person('Adit', 11)
p1.exclaim()

e1 = EmailPerson('Rishith', 10, 'rishith@ms.com')
e1.exclaim()
e1.addon()


