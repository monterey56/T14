#collect the input city_flight for which city the user is flying to, 
#collect the input num_nights for the number of nights they're staying at a hotel, 
#collect the input rental_days for the number of days they will be hiring a car
#create the function hotel_cost that will use num_nights to calculate the total cost of the hotel stay (user can input price per night)
#create the function plane_cost that will use city_flight to calculate the cost of the flight (use if/else statements to retrieve a price based on the chosen city)
#create the function car_rental that will take rental_days and calculate the total cost of the car rental (user can input rental cost)
#create the function holiday_cost that will add hotel_cost, plane_cost and car_rental to calculate the final cost of the holiday

def hotel_cost(num_nights, price_per_night):
    return num_nights * price_per_night

def plane_cost(city_flight):
    if city_flight == "London":
        return 200
    elif city_flight == "Cardiff":
        return 250
    elif city_flight == "Edinburgh":
        return 300
    elif city_flight == "Belfast":
        return 350
    else:
        return None

def car_rental(rental_days, rental_cost_per_day):
    return rental_days * rental_cost_per_day

def holiday_cost(city_flight, num_nights, price_per_night, rental_days, rental_cost_per_day):
    total_cost = hotel_cost(num_nights, price_per_night) + plane_cost(city_flight) + car_rental(rental_days, rental_cost_per_day)
    return total_cost

print("Select the city you are flying to.")
city_flight = input("Your choices are London, Cardiff, Edinburgh and Belfast: ")
num_nights = int(input("Enter the number of nights you are staying at a hotel: "))
price_per_night = float(input("Enter the price per night of the hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car: "))
rental_cost_per_day = float(input("Enter the rental cost per day: "))

total_cost = holiday_cost(city_flight, num_nights, price_per_night, rental_days, rental_cost_per_day)
result = f"""
You will be flying to {city_flight}
You will be staying for {num_nights} nights.
You will be hiring a car for {rental_days} days.
The total cost of your trip is £{total_cost}
"""
print(result)