# Portfolio Project 1
# rover.py
# Program for calculating the time it takes a rover to travel depending on rover parameters and storm status.
# DANIEL EDGAR

import math

rover_num = int(input('Which rover would you like to move? ')) # getting which rover is wanted for the mission
distance = int(input('How far is the mission in km? ')) # getting the distance of the mission
storm = input('Is there a storm in the forecast (True or False)? ') # getting if there is a storm on the way to the destination

# depending on which rover is selected, assign the constants with the values of the selected rover.
if rover_num == 1:
    battery = 100 # in kWh
    efficiency_of_battery = 50 / 100 # in kWh per km
    solar_capacity = 5 # in kWh
    velocity = 5 # in km per hour

elif rover_num == 2:
    battery = 130 # in kWh
    efficiency_of_battery = 40 / 100 # in kWh per km
    solar_capacity = 8 # in kWh
    velocity = 4 # in km per hour

elif rover_num == 3:
    battery = 80 # in kWh
    efficiency_of_battery = 30 / 100 # in kWh per km
    solar_capacity = 4 # in kWh
    velocity = 6 # in km per hour

else: # if rover_num isn't 1, 2, or 3 then the program ends because the rover_num is not valid and prints out a statement why it ended
    print('Rover number not recognized.')
    exit()

num_charges = math.ceil(distance / (battery / efficiency_of_battery)) - 1 
# calculations for how many times the rover needs to charge
# num_charges might be a decimal, so round up then subtract 1 because the rover starts with 1 charge

charge_time = num_charges * (battery / solar_capacity) # time spent charging
drive_time = distance / velocity # time spent driving to the destination
total_time = charge_time + drive_time # total time is the charge_time added to drive_time

if storm == 'True': # if there is a storm, multiply the total time by 1.2, otherwise leave the value as is
    total_time *= 1.2

print("The total travel time for Rover {0} to travel {1:0.1f} km is {2:0.1f} hours.".format(rover_num, distance, total_time))
