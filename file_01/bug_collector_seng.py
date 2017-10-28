#Author: Bunrith Seng

#This program is to find
#the total bugs collected

#The program uses:
#--for loop
#--built-in range function
#--running total
#--main
#--Global const

DAY = 7

def main():

    #accumulator variable
    total = 0.0

    #get the bug_number and accumulate them
    for number in range(DAY):
        bug_number = int(input('Number of bugs collected day ' + str(number+1) + ': '))
        total += bug_number 

    #display the total number of bugs collect for 7 days
    print('The total number of bugs collected/week:', total)

    input('Press enter to continue')

#call main function
main()
#tested value
#1,3,10,1,2,2,9
#5,3,1,2,5,7,0
