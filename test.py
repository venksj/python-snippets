def cat_n_times(s, n):
    print s*n

cat = [1, 2, 3]

print "Cat is %r" %(cat)

x = "There are %d types of people" %10
binary = "binary"
donot = "don't"
y = "Those who know %s and those who %s" %(binary, donot)

print x 
print y

print "I said: %r" %x
print "I also said: '%s'" %y

hil = False
joke = "Isn't this joke funny?! %r"

print joke % hil

w = "This is the left side of ... "
e = "a string with a right side"

print w + e

a1 = 'C'
a2 = 'h'
a3 = 'e'
a4 = 'e'
a5 = 's'
a6 = 'e'
b1 = 'B'
b2 = 'u'
b3 = 'r'
b4 = 'g'
b5 = 'e'
b6 = 'r'

print '.' * 20
#print a1 + a2 + a3 + a4 + a5 + a6,
#print b1 + b2 + b3 + b4 + b5 + b6

f1 = "%r %r %r %r"
f2 = "%s %s %s %s"

print f1 %("one", "two", "three", "four")
print f2 %("one", "two", "three", "four")
print f1 %(f1, f2, f1, f2)

d = "mon tue wed thu fri sat sun"
m = "jan\nfeb\nmar\napr\nmay\njun"

print "days:", d
print "days: %r" %d
print "months: %r" %m
print "months:\n", m

print """
Let's see if i can print multiple lines at the same time.
This is the second line.
Today is a match between RCB and KXIP
Not that interesting ...
"""

