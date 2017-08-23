import sys

def find_mean():
    """
    >>> find_mean 21 31 35
    29.0
    """
    #>>> find_mean 21 31 36
    #29.3333333

    largs = sys.argv[1:]
    for index, value in enumerate(largs):
        largs[index] = float(value)

    print "Sum is: %f" %(sum(largs))

    vjmean = sum(largs)/len(largs)

    print "Mean is: %f" %(vjmean)

    return vjmean


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    #find_mean()
