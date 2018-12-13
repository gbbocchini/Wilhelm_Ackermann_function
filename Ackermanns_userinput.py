import time
import sys
from progressbar import ProgressBar, Percentage, Bar

sys.setrecursionlimit(4096*10)


print("\nWelcome to the Ackmermann function! History: https://en.wikipedia.org/wiki/Ackermann_function \n\nAdvice: use only positive integers, most systems have stack protection...but you never know (if you use floats or negatives, boy, you are in for hell)!\n\nIf no result is shown, it´s because your system is protecting the memory stack, if your computer crashes or takes a looooong time, it´s because your stack is unprotected and it is trying to figure out the mess. It can eventualy crash also, lol\n\nThe more RAM you have, more results \n\n")

m = int(input("Choose a positive integer: "))
n = int(input("OK, another one now: "))


def ack(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1, ack(m,n-1))

progress = ProgressBar(widgets=[Percentage(), Bar()], maxval = 500000).start()
progvar = 0

for i in range(500000):
    calc = ack(m,n)
    progress.update(progvar + 1)
    progvar += 1

print("\nAckermanns for {} and {} is: {}".format(m, n, calc))
