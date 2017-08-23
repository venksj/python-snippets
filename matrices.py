
def make_matrix(rows, columns):
    '''
    >>> make_matrix(3, 5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> make_matrix(4, 2)
    [[0, 0], [0, 0], [0, 0], [0, 0]]
    >>> m = make_matrix(4, 3)
    >>> m[1][1] = 7
    >>> m 
    [[0, 0, 0], [0, 7, 0], [0, 0, 0], [0, 0, 0]]
    '''
    l1 = []
    for i in range(rows):
            l1 += [[0] * columns]

    return l1



if __name__ == '__main__':
    import doctest
    doctest.testmod()


