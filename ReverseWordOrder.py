#! /usr/bin/python

"""This programm will revrese your string
author: Sose
useful Links: http://www.doxygen.nl/manual/docblocks.html#pythonblocks"""

def Reverse_string():
##@var reversed_string 
##This is our result
    reversed_string = ""
    input_string = raw_input(" Enter string: ")
    input_list = input_string.split()
    lenght_of_list = len(input_list)-1
    for i in range(lenght_of_list , -1 , -1):
        reversed_string = reversed_string + input_list[i]+ " "
    print ("Output string is: " + reversed_string)

Reverse_string()
