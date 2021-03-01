#!/usr/bin/env python

import random
import csv

# SHUFFLE LIST
def list_shuffle(list_number):
  new_list = list_number
  random.shuffle(new_list)
  return new_list

# APPEND 0001 TO 9999 TO A GIVEN SERIES
def create_series(series):
  number = 1
  number_end_series = []
  while number <= 1000:
    if len(str(number)) == 1:
      new_number = "000" + str(number)
    elif len(str(number)) == 2:
      new_number = "00" + str(number)
    elif len(str(number)) == 3:
      new_number = "0" + str(number)
    else:
      new_number = str(number) 
    number_end_series.append(series+new_number)
    number += 1
  return number_end_series

# GENERATE A LIST OF NUMBERS WITH STARTING 4 DIGITS + 0001 TO 9999
def generate_list(user_input):
  list_of_series = user_input.split(',')
  new_list = []
  for series in list_of_series:
    new_list = new_list + create_series(series)
  return list_shuffle(new_list)

### MAIN ###

#GENERATE NUMBERS
new_list = generate_list(input('Enter number series (separate by ","):'))
counter = 0
number_to_print = []

#CREATE FILE
with open('AIVO_numbers.csv','w', newline='') as file_csv:
  writer = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
  while counter < len(new_list):
    number_to_print.append(new_list[counter])
    if counter == 19:
      writer.writerow(number_to_print)
      number_to_print = []
    if (counter+1)%20 == 0 and counter > 21:
      writer.writerow(number_to_print)
      number_to_print = []
    if counter == len(new_list)-1:
      writer.writerow(number_to_print)
      break;
    counter += 1