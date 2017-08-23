# Add doctests here
'''
   >>> a_list[3]
   42
   >>> a_list[6]
   'Ni!'
   >>> len(a_list)
   8
   >>> b_list[1:]
   ['Stills', 'Nash']
   >>> group = b_list + c_list
   >>> group[-1]
   'Young'
   >>> 'war' in mystery_list
   False
   >>> 'peace' in mystery_list
   True
   >>> 'justice' in mystery_list
   True
   >>> 'oppression' in mystery_list
   False
   >>> 'equality' in mystery_list
   True
   >>> range(a, b, c)
   [5, 9, 13, 17]
   >>> 13 in junk
   True
   >>> del junk[4]
   >>> junk
   [3, 7, 9, 10, 17, 21, 24, 27]
   >>> del junk[x:y]
   >>> junk
   [3, 7, 27]
'''

# Python code begins here
a_list = [0, 1, 2, 42, 4, 5, 'Ni!', 8]

b_list = ['Zero', 'Stills', 'Nash']
c_list = ['Young']

mystery_list = ['peace', 'justice', 'equality']

a = 5
b = 20
c = 4

junk = [3, 7, 9, 10, 13, 17, 21, 24, 27]
x = 2
y = 7

if __name__ == '__main__':
    import doctest
    doctest.testmod()

