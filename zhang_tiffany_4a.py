cities = int(input('How many cities would you like to enter temperature data for? '))

while cities <= 0:
    print('\nInvalid number, please try again.')
    cities = int(input('How many cities would you like to enter temperature data for? '))

days = int(input('How many days would you like to enter temperature data for? '))

while days <= 0:
    print('\nInvalid number, please try again.')
    days = int(input('How many days would you like to enter temperature data for? '))

print("\nOk, let's begin . . . ")

temp_all_cities = 0
highest_temp = -1000

for i in range(1, cities + 1):
    total_city_temp = 0
    print('- City', i, '-')
    for j in range(1, days + 1):
        temp = int(input('Enter high temperature for day ' + str(j) + ': '))
        total_city_temp += temp
        if temp > highest_temp:
            highest_temp = temp
    avg_temp = total_city_temp / days
    temp_all_cities += avg_temp / cities

    print('Average high temperature:', avg_temp)

print('\nThe average high temperature for all cities was:', format(temp_all_cities, '.2f'))
print('The highest temperature recorded was:', highest_temp)




