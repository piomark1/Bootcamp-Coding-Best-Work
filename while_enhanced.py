# This is enhanced version of Task program.
# Program takes only numerical datas, both integer and float and displays Error when input is wrong,
# without strings methods.

# If everything is correct, at the the end displays average value of all entered numbers

number = counter = index = ch_in_index = dot = 0
status = ""

print("\n\t\t", "*"*10, "This is enhanced version of Task program", "*"*10)
print("Program takes only numerical datas, both integer and float and displays Error when input is wrong")

while True:

# start of data entry block:
    status =input("\nPlease enter a number(-1 exit program): ")          
    
    if status == "":        #pass if input is "enter"
        continue
    else:
        while index < (len(status)) and status != "-1":            #end of string? if no, enter to the loop

            if status[index] == str(ch_in_index):   #is numerical? if 'yes' take another character
                                                    #and start checking what it is from "0"    
                index += 1
                ch_in_index = 0                     #character in index    
                continue
            
            elif status[index] == ".":              #if "." was entered check the position and number of "."     
                    if status[0] == "." or status[-1] == ".": 

                        print("\nWrong input!")    
                        status = ""
                        index = 0
                        ch_in_index = 0
                        break
                    
                    elif dot == 0:                  
                        
                        dot += 1               #if position of "." is correct and there is only 1 "." 
                        index +=1              #continue program 
                        ch_in_index = 0
                        continue
                    
                    else: 

                        print("\nWrong input!")         #if not, clear everything and start input again
                        status = ""
                        dot = 0
                        index = 0
                        ch_in_index = 0
                        break

            elif ch_in_index <= 9:                # if character entered is above "9" this is not number
                                                  # then set everything at "0" and start input again  
                ch_in_index += 1                   
                continue                               
                                               
            else:
                print("\n Wrong input!")
                index = 0
                ch_in_index = 0
                status = ""
                break        
                
# output block:                
 
    if status == "":            #if some input error occured, start input again
        continue            
        
    elif status == "0":         #if was entered only "0", clear everything and and start input again
        
        status = ""
        index = 0
        ch_in_index = 0
        continue    
    
    elif status != "-1":                      #casts input and sums with other inputs,  
                                              #counts number of inputs and clear everything  
        status = float(status)                #for another input  
        number = number + status
        counter += 1
            
        status =""
        index = 0
        ch_in_index = 0
        continue
    
    elif counter == 0:                        #if was entered "-1" and was entered as first,
                                              #exit with exit message   
        print("\nProgram exit without any input. Thank You.")
        break
    
    else:
                                               #exit and output of average of entered values when "-1"                     
                                               #wasn't entered first     
        print(f"\nThe average value of entered numbers is: {number/counter:.2f}")
        print("Thank You.")
        break

