
try:
    text = raw_input("Enter something: ")
except EOFError:
    print "\n\t\tEOF symbol received"
except KeyboardInterrupt:
    print "\n\t\tKeyboard interrupt received"
else:
    print "\tYou entered: " + str(text)

