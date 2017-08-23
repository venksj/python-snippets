

def myreplace(old, new, s):
    """
    Replace all occurences of old with new in the string s.

    >>> myreplace(',', ';', 'this, that, and, some, other, thing')
    'this; that; and; some; other; thing'
    >>> myreplace(' ', '**', 'Words will now be separated by stars.')
    'Words**will**now**be**separated**by**stars.'
    """ 
    return new.join(s.split(old))
    


def cleanword(word):
    """
    >>> cleanword('what?')
    'what'
    >>> cleanword('"now!"')
    'now'
    >>> cleanword('?+="word!,@$()"')
    'word'
    """
    new_word = ''
    sep = '?"!+=,@$()'
    for x in word:
        if x in sep:
            continue
        new_word += x
    return new_word



def has_dashdash(s):
    """
    >>> has_dashdash('distance--but')
    True
    >>> has_dashdash('several')
    False
    >>> has_dashdash('critters')
    False
    >>> has_dashdash('spoke--fancy')
    True
    >>> has_dashdash('yo-yo')
    False
    """
    sep = '--'
    l = (s.split(sep))
    if (len(l) > 1):
        return True
    else:
        return False




if __name__ == '__main__':
    import doctest
    doctest.testmod()
