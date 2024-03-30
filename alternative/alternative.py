# Write a program that reads in a string and makes each alternate character
# into an upper case character and each other alternate character a lower case character.
# and each other alternate character a lower case character.
#
# e.g. The string "Hello World" would becom "HeLlO WoRlD"
#
# Now, try starting with the same string but making each alternative word
# lower and upper case.
#
# e.g. The string: "I am learning to code" would become "i AM learning TO code".
#
# Tip: Using the split() and join() functions will help you here

# 1. Input any string You want, index = 0, new_string = ""
# 2. While index < len(the_string)(False) go to 4, (True): 
#
#    *Take index element of the string, index:{0, 1, 2...index}:   
#       -if index % 2 == 0(True): new_string = new_string + the_string[index].upper()
#       -else index % 2 == 0(False): new_string = new_string + the_string[index].lower()
#
# 3. index+=1, go to step 2.
# 4. While index < len(the_string)(False), no loop entry, output new_string, end program.

#============================ALTERNATION EVERY LETTER=======================================

#set up: string input, new_string = empty string, index = 0
the_string = input("Enter any sentence You wish: ") 
index = 0
new_string = ""     #for storing alternated letters                                              

while index < len(the_string):          # index less than the lenght of "the_string" = True, go into the loop, otherwise
                                        # output "new_string", end program

                         
    if index % 2 == 0:                                           #if True, transform "the_string[index]" uppercase, add to "new_string", store in "new_string"
        new_string = new_string + the_string[index].upper()      #"the_string[index] = the_string[index].upper()" generates error
                                                                 #we need new variable "new_string"        
    else:
        new_string = new_string + the_string[index].lower()      #if "index % 2 == 0" is False, tranform "the_string[index]" lowercase,
                                                                 #add to "new_string", store in "new_string"   
    
    index += 1          #index = index + 1            

print(new_string)   #output "new_string" because of no entry to the loop but jump over the loop, end program

#============================ALTERNATION EVERY WORD=============================================

# 1. Input any string You want, transform string into list, index = 0
# 2. While index < len(the_string)(False): go to 4, (True):  
#
#    *Take index element of the list, index:{0, 1, 2...index}:   
#       -if index % 2 == 0(True): the_string[index] = the_string[index].lower()
#       -else index % 2 == 0(False): the_string = the_string[index].upper()
# 
# 3. index+=1, go to step 2.
# 4. While index < len(the_string)(False), no loop entry, transform list the_string into string the_string, 
#     output the_string, end program.


#set up: string input, transform the_string into list "the_string", set index = 0
the_string = input("Enter any sentence You want: ")
the_string = the_string.split()
index = 0

while index < len(the_string):    #while index less than the lenght of the list "the_string", go into the loop

    if index%2 == 0:                                        #if "True", transform index element of the list "lowercase"  
        the_string[index]=the_string[index].lower()         #store in the_string[index]
    
    else:
        the_string[index]=the_string[index].upper()       #else, transform index element of the list "uppercase"  
                                                          #store in the_string[index]  
    
    index += 1                                            #increase index = index + 1, go to begining of the loop  

the_string = " ".join(the_string)                         #if index < len(the_string)(False), don't entry to the loop  
                                                          #transform list "the_string" into the string "the_string" 
                                                          #and store in "the_string"  
print(the_string)   #output "the_string"              


