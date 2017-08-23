
# vjlist = [1, 2, [3, 4], 5, 6]
def sum_by_recursion(vjlist):
    """
    >>> sum_by_recursion([1, 2, [3, 4], 5, 6])
    21
    """
    vjsum = 0
    for x in vjlist:
        if (type(x) == type([])):
            vjsum += sum_by_recursion(x)
        else:
            vjsum += x
    return vjsum
       

def get_age(age):
    """
    >>> get_age(31)
    31
    >>> get_age(-1)
    """
    if (age < 0):
        raise ValueError, "%s is not a valid age" %(age)
    return age



if __name__ == '__main__':
    import doctest
    doctest.testmod()
