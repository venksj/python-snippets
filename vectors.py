import string

def add_vectors(u, v):
    """
    >>> add_vectors([1, 0, 2], [1, 1, 1])
    [2, 1, 3]
    >>> add_vectors([1, 2], [1, 4])
    [2, 6]
    >>> add_vectors([1, 2, 1], [1, 4, 3])
    [2, 6, 4]
    >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
    [13, -4, 13, 5]
    """
    i = 0
    w = []

    while i < len(u):
        w.append(u[i] + v[i])
        i += 1

    return w


def dot_product(u, v):
    """
    >>> dot_product([1, 1], [1, 1])
    2
    >>> dot_product([1, 2], [1, 4])
    9
    >>> dot_product([1, 2, 1], [1, 4, 3])
    12
    >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
    0
    """
    sum = 0
    for i in range(len(u)):
        sum += (u[i] * v[i])
    return sum



def add_row(matrix):
    """
    >>> m = [[0, 0], [0, 0]]
    >>> add_row(m)
    [[0, 0], [0, 0], [0, 0]]
    >>> n = [[3, 2, 5], [1, 4, 7]]
    >>> add_row(n)
    [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
    >>> n
    [[3, 2, 5], [1, 4, 7]]
    """
    rows = len(matrix)
    cols = len(matrix[0])
    new_m = []
    for i in range(rows):
        new_m.append(matrix[i])
    new_m.append([0]*cols)
    return new_m


def add_matrices(m1, m2):
    """
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[2, 2], [2, 2]]
    >>> add_matrices(a, b)
    [[3, 4], [5, 6]]
    >>> c = [[8, 2], [3, 4], [5, 7]]
    >>> d = [[3, 2], [9, 2], [10, 12]]
    >>> add_matrices(c, d)
    [[11, 4], [12, 6], [15, 19]]
    >>> c
    [[8, 2], [3, 4], [5, 7]]
    >>> d
    [[3, 2], [9, 2], [10, 12]]
    """
    new_mtx = []
    rows = len(m1) # 2
    cols = len(m1[0]) #2
    for i in range(rows): 
        new_mtx.append([0] * cols)
    for i in range(rows): 
        for j in range(cols): 
            new_mtx[i][j] = (m1[i][j] + m2[i][j])
    return new_mtx


def replace(s, old, new):
    """
    >>> replace('Mississippi', 'i', 'I')
    'MIssIssIppI'
    >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
    >>> replace(s, 'om', 'am')
    'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
    >>> replace(s, 'o', 'a')
    'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
    """
    return string.join(string.split(s, old), new)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

