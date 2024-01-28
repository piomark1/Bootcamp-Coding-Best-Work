#IMPROVED VERSION OF holiday.py program.
#improvements contain:
#    -"if-else" structures in "hotel_cost" and "car_rental"
#    -lowercase, uppercase and extraoridnary cars input "filters"   
#    -better final datas table output   
#
#    -i resigned from "if/else choice" statements in the functions
#    -because i thought that program with database and haversine formula will be   
#    -more intresting and i'll repeat dictionaries, lists, touples, loops... etc.   
#
#
#for better list of choice output
#
#Your task will be to calculate a user's total holiday cost, which includes
#the plane cost, hotel cost, and car-rental cost.
#
#Frist, get the following user inputs:
#
#   "city_flight": The city they will be flying to.
#                  (You can create some options for them. Remember each city will have 
#                   different filght costs.)
#
#   "num_nights": The number of nights they will be staying at a hotel
#                 
#   "rental_days": The number of days for which they will be hiring a car.
#
#   Next, create the following four functions:
#   
#       -hotel_cost: This function will take num_nights as an argument
#                    and return a total cost for the hotel stay 
#                    (you can choose the price per night charged at the hotel).
#       
#       -plane_cost: This function will take city_flight as an argument 
#                    and return a cost for the fligh. (Hint: use if/else if statemnts in
#                    in the function to retrieve a price based on the chosen city.)
#       
#       -car_rental: This function will take rental_days as an argument and return the total cost
#                    of the car rental (you can choose the daily rental cost.)
#
#       -holiday_cost: This function will take the three arguments hotel_cost, plane_cost, car_rental.
#                      Using these three arguments, you can call all of or the above functions with
#                      respective arguments and finally return a total cost for your holiday.   
#
#   Print out all the details about the holiday in a readable way.
#
#   Try running your program with different combinations of input to show
#   its compatibility with different options.
#



import math #math library import (neccessary) for calculating haversine formula

#Database of flight destination cities.
#cities ={'city_name':(latitude, longtitude, {car_name:price}, {hotel_name:({room_clas:price})})} 

cities = {'Berlin':(52.5200, 13.4050, 
                     
                     {'Audi':40.99, 'Volkswagen':46.50 , 'BMW':50.20}, 
                     
                     {'Keizer Hotel':({'President':90.65, 'Business':70.49, 'Economic':40.00}), 
                      'Ludvig Hotel':({'President':100.20, 'Business': 80.49, 'Economic':50.39}), 
                      'Bach Hotel':({'President':120.50, 'Business':100.80, 'Economic':70.45}) }), 
          
          'Moscow': (55.7558, 37.6173, 
                     
                     {'Lada':40.65, 'Patriot':60.55, 'Aurus':70.10},  
                     
                     {'Alexander Hotel':({'President':90.99, 'Business':89.99, 'Economic':59.99}), 
                      'Pushkin Hotel':({'President':110.89, 'Business':90.49, 'Economic':60.20}), 
                      'Tchaikovsky Hotel':({'President':105.55, 'Business':90.76, 'Economic':69.99}) }),
          
          'Helsinki': (60.1699, 24.9384, 
                       
                       {'Saab':40.00, 'Th!nk':50.99, 'Opel':39.99}, 
                       
                       {'Santa Hotel':({'President':90.87, 'Business':80.39, 'Economic':40.50}), 
                        'Suomi Hotel':({'President':100.99, 'Business':90.44, 'Economic':50.00}), 
                        'Moomin Hotel':({'President':110.10, 'Business':100.00 , 'Economic':80.59}) }),
          
          'Stockholm': (59.3293, 18.0686, 
                        
                        {'Volvo':50.12, 'Nevs':48.99, 'Caresto':39.99}, 
                        
                        {'Vasa Hotel':({'President':109.09, 'Business':87.65, 'Economic':56.77}) ,
                         'Pippi Hotel':({'President':104.00, 'Business':89.89, 'Economic':60.50}), 
                         'Emil Hotel':({'President':101.10, 'Business':90.45, 'Economic':58.65 }) }),
          
          'Copenhagen': (55.6761, 12.5683, 
                         
                         {'CityEL':50.00, 'Zenvo':40.00, 'Kuga':30.00  }, 
                         
                         {'Viking Hotel':({'President':100.34, 'Business':90.80, 'Economic':70.05 }) , 
                          'Lego Hotel':({'President':120.20, 'Business':100.10, 'Economic':80.08 }) , 
                          'Andersen Hotel':({'President':140.04,'Business':100.00, 'Economic':60.99}) }),
          
          'Amsterdam': (52.3676, 4.9041, 
                        
                        {'Siluro': 50.65, 'Daffodil':55.49, 'Kalmar':57.70}, 
                        
                        {'Mill Hotel':({'President':108.89,'Business':89.80,'Economic':69.99}), 
                         'Tulip Hotel':({'President':114.41,'Business':97.76,'Economic':71.80}), 
                         'V.Gogh Hotel':({'President':119.85,'Business':90.13,'Economic':70.39}) }),
          
          'Prague': (50.0755, 14.4378, 
                     
                     {'Skoda':40.35, 'MWM':45.49, 'Kaipan':50.05}, 
                     
                     {'Hasek Hotel':({'President':90.10,'Business':80.08,'Economic':60.69}), 
                      'Pepik Hotel':({'President':100.52,'Business':90.63,'Economic':65.95}), 
                      'Svejk Hotel':({'President':110.15,'Business':100.80,'Economic':70.77})}),
          
          'Bratislava': (48.1486, 17.1077, 
                         
                         {'K-1':46.75,'KIA':48.90,'Drndicka':50.20}, 
                         
                         {'Janosik Hotel':({'President':90.54, 'Business':70.43, 'Economic':59.85}),
                          'Tatra Hotel':({'President':107.43, 'Business':89.53, 'Economic':60.87}) ,
                          'Dubcek Hotel':({'President':111.11, 'Business':99.99, 'Economic':78.99}) }),
          
          'Vienna': (48.2082, 16.3719, 
                     
                     {'Denzel':60.15,'Libelle':55.25,'Grofri':45.65}, 
                     
                     {'Mozart Hotel':({'President':115.15, 'Business':95.65, 'Economic':75.25}) ,
                      'Strauss Hotel':({'President':105.35, 'Business':89.85, 'Economic':69.75}) ,
                      'Sisi Hotel':({'President':120.00, 'Business':100.99, 'Economic':80.65}) }),
          
          'Oslo': (59.9139, 10.7522,
                   
                   {'Troll':50.50,'Buddy':60.45,'FYK':55.15},
                   
                   {'Sven Hotel':({'President': 130.45, 'Business':110.75, 'Economic':90.85}),
                    'Viking Hotel':({'President':105.05, 'Business':90.10, 'Economic':70.30}),
                    'Thorgal Hotel':({'President':118.99, 'Business':88.90, 'Economic':69.99}) }),
          
          'Paris': (48.8566, 2.3522, 
                    
                    {'Reanult':60.65,'Peugeot':59.46,'Citroen':49.65},
                    
                    {'Eiffel Hotel':({'President':118.81, 'Business':97.68, 'Economic':70.00}) ,
                     'Versailles Hotel':({'President':130.30, 'Business':99.99, 'Economic':69.80}) ,
                     'Gauloise Hotel':({'president':120.10, 'Busines':80.50, 'Economic':60.50}) }),
          
          'London': (51.5072, -0.1276, 
                     
                     {'Jaguar': 34.56, 'MG': 45.67, 'Bentley': 67.54 }, 
                     
                     {'Royal Hotel':({'President': 176.45, 'Business':100.50, 'Economic':80.40}),
                      'Grand Hotel':({'President': 154.56, 'Business':99.80, 'Economic':84.23}),
                      'Holidayinn':({'President': 156.87, 'Business':101.20, 'Economic':83.25}) }),
          
          'Madrid': (40.4168, -3.7038, 
                     
                     {'SEAT':50.00,'Pegaso':45.00,'Hurtan':40.00}, 
                     
                     {'Toreador Hotel':({'President':100.87, 'Business':84.18, 'Economic':63.95}),
                      'Carmen Hotel':({'President':103.65, 'Business':90.23, 'Economic':70.40}),
                      'Flamenco Hotel':({'President':110.05, 'Business':99.50, 'Economic':76.32}) }),
          
          'Lisbon': (38.7223, -9.1393, 
                     
                     {'Vinci':43.25,'Portaro':50.04,'Sado':39.99}, 
                     
                     {'Magellan Hotel':({'President':104.57, 'Business':85.42, 'Economic':64.89}),
                      'Lusitania Hotel':({'President':131.00, 'Business':100.05, 'Economic':81.33}),
                      'Afonso Hotel':({'President':113.23, 'Business':95.65, 'Economic':73.40}) }),
          
          'Rome': (41.9028, 12.4964, 
                   
                   {'FIAT':54.32, 'Lancia':60.49, 'Ferrari':80.00}, 
                   
                   {'Caesar Hotel':({'President':120.45, 'Business':100.50, 'Economic':79.99}),
                    'Colosseum Hotel':({'President':124.99, 'Business':89.85, 'Economic':68.58}),
                    'Tiber Hotel':({'President':130.67, 'Business':95.55, 'Economic':74.60}) }),
          
          'Athens': (37.9838, 23.7275, 
                     
                     {'Dimitriadis':50.32,'Arco':52.44,'DIM':51.65}, 
                     
                     {'Hercules Hotel':({'President':100.55, 'Business':90.34, 'Economic':80.25}),
                      'Jason Hotel':({'President':115.45, 'Business':100.35, 'Economic':70.34}),
                      'Titan Hotel':({'President':128.63, 'Business':95.43, 'Economic':84.74}) }),
          
          'Budapest': (47.4979, 19.0402, 
                       
                       {'Puli':55.46, 'Csonka':49.49,'Fejes':60.31}, 
                       
                       {'Danube Hotel':({'President':150.45, 'Business':90.40, 'Economic':60.32}),
                        'Magyar Hotel':({'President':136.95, 'Business':89.69, 'Economic':59.57}),
                        'Rakoczi Hotel':({'President':124.39, 'Business':85.14, 'Economic':60.49}) }),
          
          'Bucharest': (44.4268, 26.1025, 
                        
                        {'Dacia':49.85 ,'ARO':51.25,'Lastun':55.00}, 
                        
                        {'Nadia Hotel':({'President':123.45 , 'Business':90.12, 'Economic':70.34}),
                         'Dracula Hotel':({'President':135.67, 'Business':92.45, 'Economic':72.44}),
                         'Constanca Hotel':({'President':148.80, 'Business':91.35, 'Economic':71.33}) }),
          
          'Belgrade': (44.8125, 20.4612, 
                       
                       {'Yugo':50.15, 'Zastava':43.23,'Koral':60.04},
                       
                       {'Milos Hotel':({'President':110.03, 'Business':80.10, 'Economic':60.42}),
                        'Midzor Hotel':({'President':124.86, 'Business':95.24, 'Economic':70.16}),
                        'Galaksija Hotel':({'President':115.64, 'Business':88.90, 'Economic':67.93}) }),
          
          'Istanbul': (41.0082, 28.9784, 
                       
                       {'Devrim':48.99, 'Anadol':50.50, 'Murat':51.25}, 
                       
                       {'Ottoman Hotel':({'President':110.10, 'Business':90.06, 'Economic':74.43}),
                        'Ararat Hotel':({'President':130.24, 'Business':110.49, 'Economic':90.00}),
                        'Bosfor Hotel':({'President':105.31, 'Business':89.15, 'Economic':69.85}) })
          }


DEPARTURE = (52.2297, 21.0122)       #departure starting coridnates for haversine formula
CASK = 0.22976                       #price of seat per km in 0.01$ (Cost of Available Seat Kilometer)   


def hotel_cost(num_nights_input):                       #definition of hotel_cost function, 
                                                        #function takes "num_nights" as arument            
    while True:                                         #and stores in lockal variable "num_nights_input"

        
        hotel_list = list(cities[city_flight][3])

        print("\n\nWhich hotel do You wish for stay?:\n")

        for x in range(0, len(hotel_list)):                 #loop for hotel options list
            
            room_list = list(cities[city_flight][3][hotel_list[x]])
            print(f"\n{hotel_list[x]}:\n")
            
            for y in range(0, len(room_list)):              #loop for room class opiotns list
                
                if y == 0:
                    
                    print(" "*16, f"{room_list[y]}: {cities[city_flight][3][hotel_list[x]][room_list[y]]}$/night", end = " "*4)
                
                else:
                    print(f"{room_list[y]}: {cities[city_flight][3][hotel_list[x]][room_list[y]]}$/night", end = " "*4)

            print("\n")
                
        
        hotel = input("\nEnter hotel name: ")
        hotel = hotel.lower()
        
        if ("hotel" in hotel) == True:              #hotel name filter
                                                    #input: just hotel name(lower or upper cases)
            hotel = hotel.title()
        
        else:
            hotel += " hotel"                       #add " hotel" to entered string with hotel name
            hotel = hotel.title()                   #capitalize first letters of all words    
        
        
        
        if (hotel in hotel_list) == False:     #condition for propper hotel name input
            
            hotel = ""
            continue
        
        else:
            
        
            print(f"\n{hotel}, rooms:\n")                       #rooms output for choosed hotel

            
            room_class_list = list(cities[city_flight][3][hotel])

            for x in range(0, len(room_class_list)):
                
                print(" "*22, f"{room_class_list[x]}: {cities[city_flight][3][hotel][room_class_list[x]]}$/night\n")



            
            while True:
            
                room_class = input(f"What room class do You wish?: ")
                
                room_class = room_class.lower()                          #room class choice filter,                       
                room_class = room_class.capitalize()                     #takes lower, upper and mixed case input   
                
                if (room_class in room_class_list) == False: #condition for propper room class input
                        
                    room_class = ""
                    continue
                
                else:    
                    stay_cost = (cities[city_flight][3][hotel][room_class]) * num_nights_input
                    break    
            break                
    
    return stay_cost            #if inputs were correct return calculated stay_cost


def plane_cost(city_flight_input):      #definition of "plane_cost" function,
                                        #function takes "city_flight" as argument
                                        #and calculates distance between "DEPARTURE" 
                                        #and "city_flight" using geographical coordinates
    
    def degrees_to_radians(degrees):    #auxilary function "degrees_to_radians" inside "plane_cost" function    
                                        #function takes latitudes and longtitudes values as argument    
        radians = degrees * (math.pi/180)
                                            
        return radians
    
    #haversine formula sliced for 3 parts for better readability
    hav_1 = math.sin( degrees_to_radians(cities[city_flight_input][0]) ) * math.sin( degrees_to_radians(DEPARTURE[0]) )
    hav_2 = math.cos( degrees_to_radians(cities[city_flight_input][0]) ) * math.cos( degrees_to_radians(DEPARTURE[0]) )
    hav_3 = ( hav_2 * (math.cos(degrees_to_radians(cities[city_flight_input][1]) - degrees_to_radians(DEPARTURE[1]))) )
    
    distance = 6371 * math.acos( hav_1  + hav_3 )   #distance calculation in "km" by using haversine formula
    cost = CASK * distance                          #cost of flight calculated by multiplying "distance" by CASK value    
    
    return cost     #return of calculated "cost" value of flight             


def car_rental(rental_days_input):      #"car_rental" function, function takes "rental_days" as argument,
                                        #calculates rental cost
                                        #and checks input correctness 
    while True:
        
        
        car_list = list(cities[city_flight][2])
        
        print("\n\nWhat car do You wish?:\n")

        for x in range(0, len(car_list)):   #loop for display car options list 

            if x == 0:
                
                 print(" "*20, f"{car_list[x]}: {cities[city_flight][2][car_list[x]]}$/day", end = " "*4)
            
            else:
                print(f"{car_list[x]}: {cities[city_flight][2][car_list[x]]}$/day", end = " "*4)

        car = input("\n\nEnter car name: ")               #car input filter
        car = car.upper()                                   
                                                           
        if ( car in car_list) == True:          #if BMW, FIAT, MG... etc, 'pass'
            pass
        
        elif car == "TH!NK" or car == "THINK":  #filter for cars "Th!nk" and "CityEL"
            
            car = "Th!nk"
            pass
        
        elif car == "CITYEL":

             car = "CityEL"
             pass       
        
        elif car == "K1":                       #if input was 'k1'

            car = "K-1"
            pass
        
        else: 
            
            car = car.lower()                   #other cars, back to lowercase,
            car = car.capitalize()              #set up first letter capital

        
        if (car in car_list) == False: #condition for propper car name input,
                                                     #if "True" enter car name again but this time propperly   
            car = ""
            continue
        
        else:    
            
            car_hire = cities[city_flight][2][car] * rental_days_input
            break
    
    return car_hire #if input was correct, return calculated rental cost         


def holiday_cost(hotel_cost_return, plane_cost_return, car_rental_return):              #defintion of "holiday_cost" function
                                                                                        #functin takes as arguments values
    holiday_total_cost = hotel_cost_return + plane_cost_return + car_rental_return      #returned by "hotel_cost", "plane_cost"    
                                                                                        #and "car_rental" functions,
                                                                                        #calculates total cost of holiday,        
                                                                                        #doesn't return anything but displays        
                                                                                        #entered values and calculated values
    print("\n"*40)                                                                      #in organised form                
    print("--------------------------------------------------------")                                                                                   
    print("Your holiday cost will be...")                                                                                    
    print("--------------------------------------------------------\n")          
    print("City flight:", f"{city_flight:>15},\tFlight cost: {plane_cost_return:.2f}$\n\n")
    print(f"Days of hotel stay:{num_nights:9},\tHotel cost:  {hotel_cost_return:.2f}$\n\n")
    print(f"Days of car hiring:{rental_days:9},\tHiring cost: {car_rental_return:.2f}$")
    print("---------------------------------------------------------")
    print(f"Total holiday cost:                          {holiday_total_cost:.2f}$\n")
    

    
#--------------------------------------------beginig of main program body--------------------------------------------------------
list_cities = list(cities) #transforms "cities" dictionary for list of keys,  
list_cities.sort()         #every key is a city name, then sorts list
                           #in alphabetical order 

print("\n", "*"*40, "HOLIDAY CALCULATOR!!!", "*"*40)
print("\nWhere would You like to go?:\n")


while True:    
    
    for x in range(1, len(list_cities)):                    #loop for printing cities list

        if (x % 4) != 0:
            print(f"\t\t\t{list_cities[x]:10}", end = " ")

        else:
            print("\n")    

    while True:
        
        city_flight = input("\n\nPlease enter the city name: ") #users choice input into "city_flight"
        
        city_flight = city_flight.lower()
        city_flight = city_flight.capitalize()

        
        if (city_flight in cities) == False:        #input correctness check, if "True", start input again
        
            city_flight = ""
            continue
        
        else:
            break   
    
    while True:
        
        num_nights = input("Please enter the number of nights You will stay at the hotel: ") #hotel nights input
    
        
        if (num_nights.isnumeric()) == False: #if input was wrong, start input again

            num_nights = ""
            continue
    
        else:
            num_nights = int(num_nights)  
            break   
   
   
    while True:
        
        rental_days = input("Plese enter the number of car hiring days: ") #car hiring days input

        if (rental_days.isnumeric()) == False: #if input incorrect, start again

            num_nights = ""
            continue
    
        else:
            rental_days = int(rental_days)
            break



    
    holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days)) 
                                                                                           #call "holiday_cost" function,
                                                                                           #"holiday_cost" function calls 
                                                                                           #"hotel_cost", "plane_cost", 
                                                                                           #"car_rental" functions as arguments,  
                                                                                           #displays details of total holiday cost
                                                                                           #in readable way      
    while True:  #loop with question about check of other holiday options
                 #exits program when answer for user choice is "n" or "N"   
                 #checks correctnes of input, if input is incorrect asks again
                 #until stisfying result   
        choice = input("\nHave You changed Your Mind? Would You like to try other options?(Y/N): ")
        choice = choice.lower()

        if (choice != "y") and (choice !="n"):
            choice = ""
            continue
        else:
            break
    
    if choice == "y":
        continue
    else:
        print("\nHave a nice holiday! Goodbye!!!")    
        break

        
            






