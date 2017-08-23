
import sys
import os


def fibonacci_1(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)


computed_vals = {1: 1, 0: 1}

def fibonacci_2(n1):
    n = int(n1)
    if computed_vals.has_key(n):
        return computed_vals[n]
    else:
        new_value = fibonacci_2(n -1) + fibonacci_2(n -2)
        computed_vals[n] = new_value
        return new_value

letters = {}

def letter_count(s1):
    for x in s1:
        letters[x] = letters.get(x, 0) + 1

    print "letters: ",
    print letters

    letter_items = letters.items()
    print "letter_items: ", 
    print letter_items

    letter_items.sort()
    print "sorted letter_items: ", 
    print letter_items



if __name__ == '__main__':
    #x = fibonacci_2(sys.argv[1])
    #print "Fibonacci of %s is %d" %(sys.argv[1], x)
    #print computed_vals

    letter_count(sys.argv[1])


