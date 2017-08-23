
def outer():
    x = 1
    def inner():
        y = 0
        print "Inner: "
        print "------------"
        print locals()
        print "Value of x is %d" %x

    print "Outer: "
    print "------------"
    print locals()

    inner()


outer()
