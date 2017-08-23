
import sys
import doctest

    
class vjTime:
    def __init__(self, hh=0, mm=0, ss=0):
        self.hours = hh
        self.minutes = mm
        self.seconds = ss

    def print_time(self):
        print "Time: %02d:%02d:%02d" %(self.hours, self.minutes, self.seconds)

    def after(self, t):
        return ((self.convert_to_seconds() - t.convert_to_seconds()) > 0)

    def convert_to_seconds(self):
        return self.hours*60*60 + self.minutes*60 + self.seconds

    def add_time(self, t):
        secs = self.convert_to_seconds() + t.convert_to_seconds()
        return make_time(secs)

    def make_time_x(self, seconds):
        self.hours = seconds/3600

        remain_1 = seconds - (self.hours*3600)
        self.minutes = remain_1/60

        remain_2  = remain_1 - (self.minutes*60)
        self.seconds = remain_2


    def increment(self, seconds):
        new_sec = self.convert_to_seconds() + seconds
        self = make_time(new_sec)





def add_time(t1, t2):
    '''Add the two time-periods specified by t1 and t2.

    Returns the answer as an object of class vjTime.'''

    secs = convert_to_seconds(t1) + convert_to_seconds(t2)
    return make_time(secs)


def make_time(seconds):
    t = vjTime()
    t.hours = seconds/3600

    remain_1 = seconds - (t.hours*3600)
    t.minutes = remain_1/60

    remain_2  = remain_1 - (t.minutes*60)
    t.seconds = remain_2

    return t



if __name__ == '__main__':
    print add_time.__doc__

    t1 = make_time(int(sys.argv[1]))
    t1.print_time()

    t2 = vjTime()
    t2.make_time_x(int(sys.argv[2]))
    t2.print_time()

    t3 = t1.add_time(t2)
    t3.print_time()

    print t1.after(t2)

    t4 = vjTime(9, 10)
    t4.print_time()
