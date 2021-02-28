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
def generate_list(series1, series2 = "None", series3 = "None", series4 = "None", series5 = "None", series6 = "None", series7 = "None", series8 = "None", series9 = "None", series10 = "None"):
  new_list = []
  new_list = new_list + create_series(series1)
  if series2 != "None":
    new_list = new_list + create_series(series2)
  if series3 != "None":
    new_list = new_list + create_series(series3)
  if series4 != "None":
    new_list = new_list + create_series(series4)
  if series5 != "None":
    new_list = new_list + create_series(series5)
  if series6 != "None":
    new_list = new_list + create_series(series6)
  if series7 != "None":
    new_list = new_list + create_series(series7)
  if series8 != "None":
    new_list = new_list + create_series(series8)
  if series9 != "None":
    new_list = new_list + create_series(series9)
  if series10 != "None":
    new_list = new_list + create_series(series10)
  return list_shuffle(new_list)

### MAIN ###

#GENERATE NUMBERS
new_list = generate_list("8322","9012","8727","9696","8161","9022","9749","9660","9876","8671")
counter = 0
number_to_print = []

#CREATE FILE
with open('AIVO_numbers.csv','w', newline='') as file_csv:
  writer = csv.writer(file_csv, quoting=csv.QUOTE_ALL)
  while counter < len(new_list):
    number_to_print.append(new_list[counter])
    if counter%20 == 0:
      writer.writerow(number_to_print)
      number_to_print = []
    if counter == len(new_list)-1:
      writer.writerow(number_to_print)
      break;
    counter += 1