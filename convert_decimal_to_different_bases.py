# convert a base 10 number to a different base of users choice
# number entered has to be above 0

number = input("please enter a positive integer: ")
int_number = int(number)
base = input("choose a base of 16 or less to convert to: ")
base = int(base)

if 0 < base < 17:

    remainder = ""
    binary = ""

    while int_number > 0:
        remainder = int_number % base

        if remainder >= base:
            remainder = (remainder - base) + 10

        if remainder > 9:
            if remainder == 10:
                remainder = "A"
            elif remainder == 11:
                remainder = "B"
            elif remainder == 12:
                remainder = "C"
            elif remainder == 13:
                remainder = "D"
            elif remainder == 14:
                remainder = "E"
            elif remainder == 15:
                remainder = "F"

# add binary to the string to avoid having to reverse splice, do not use +=

        binary = str(remainder) + binary
        int_number //= base

    print("{0} in base decimal is {1} in base {2} ".format(number, binary, base))

elif number == 0:
    print("it is 0")

else:
    print("cannot achieve this operation please use positive integer next time with a base of less than 16")
