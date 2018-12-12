import time
import sys

sys.setrecursionlimit(4096*10)


print("\nWelcome to the Ackmermann function! History: https://en.wikipedia.org/wiki/Ackermann_function \n\nAdvice: use only positive integers, most systems have stack protection...but you never know (if you use floats or negatives, boy, you are in for hell)!\n\nIf no result is shown, it´s because your system is protecting the memory stack, if your computer crashes or takes a looooong time, it´s because your stack is unprotected and it is trying to figure out the mess. It can eventualy crash also, lol\n\nThe more RAM you have, more results you will see!\n\n")

m = int(input("Choose a positive integer: "))
n = int(input("OK, another one now: "))


def ack(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1, ack(m,n-1))

animation = "."
for i in range(5):
    time.sleep(1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
    print("Calculating")

print("Ackermanns for {} and {} is: {}".format(m, n, ack(m,n)))
