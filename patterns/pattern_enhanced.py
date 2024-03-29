# Enhanced version of Task program.
# Program asks about odd (for even input pattern doesn't egsit) input and then and outputs entered character in pattern.

counter_decreaser = 0               # will decrase number of character output when counter will increase                          

pattern = input("Please enter something: ")                 #character for output in pattern

while True:                 
    
    iterations = int(input("Enter odd number of rows: "))    #even/odd input check loop   
    if (iterations%2) == 1:
        break
    else:
        iterations = 0
        continue

print("\nPattern output:\n")                                    

for counter in range(iterations):                               #pattern output loop                                 
                                                                    
    if counter <= (iterations/2):                               #have we reached middle of pattern?
        
        counter += 1                                            #if "no" output characters increasingly
        print(pattern * counter)
    
    else:
        
        counter -= 1
        print(pattern * (counter - counter_decreaser))          #if middle of pattern is reached
                                                                #start output characters decreasingly
        counter_decreaser += 2





        

