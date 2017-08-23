def reverse(s1):
    """
    >>> reverse('happy')
    'yppah'
    >>> reverse('Python')
    'nohtyP'
    >>> reverse("")
    ''
    >>> reverse("P")
    'P'
    """
    s2 = ""
    nc = len(s1) -1
    while nc >= 0:
        s2 += s1[nc]
        nc -= 1
    return s2


def mirror(s1):
    """
    >>> mirror("good")
    'gooddoog'
    >>> mirror("yes")
    'yessey'
    >>> mirror('Python')
    'PythonnohtyP'
    >>> mirror("")
    ''
    >>> mirror("a")
    'aa'
    """
    s2 = ""
    nc = len(s1) -1
    while nc >= 0:
        s2 += s1[nc]
        nc -= 1
    return s1+s2



def remove_letter(letter, strng):
    """
    >>> remove_letter('a', 'apple')
    'pple'
    >>> remove_letter('a', 'banana')
    'bnn'
    >>> remove_letter('z', 'banana')
    'banana'
    >>> remove_letter('i', 'Mississippi')
    'Msssspp'
    """
    s2 = ""
    for x in strng:
        if x == letter:
            continue
        s2 += x
    return s2


def is_palindrome(s):
    """
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abab')
    False
    >>> is_palindrome('tenet')
    True
    >>> is_palindrome('banana')
    False
    >>> is_palindrome('straw warts')
    True
    """
    s2 = reverse(s)
    if s2 == s:
        return True
    else:
        return False


def find(st, ch, pos=0):
    """
    >>> find("bannon", "on", 0)
    4
    >>> find("banana", "an", 0)
    1
    >>> find("bicycle", "cyc", 0)
    2
    >>> find('Mississippi', 'pp')
    8
    """
    index = pos
    while index < len(st):
        part = st[index:(index + len(ch))]
        if part == ch:
            return index
        index += 1
    return -1



def count(sub, s):
    """
    >>> count('is', 'Mississippi')
    2
    >>> count('an', 'banana')
    2
    >>> count('ana', 'banana')
    2
    >>> count('nana', 'banana')
    1
    >>> count('nanan', 'banana')
    0
    """
    index = 0
    nc = 0
    pos = 0
    while index <= len(s):
        index = find(s, sub, pos)
        if index == -1:
            break
        else:
            nc += 1
            index += 1
            pos = index
    return nc


def remove(sub, s):
    """
    >>> remove('an', 'banana')
    'bana'
    >>> remove('cyc', 'bicycle')
    'bile'
    >>> remove('iss', 'Mississippi')
    'Missippi'
    >>> remove('egg', 'bicycle')
    'bicycle'
    """
    s2 = ""
    index = find(s, sub)
    if index != -1:
        s2 += s[:index] + s[index+len(sub):]
    else:
        s2 = s[:]
    return s2


def remove_all(sub, s):
    """
    >>> remove_all('an', 'bandana')
    'bda'
    >>> remove_all('cyc', 'bicycle')
    'bile'
    >>> remove_all('iss', 'Mississippi')
    'Mippi'
    >>> remove_all('eggs', 'bicycle')
    'bicycle'
    """
    index = 0
    prev = index
    s2 = ""
    while index < len(s):
        index = find(s, sub, prev)
        if index == -1:
            s2 += s[prev:]
            break
        else:
            s2 += s[prev:index]
            index += len(sub)
            prev = index
    return s2




if __name__ == '__main__':
    import doctest
    doctest.testmod()

