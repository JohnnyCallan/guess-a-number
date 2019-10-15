# create a cypher that shifts the ansii value of text by many places
import random

user_input = input("please input your string \n")
encripted = ""
uncyphered = ""
saved_random = ""
increment = 0

for i in user_input:
    random_number = random.randint(0,9)
    saved_random += str(random_number)
    print("{0} letter {1} ordenance, encripted letter {2}".format(i, ord(i), chr(ord(i) + random_number)))
    encripted += chr(ord(i) + random_number)
print(saved_random)
print(encripted)

for i in encripted:
    working_number = int(saved_random[increment])
    increment += 1
#    print("{0} letter {1} ordenace, uncyphered value {2}".format(i, ord(i), chr(ord(i) - working_number)))
    uncyphered += chr(ord(i) - int(working_number))
print()
print(uncyphered)
