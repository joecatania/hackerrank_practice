#!/bin/python3


def check_num(N):
    #print("N", N)

    if N % 2 == 1:
        #print("N is odd: Weird", N)
        print("Weird")
    elif N >= 2 and N <= 5:
             print("Not Weird")
    elif N >= 6 and N <= 20:
             #print("N is even: Weird", N)
             print("Weird")
    elif N > 20:
             #print("N is even: Not Weird", N)
             print("Not Weird")


N = int(input())

result = check_num(N)
