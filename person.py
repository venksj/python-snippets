import sys

class Person:
    number = 0
    head   = None

    def __init__(self, name=None, age=0, next=None):
        if name: print "Init %s" %name
        else: print "Init ..."

        self.name = name
        self.age = age
        self.next = next
        Person.number += 1
        Person.head = self


    def __str__(self):
        return ("Name: " + str(self.name) + "; Age: " + str(self.age))

    def hello(self):
        print "I am %s" %(self.name)

    def die(self):
        print "die ..."

        tmp = Person.head
        # first node matches
        if tmp == self:
            print "First"
            Person.head = tmp.next
            tmp.next = None
        else:
            print "Not first"
            # some intermediate node
            count = 1
            prev = tmp
            tmp = tmp.next
            while tmp:
                print count, tmp
                count += 1
                if tmp == self:
                    print "Found"
                    prev.next = tmp.next
                    tmp = None
                    break
                else:
                    prev = tmp
                    tmp = tmp.next

        Person.number -= 1

        if Person.number == 0:
            print "No more Person objects left"
        else:
            print "We have %d Person objects remaining" %(Person.number)

    @classmethod
    def how_many(cls):
        print "We have %d Person objects remaining" %(Person.number)


if __name__ == '__main__':
    import doctest

    p1 = Person("Person1", 6)
    p2 = Person("Person2", 10, p1)
    p3 = Person("Person3", 12, p2)

    tmp = Person.head
    prefix = "|-"
    while tmp:
        print prefix, tmp.name, tmp.age
        tmp = tmp.next 

    Person.how_many()
    p1.die()

    tmp = Person.head
    prefix = "|-"
    while tmp:
        print prefix, tmp.name, tmp.age
        tmp = tmp.next 

