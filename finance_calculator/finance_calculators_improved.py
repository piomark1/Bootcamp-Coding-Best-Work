#Improved version of finance_calculators.py
#Improvements include removal of all data type processing functions from print() function 
#and adding few extra comments 

# At the top of the file include the line: "import math"
# Write the code that will do the following:
# 1. The user shoud be allowed to choose which calculation they want to do.
#   The first output that the user sees when the program runs sould look like
#   this:
#                                                                               
#   __________________________________________________________________________________                                                                        
#  | investment - to calculate the amount of interest you'll earn on your investemnt  |                                                                             
#  | bond       - to calculate the amonut you'll have to pay on a home loan           |                                                                
#  |                                                                                  |  
#  |                                                                                  |  
#  | Enter either 'investment' or 'bond' form the menu above to proceed:              |                                                              
#  |__________________________________________________________________________________|
#
#
# 2. How the user capitalises their selection should not affect how the program
#   proceeds. i.e. 'Bond', 'bond', 'BOND' or 'investment', 'Investment',
#   'INVESTMENT', etc., should all be recognised as valid entries. If the use
#   doesn't type in a valid input, show an appropriate error message.   
#----------------------------------------------------------------------------------------------
# 3. If the user selects 'investment', do the following:
#   *Askt the user to input:
#       -The amount of money that they are depositing.
#       -The interest rate (as a percentage). Only the number of the interest
#        rate should be entered - don't worry about having to deal with the
#        added '%', e.g. The user should enter 8 and not 8%.
#       -The number of years te plan on investing.
#       -Then ask the user to input if they want "simple" or "compound" interest,
#        and store this in a variable called interest. Depending on whether or not
#        they typed "simple" or "compound", output the appropriate amount that they
#        will get back after the given period, at the specified interest rate.
#        See below for the formula to be used:
# ______________________________________________________________________________________
# Interest formula:
#
# The total amount when "simple interest" is applied is calculated as
# follows: A = P(1 +r x t)
# The Python equivalent is very similar: A = P*(1 + r*t)
#
# The total amont when "compound interest" is applied is calculated as
# follows: A = P(1 + r)^t
# The Python equivalent is slightly different: A = P * math.pow((1+r), t)
#
# In the formulae above:
#    * 'r' is the interest entered above divided by 100, e.g. if 8% is entered,
#      then r is 0.08.
#    * 'P' is the amount that the user deposits.
#    * 't' is the number of years that the money is being invested.
#    * 'A' is the total amount once the interest has ben applied.
# ______________________________________________________________________________________
#
# *Print out the answer!
# *Try entering 20 years and 8 (%) and see what the difference is depending on
#  the type of interest rate!
#-----------------------------------------------------------------------------------------
# 4. If the user selects 'bond', do the following:
#  *  Ask the user to input:
#       - The present value of the house. e.g. 100000
#       - The interest rate. e.g. 7
#       - The number of months they plan to take to repay the bond. e.g. 120
#_____________________________________________________________________________
# Bond repayment formula:
# The amount that a person will have to be repaid on a home loan each
# month is calculated as follows: repayment = (i x P)/1-(1+i)^-n
#                                           
# The Python equivalent is slightly different:
# repayment = (i * P)/(1-(1 + i)**(-n))
# In the formula above:
#   * 'P' is the present value of the house.
#   * 'i' is the monthly interest rate, calculated by dividing the annual
#     interest rate by 12. Remember to divide the interest entered by
#   * 'n' is the number of months over which the bond will be repaid.
#_____________________________________________________________________________
# *Calculate how much money the user will have to repay each month
#  and output the answer.                                                                      


import math #import "math" library for "math.pow()" funcion



#welcome message:
print('''\n         *********************** WELCOME IN PANAMA-SWISS BANK LTD! ***********************\n
         **************** BELOW YOU'LL FIND SERVICES WE ALREADY OFFER, *******************\n
         *************** JUST SIMPLE TYPE FROM THE LIST WHAT YOU WISH! *******************''')

wish=input("\n\nWould You like to try our service? Please enter 'Y' or 'N': ") #"wish" var. necessary for loop entry 
wish=wish.lower()

while (wish == "y"):            #thanks this loop we'll be able to try other services as much as we wish
                                #after entering other value than "y", there be no loop entry or loop will be left 

    print('''\n\n\t  investment - to calculate the amount of interest you'll earn on your investment  
          bond       - to calculate the amont you'll have to py on a home loan\n''') #bank service "choice menu"


    choice=input("\t  Enter either 'investment' or 'bond' from the menu above to proceed: ") 
    choice=choice.lower()
    choice=choice.strip()

    while (choice !="investment") and (choice != "bond"): #loop for propper choice check
        print("\n\t\tSorry wrong input ;(")

        choice=input("\t  Enter either 'investment' or 'bond' from the menu above to proceed: ")
        choice=choice.lower()
        choice=choice.strip()
    
    #investment service block where we enter: 
    # "money_deposit"-how much money we wish to invest    
    # "i_rate"-interest rate we wish for our invested money
    # "years" - time how long we wish investing our money
    
    if choice == "investment":                                                
     
        money_deposit=float(input("\n\t  How much would You like to deposit? Please enter: ")) 

        i_rate=input("\n\t  What interest rate You wish? Please enter: ")
        i_rate=(float(i_rate.replace("%","")))/100 #if user entered "%"

        years=int(input("\n\t  For how many years? Please enter: "))
    
        i_choice=input("\n\t  Type which interest You wish, 'simple' or 'compound': ") #type of investment "simple" or "compound"
        i_choice=i_choice.lower()
        i_choice=i_choice.strip()    
    
        while (i_choice != "simple") and (i_choice != "compound"): #another loop for propper input checking
            print("\n\t\tSorry, wrong input ;(")
            
            i_choice=input("\n\t  Type which interest You wish, 'simple' or 'compound': ")
            i_choice=i_choice.lower()
            i_choice=i_choice.strip() 
        #if input is right we can calculate according to our choice
        if i_choice == "simple":
            #simple interest calculation and output
            simple=money_deposit*(1 + (i_rate*years) )
            simple=round(simple, 2) #round "simple" up to second digit after decimal dot
            
            print(f"\n\t  Your simple interest after {years} years with rate {i_rate} will be: {simple}\n\n")
            
        #compound interest calculation and output
        else:
            compound=money_deposit*math.pow((1 + i_rate), years)
            compound=round(compound, 2) #round "compound" up to second digit after decimal dot
            
            print(f"\n\t  Compound interest of Your deposit after {years} years will be: {compound}")
                
    else:
        #bond service section:
        #"house_value"-here we put how much is worth our house
        #"i_rate"-bond interest rate we wish for monthly payments
        #"months"-time how many months we wish to pay our bond
        house_value=float(input("\n\t  Please enter the present value of the house. e.g. '100000': "))

        i_rate=input("\n\t  Please enter the interest rate: ")
        i_rate=(float(i_rate.replace("%", "" )))/100

        months=int(input("\n\t  Enter the number of months You plan to take to repay the bond. e.g. '120': "))

        repayment=(i_rate * house_value)/(1-(1 + i_rate)**(-months)) #calculatd bond
        repayment=round(repayment, 2) #round repayment up second digit after decimal dot
        #our monthly bond outpu
        print(f"\n\t  Your bond with your house value:{house_value} in time range {months} months will be {repayment} monthly")

    wish=input("\n\nDo you wish to try other service? Please enter 'Y' or 'N': ") #conditional question for trying other services.
    wish=wish.lower()                                                             #answer other than "y" will result with loop exit          

