'''
 Write a program that reads in a string and makes each alternate character
 into an upper case character and each other alternate character a lower case character.
 and each other alternate character a lower case character.

 e.g. The string "Hello World" would becom "HeLlO WoRlD"

 Now, try starting with the same string but making each alternative word
 lower and upper case.

 e.g. The string: "I am learning to code" would become "i AM learning TO code".

 Tip: Using the split() and join() functions will help you here
'''                                              
#check is entered string not empty 
while True:

    the_string = input("Enter any sentence You want: ")
        
    if (the_string == ""):
                
        print("Empty string! Try again.")
        continue
    
    else:
        break

#'new_string_list' will allow store every letter of entered string after 'upper', 'lower' transformation
new_string_list = []

#loop which goes through every letter in the entered string
for letter_index in range(0, len(the_string)):          
                                                        
    
    if the_string[letter_index].isalpha() == True:  #is alphabetical? if 'True', check result of 'modulo' operation
        
        
        if letter_index % 2 == 0:   #if 'letter_index' modulo 2 is even transform letter to upper form, 
                                    #if result is odd, transfrom letter to lower form
            new_string_list.append(the_string[letter_index].upper())     
                                                                    
        else:
        
            new_string_list.append(the_string[letter_index].lower())   
                                                                    
    #is 'space'? if 'True' append 'space' to 'new_string_list',
    #if 'no space' and 'no letter' replace mark with empty string          
    elif the_string[letter_index].isspace() == True:
        
            new_string_list.append(the_string[letter_index])

    else:
            new_string_list.append(the_string[letter_index].replace(the_string[letter_index], ""))                     

#when loop went through the string, join all elements of the list,
#display transformed string
new_string_list = "".join(new_string_list)

print("\n%s" %(new_string_list))   

#transfrom 'new_string_list' into list of words
new_string_list = new_string_list.split()


#loop through every 'item_index' in the 'new_string_list'
#if 'item_index' modulo 2 is even transform 'new_string_list[item_index]' to lower form,
#if result of modulo operation is odd transform 'new_string_list[item_index] to upper form 
for item_index in range (0, len(new_string_list)):

    if item_index % 2 == 0:                                           
        
        new_string_list[item_index] = new_string_list[item_index].lower()        
    
    else:
        new_string_list[item_index] = new_string_list[item_index].upper()         
                                                            
    
#when loop went through the list, join all elements in one string,
#display transformed string
new_string_list = " ".join(new_string_list)                           
                                                          
                                                            
print("\n%s\n" %(new_string_list))           


