"""Problem


Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)."""

import fileinput
import os
import sys

def calculate_hamming(s,t):
    dist=0
    for i,c in enumerate(s):
        if t[i]!=c:
            dist+=1
    return dist
    
def main():
    args=[]
    for line in fileinput.input():
        args.append(line.rstrip())
        
    s = args[0]
    t = args[1]
    ans=calculate_hamming(s,t)
    print ans
    
if __name__ == '__main__':
    main()
    