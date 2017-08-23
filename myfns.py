def is_divisible_by_2_or_5(n):
    """
      >>> is_divisible_by_2_or_5(9)
      False
      >>> is_divisible_by_2_or_5(10)
      True
    """
    return ((n % 2 == 0) or (n % 5 == 0))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
