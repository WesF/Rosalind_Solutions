"""Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s."""

import fileinput
import os
import sys

def rev_transcribe_dna(s):
    bases=''
    base_dict={'A':'T','C':'G','G':'C','T':'A'}
    for base in s[::-1]:
        bases+=base_dict[base]
        
        
    return bases
    

    
def main():
    args=[]
    for line in fileinput.input():
        args.append(line.rstrip())
        
    in_ = args[0]
    bases = rev_transcribe_dna(in_)
    print bases
    
if __name__ == '__main__':
    main()
    