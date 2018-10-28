#!/bin/python3


def check_num(N):
    print("N", N)

    if N % 2 == 1:
        print("N is odd: Weird", N)
    elif N >= 2 and N <= 5:
             print("N is even: Not Weird", N)


N = int(input())

result = check_num(N)
