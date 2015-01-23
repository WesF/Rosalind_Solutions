"""Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order."""

import fileinput
import os
import sys

def convert_dna_to_palindrome(s):
    _list=[]
    rev_list=[]
    base_dict={'A':'T','C':'G','G':'C','T':'A'}
    for base in s[::-1]:
        _list.insert(0,base)
        rev_list.insert(0,base_dict[base])
    return _list,rev_list
    
def find_palindromes(l,m):
    """Looking for all plaindromes between 4 and 12 in length in list
    of 1s and 0s that represent DNA. Most efficient to start from the middle of a possible palindrome
    and check from both directions until the end. Given this, we can start
    this check at position 2 and end at len(s)-2.
    """
    #Keys are positions, values are lengths
    palindrome_dict={}
    for i in range(2,len(l)-1):
        
        length =0
        #this means a possible middle
        if l[i]==m[i+1]:
            while l[i-length]==m[i+1+length]:
                length+=1
                
                if length>=2:
                    palindrome_dict[i-length+2]=(length*2)
                if length >12:
                    break
                try:
                    l[i+1+length]
                except IndexError:
                    break
    return palindrome_dict
            
    
    
def main():
    args=[]
    for line in fileinput.input():
        args.append(line.rstrip())
        
    in_ = args[0]
    _list,rev_list=convert_dna_to_palindrome(in_)
    dict_ = find_palindromes(_list,rev_list)
    for key in sorted(dict_, key=dict_.get):
        print str(key)+' '+str(dict_[key])
    print sorted(dict_, key=dict_.get)
    
if __name__ == '__main__':
    main()
    