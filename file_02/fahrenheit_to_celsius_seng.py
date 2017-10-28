#Author: Bunrith Seng
#File name: celsius_to_fahrenheit_seng.py

#Ex. 4 Fahrenheit to celsius.
#Ask the user to enter the the temperature in Fahrenheit


fahrenheit = float(input("Enter a temperature in Fahreheit: "))

celsius = (fahrenheit - 32) * 5 // 9

print("Temperature converted to Celsius: ", celsius, "degrees")


input ('Press enter to continue')


#Date for the buggy code

#98.6 F
#81.6 C, Incorrect!

#Data after debugged

#98.6 F, 0 F
#37 C, -18.0C
