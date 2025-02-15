"""
Illustrates nested Loop Join in SQL
cs3200 Database design
https://northeastern-datalab.github.io/cs3200/
CS 7240 Principles of scalable data management
https://northeastern-datalab.github.io/cs7240/
First version: 3/23/2015
This version (updated to Python 3): 2/14/2025
"""


print("--- 1st nested loop ---")
for i in range(2):
    for j in range(3):
        for k in range(2):
            print("i=%d, j=%d, k=%d: " % (i, j, k))
            if i == j or i == k:
                print("TRUE")
            print

print("\n--- 2nd nested loop ---")
for i in range(2):
    for j in range(3):
        for k in range(1):
            print("i=%d, j=%d, k=%d: " % (i, j, k))
            if i == j or i == k:
                print("TRUE")
            print

print("\n--- 3rd nested loop ---")
for i in range(2):
    for j in range(3):
        for k in range(0):
            print("i=%d, j=%d, k=%d: " % (i, j, k))
            if i == j or i == k:
                print("TRUE")
            print

