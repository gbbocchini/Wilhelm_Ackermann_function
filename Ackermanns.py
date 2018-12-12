import sys

sys.setrecursionlimit(10**9)

list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = [9,8,7,6,5,4,3,2,1,0]

def ack(m,n):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1, ack(m,n-1))

for m,n in zip(list1, list2):
    calc = ack(m,n)
    print("Ackermanns for {} and {} is: {}".format(m, n, calc))
