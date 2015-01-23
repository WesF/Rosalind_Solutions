"""Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s."""


import fileinput
import os
import sys

def count_bases(s):
    bases=[]
    
    for base in ('A','C','G','T'):
        bases.append(s.count(base))
    return bases
    
def main():
    args=[]
    for line in fileinput.input():
        args.append(line.rstrip())
        
    in_ = args[0]
    bases = count_bases(in_)
    print str(bases[0])+' '+str(bases[1])+' '+str(bases[2])+' '+str(bases[3])
    
if __name__ == '__main__':
    main()
    