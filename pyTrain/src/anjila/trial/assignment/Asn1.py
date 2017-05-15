'''
Created on May 14, 2017

@author: rujina
'''
'''
select any 6 columns out of the columns inside csv file attached to this email and write it in other csv files 
with the same column names.(do not select adjacent coloumns)
'''
# with open('write.csv', 'wb') as csv_write_file:
#     writer=csv.writer(csv_write_file)
#     with open('FL_insurance_sample.csv','rb') as csv_data:
#         read_data=csv.reader(csv_data)
#         for rowdata in read_data:
#             writer.writerow([rowdata[0], rowdata[2], rowdata[4], rowdata[6], rowdata[8], rowdata[10]])
'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in 
the sentence capitalized. 
Suppose the following input is supplied to the program:
Hello world s
Practice makes perfect 
Then, the output should be: 
HELLO WORLD 
PRACTICE MAKES PERFECT 
'''
# print "Enter/Paste your content. Ctrl-D to save it."
# contents = ""
# 
# while True:
#     line = raw_input("")
#     if(line==""):
#         break
#     contents=contents+"\n"+line
# print contents.upper()
'''
3)-Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, 
then the function should print all strings line by line.
'''

# no_of_lines = 2
# lines = []
# for i in xrange(no_of_lines):
#     lines.append(raw_input())
# maxLineLen = max(lines, key=len)
# for st in lines:
#     if(len(st) == len(maxLineLen)):
#         print st

'''
4)-With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all
 duplicate values with original order reserved.
'''
# t=[12,24,35,24,88,120,155,88,120,155]
# list_suplicateRemoved=list(set(t))
# print list_suplicateRemoved
# list_suplicateRemoved.reverse()
# print list_suplicateRemoved

'''
5)- create html page consisting of all points of the course from w3schools.
'''
