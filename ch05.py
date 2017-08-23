def compare(a, b):
    """
    >>> compare(8, 7)
    1
    >>> compare(6, 6)
    0
    >>> compare(6, 7)
    -1
    """
    if (a > b):
        return 1
    elif (a == b):
        return 0
    else:
        return -1


def hypotenuse(x, y):
    '''
    >>> hypotenuse(3, 4)
    5.0
    >>> hypotenuse(12, 5)
    13.0
    >>> hypotenuse(7, 24)
    25.0
    >>> hypotenuse(9, 12)
    15.0
    '''
    return (x**2 + y**2) ** 0.5



def countdown(n):
    """
    >>> countdown(10)
    10 9 8 7 6 5 4 3 2 1
    """
    while (n > 0):
        print n,
        n -= 1


def num_digits(n):
    """
    >>> num_digits(100)
    3
    >>> num_digits(0)
    1
    >>> num_digits(-10)
    2
    """
    if (n < 0):
        n = abs(n)

    if (n == 0):
        return 1

    count = 0
    while n > 0:
        count += 1
        n = n/10

    return count


def sqrt(n):
    """
    >>> sqrt(49)
    7.0
    >>> sqrt(225)
    15.0
    """
    if (n < 0):
        n = abs(n)

    if (n == 0)
        return 0

    approx = 1.0
    diff = 0.000000001
    better = (approx + n/approx)/2.0
    print "approx:", approx, "\t", "better:", better

    while (abs(better - approx) > diff):
        approx = better
        better = (approx + n/approx)/2.0
        print "approx:", approx, "\t", "better:", better

    print "Ans:", better ** 2
    return better




if __name__ == '__main__':
    import doctest
    doctest.testmod()

