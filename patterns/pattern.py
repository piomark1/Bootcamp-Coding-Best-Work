# Write code to output the star pattern shown below, using an "if-else"
# statement in combintation with a single "for" loop(it's really easy with two,
# but using only one takes a little more thought!):
#
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

counter = 0             #initialisation "counter" variable which will be necessary in
                        #decreasing number of printed stars

for i in range(1, 10):  #"for" loop which need 9 repeats for printing 9 rows
                        # from "i=1" to "i=9"
    
    if i <=5:           #up to 5th row, number of stars increases  
        print("*"*i)    #and covers with "i" value   
        
    else:
     counter += 2           #from row 6th we have to decrease number of printed stars
     print("*"*(i-counter)) #"i=6" we need 4 so, we can decrease "i" by 2 with "counter"
                            # which increases about 2 with every repeat of loop 
                            # i=6   counter=2   i-counter=4 stars_output= ****
                            # i=7   counter=4   i-counter=3 stars_output= *** 
                            # i=8   counter=6   i-counter=2 stars_output= **
                            # i=9   counter=8   i-counter=1 stars_output= *
                            # i=10 for loop exit
     
###########################################################################################################################
     number=int(input("Enter a number:"))
     temp=number

     rev=0

     while number > 0:

        modulus_of_number=number % 10
        print(modulus_of_number)
        rev=rev*10 + modulus_of_number
        print(rev)

        number=number//10
        print(number)

        print("...................................")

    if temp==rev:
       print("The number is a palindrom.")
    else:
       print("Not a palindrome")     
