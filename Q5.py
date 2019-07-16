'''QUESTION NO 5 : 
Create a function that takes two strings as arguments 
and return either True or False depending on
whether the total number of characters in the first string
is equal to the total number of characters in the second string'''

def string1(str):
    str1=input("Enter string 1: ")
    str2=input("Enter string 2: ")
    length_str1=print(len(str1))
    length_str2=print(len(str2))
    if len(str1) == len(str2):
        print(True)
    else:
        print(False)
string1(str)