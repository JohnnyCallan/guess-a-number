# create a cypher that shifts the ansii value of text by many places

user_input = input("please input your string ")
print()

encripted = ""
uncyphered = ""

for i in user_input:
    print("{0} letter {1} ordenance, encripted letter {2}".format(i, ord(i), chr(ord(i)+1)))
    encripted += chr(ord(i) + 1)

print()
print(encripted)
print()

for i in encripted:
    print("{0} letter {1} ordenace, uncyphered value {2}".format(i, ord(i), chr(ord(i)-1)))
    uncyphered += chr(ord(i)-1)
print()
print(uncyphered)