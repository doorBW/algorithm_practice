#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(note) > len(magazine):
        print("No")
        return
    elif len(note) == len(magazine):
        note = list(sorted(note))
        magazine = list(sorted(magazine))
        for idx in range(len(note)):
            if note[idx] != magazine[idx]:
                print("No")
                return
        print("Yes")
        return

    for word in note:
        if word in magazine:
            magazine.remove(word)
        else:
            print("No")
            return
    print("Yes")
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

