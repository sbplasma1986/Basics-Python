# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 08:20:56 2022

@author: Suresh BASNET
"""


# Data structure:
    
A=[]               # To create empty list
# print(A) type(A)
#================

A=[1.0, 2, 3.0, 4, 5.0, 6, 7.0, 8, 9.0] # Create a list with characters.
#type(A[0]),type(A[1])
#===========================================

# Indexing the characters in the list A

# A[0], A[1], A[-1] A[-2]

# To find the length of list A
 
# len(A) 

#=========================================
# To add the characters in the list A

# A.append(10)

#=========================================
# To find the sum of all the characters in the list A

# A1=sum(A)
# A.append(sum(A)) # If you want to add this sum in the list
#==========================================

#Find the maximum and minimum character's value in the list A

#max(A),   min(A),    type(max(A)) 

#==========================================
# Create the new list B consists of integer, float, string and Boolean

B=[10, 20, 30, 40, 50, 60.01, "Suresh", True, False] 

# To find the type of characters in the list B

# type(B[-1]),  type(B[0]), type(B[-3]), type(B[-4])

#==============================================

#To create the list inside the list
C=[[1,2],[1.0,2.0],[0.5,1.5,2.5]]
# C[0][1], C[1][0],type(C[1][0]),type(C[1]) 

#===============================================
# Suppose you have two lists and to add the characters of the lists. 
# That means (Simply accumulated the characters in a list). 

C1=[10, 20, 30, 40, 50, 60, 70, 70]; C2=[5, 15, 25, 35, 45, 55,
                                         65, 75, 10, 20, 80]
C3=C1+C2

# To add the characters in a desired position.

#C1.insert(7,90)
#C1.insert(0,"Basnet")

#To remove the desired character from the list.

#C1.remove("Basnet")
# To remove character from the desired index.
#C1.pop(-1)

#================================Replace the word from string

C4 = 'Suresh'
C5 = C4.replace('S','B')

C6 = str.upper('Suresh') #Changing the string into upper case.

C7 = str.lower('SURESH') #Changing the string into lower case.

#==============Splitting the string into the list.

C8 = 'Suresh Basnet live in Uralbari-04 Morang'
C9 = C8.split() 
len(C9)
len(C8)

First_Name = C9[0]
Family_Name = C9[1]
City = C9[4]
Ward_No = C9[5]
District = C9[-1]

#================Creating empty string

C10 = ' My research interest is plasma physics '

C11 = C10.split(' ')

#==================Using another feature of split is maxsplit.
C12 = 'Suresh, Basnet, live, in, Urlabari-04, Morang'
C13 = C12.split(' ', maxsplit=4)

#=========Join function

C14 = ' '.join(C9)

#===============================================
# Suppose you have large number of data and want to arrange them in 
# increasing or decreasing order.
# Again create new list

D=[70, 75, 80, 90, 85, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 95]

#To arrange the characters in index increasing (Ascending) order

#D.sort()

# To arrange the characters in index decreasing (descending) order

#D.reverse()

# Another way to create the list (that we called List Comprehension method)

E1=[i for i in range(20)] # Excluding 20 and inclusion 0

E2 = [i for i in range(0,20,2)]

E3 = [i for i in range(0,20)]

# List of characters divisible by 3.

F1=[k for k in range(20) if k%3==0]

F2=[j for j in range(20) if j%2==1]

#===========================================
# Making the list by pulling random integer using random library of python.
import random as random         # Call the random library

# 1st learn how we can select a random integer

F3=random.randint(1,10) # Here both 1 and 10 are inclusive.

F4=random.random()      # Creating random float number less than 1.0.

#=====If you want to add these two random numbers
F5=F3+F4

#===========Control the decimal value of the real number
F6=round(F5,2)

# Another way to control the decimal value of the real number.
F7="{:.2f}".format(F5)

#=========Now making the list from random number.

G=[random.randint(1,10) for i in range(20)]

#========================================
# To count the frequency of character in the created random list
# For this, you have again call the library of python collections
import collections as collection  # Call the library of python
G1=collection.Counter(G)

#=========================================
# Count of character (string) in the list
H1=[random.choice(['S','U','R','E','S','H']) for k in range(15)]
# type(H1[-1])
H2=collection.Counter(H1)

# You want make a count the particular string
H3=H1.count('S')
H4=H1.count('U') 
#============================ Thank you and see you soon.


