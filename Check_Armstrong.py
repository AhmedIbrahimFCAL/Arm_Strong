# Author: Ahmad Ibrahim Ahmad Mohammed
# Under the supervision of the assistant professor: Dr. Mohammed_El_Ramly

# The Function Definition.
# This functuin check the input
def check_number(num):
    if num=="":
        print("Please, don't leave it empty.")
        return True
    for i in num:
        if i!="0" and i!="1" and i!="2" and i!="3" and i!="4" and i!="5" and i!="6" and i!="7" and i!="8" and i!="9":
            print("This", num, "does not fit to be a positive number. Because, the positive integer number don't include '"+i+"'.")
            return True

# The main program
# print the using way
print("\nA positive integer of 3 digits is called an Armstrong number\n\
if the sum of a cubes of individual digits of the number is equal to that number.")
# read the number from the user
num = input("\nPlease, enter a positive integer number: ").strip()
while check_number(num):
    num = input("Your input isn't valid.\nPlease, enter a positive integer number: ").strip()
rep = len(num)
number = 0
# Check Arm Strong or not by passing each digit power difits number
for i in range(len(num)):
    number+=(int(num[i])**rep)
if number == int(num):
    print(f"\nThe number {num} is Armstrong.\n\nThanks for using my program. See You Soon!")
else:
    print(f"\nThe number {num} is not Armstrong.\n\nThanks for using my program. See You Soon!")
# Thanks for reading my code. See You Soon!