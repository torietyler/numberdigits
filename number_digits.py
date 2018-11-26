'''
Find the number of digits in a given integer
'''

num = int(input("Enter the number  :")) # enter the number using keyboard

div = 1 # start with 1 the first power 0f 10 in the integer division
while num// 10**div != 0: # Check the condition: is the quotient of the
                          # integer division num divided by 10 to the power of div
    div = div + 1         # not equal to zero
                          # if yes execute the loop body
print("the number :", num, "has ", div, "digits") # if no, get out of the loop and print
                                                  # the message