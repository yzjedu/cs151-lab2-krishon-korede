## Programmers: Krishon, Rayan, Megan, and Korede
# Course: CS151, Professor Zee
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement:  Create a program that will determine the expected population in the future /
# (a certain number of years away) for a country based on a current population amount if you are given (1)/
# how often someone is born (in seconds), how often someone dies (in seconds), and (3) how often a new immigrant/
# joins the country (in seconds).
#The purpose of the program is to give the population change when the user enters 5 values.
#Data In: Code needs inputs of seconds between births, seconds between deaths, seconds between immigration,/
#current population size, and number of years in the future
#Data Out: Code outputs population change (for fun!) and future population

# User should be prompted to enter in five inputs: seconds between births, seconds between deaths,/
# seconds between immigration current population size, and number of years in the future.

sec_year = 31536000
print('How many seconds between births?')
secs_births = float(input())
print('How many seconds between deaths?')
secs_deaths = float(input())
print('How many seconds between immigration?')
secs_immigration = float(input())
print('What is the current population size?')
current_population_size = int(input())
print('How many years in the future?')
num_years = float(input())

# Code should calculate population change and print it.

pop_change = ((sec_year/secs_births + sec_year/secs_immigration - sec_year/secs_deaths) * num_years)
print('Population changed by', pop_change, 'people')

# Code should calculate future population and print it.

future_pop = (current_population_size + pop_change)
print('The future population is', int(future_pop))

# Code should use "if" statement to compare results of/
# population change and future calculation to output various statements

if future_pop > current_population_size:
    print('Your current population increased!')
elif future_pop < current_population_size:
    print('Your current population decreased!')
else:
    print('Your current population same!')