"""An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t."""


import fileinput
import os
import sys

def transcribe_dna(s):
    bases=''
    
    for base in s:
        
        if base =='T':
            bases+='U'
        else:
            bases+=base
    return bases
    
def main():
    args=[]
    for line in fileinput.input():
        args.append(line.rstrip())
        
    in_ = args[0]
    bases = transcribe_dna(in_)
    print bases
    
if __name__ == '__main__':
    main()
    