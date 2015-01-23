"""Problem

Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s."""


import fileinput
import os
import sys
from collections import OrderedDict

def find_motifs(s,t):
    """Find the starting positions in s that t begins at, where the first character in s is at 1"""
    starts=[]
    n=0
    for i in range(len(s)):
        try:
            if n==0:
                n=s.index(t, 0,len(s))
                starts.append(n+1)
            else:
                n=s.index(t, n+1,len(s))
                starts.append(n+1)
        except ValueError:
            break
            
    return starts #list(OrderedDict.fromkeys(starts))

def main():
    args=[]
    for line in fileinput.input():
        args.append(line.rstrip())
        
    s = args[0]
    t = args[1]
    
    positions = find_motifs(s,t)
    print ' '.join(map(str,positions))
    
if __name__ == '__main__':
    main()
    