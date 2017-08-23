
def infinite_recursion(number):
    try:
        print "recursion depth %d" %(number)
        infinite_recursion(number +  1)
    except:
        print "Recursion Depth exceeded"


def countdown(n):
    if n == 0:
        print "BlastOff"
    else:
        countdown(n-1)


#find_max in a list using recursion
def find_max(vjlist, cur_max):
    """
    >>> find_max([1, 11, 4, 9], 0)
    11
    """
    #print len(vjlist), cur_max
    if len(vjlist) == 0:
        print cur_max
        #return cur_max
    else:
        #print vjlist[0]
        if (cur_max < vjlist[0]):
            cur_max = vjlist[0]
        find_max(vjlist[1:], cur_max)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #infinite_recursion(0)

