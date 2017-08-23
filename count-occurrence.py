
def count(sub, s):
    """
      >>> count('iss', 'Mississippi')
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
    instance = 0
    l = len(sub)

    pos = strpos(sub, s, 0)
    if pos != -1:
        instance += 1

    while pos != -1:
        pos = strpos(sub, s[pos+l:], (pos+l))
        if pos != -1:
            instance += 1

    print ("count of instances: " + str(instance))
    return instance


def strpos(sub, s, curpos=0):
    # return the position of substring 'sub' in string 's'

    # first, check if sub exists in s
    print("string: ", s, ";substring: ", sub)
    pos = -1
    if sub in s:
        l1 = len(s)
        l2 = len(sub)
        for index1 in range(l1):
            #print("index1: [" + str(index1) + "] " + s[index1])
            if s[index1] == sub[0]:
                pos = index1
                temp = index1
                for index2 in range(l2):
                    #print("index2: [" + str(index2) + "] " + sub[index2])
                    if s[temp+index2] != sub[index2]:
                        pos = -1
                        break
                if pos != -1:
                    print ("IF strpos: " + str(pos+curpos))
                    return (pos+curpos)
                   
    print ("FI strpos: " + str(pos))
    return (pos)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    count('an', 'bandana')
    count('an', 'Pear')





