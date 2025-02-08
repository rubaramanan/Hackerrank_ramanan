#!/bin/python3

import os


# Complete the solve function below.
def solve(s):
    c_words = [word.capitalize() for word in s.split(' ')]
    return ' '.join(c_words)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
