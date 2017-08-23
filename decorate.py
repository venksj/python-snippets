
def test(func):
    def new_test(*args, **kwargs):
        print "start"
        func(*args, **kwargs)
        print "stop"
    return new_test


titles = ['creature of habit', 'crewel tale']
plots  = ['a nun turns into a monster', 'a haunted yarn shop']

@test
def myprint(titles, plots):
    d1 = dict(zip(titles, plots))
    print d1


if __name__ == '__main__':
    myprint(titles, plots)


