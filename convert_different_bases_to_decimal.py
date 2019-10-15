# convert any base number to a base 10

input_number = input("please enter number to be converted to decimal: ")
base = input("please enter the base we are working with, keep below base 16: ")
base = int(base)
#1101

holding_value = 0
decimal_value = 0
powers = len(input_number) - 1

for i in range(0, len(input_number)):
    if input_number[i] in "0123456789ABCDEF":

        working_number = input_number[i]

        if input_number[i] == "A":
            working_number = 10
        elif input_number[i] == "B":
            working_number = "11"
        elif input_number[i] == "C":
            working_number = 12
        elif input_number[i] == "D":
            working_number = 13
        elif input_number[i] == "E":
            working_number = 14
        elif input_number[i] == "F":
            working_number = 15

        working_number = int(working_number)

        if working_number < base:
            holding_value = (base ** powers) * working_number
            decimal_value += holding_value
            powers -= 1
        else:
            print("number entered not in base system")
            break

if powers == -1:
    print(decimal_value)



