import numpy as np


def degree_seq(A, n):
    A.sort(reverse=True)

    while True:
        
        if all(v == 0 for v in A):
            return True

        if A[0] < 0 or A[0] >= n or np.sum(A) < 0:
            return False

        i = 1
        while i <= A[0]:
            A[i] = A[i] - 1
            i = i + 1

        A[0] = 0
        A.sort(reverse=True)


test = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
test2 = [4, 4, 3, 1, 2]
print(degree_seq(test, 11))
print(degree_seq(test2, 5))
