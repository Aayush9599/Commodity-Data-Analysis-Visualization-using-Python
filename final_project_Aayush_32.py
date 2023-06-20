#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:51:25 2023

@author: aayushsahare
"""
'''
Program name: Final Project Python
Author Name : Aayush Sahare
Description :The project involves reading data from a file,
             organizing it into individual data records, 
             selecting data records of interest through user interaction, 
             consolidating the selected data records and generating graphical 
             representations of the data.  
             The only new aspect is the use of plotly to generate grouped bar 
             graphs. The final project challenges us to expand on the preliminary
             work we completed last week to provide a comprehensive analysis of the commodity data.
Revisions 00: Import the required modules
          01: initialize a List data
          02: open the csv file for reading
          03: instantiate a csv file reader
          04: reorganize the data, loop through the data,one row at a time
          05: get the Location names from header row 1
          06: slice to remove commodity and date,now we have a List of Locations
          07: iterate through Locations and values to build records
          08: for each Location,value create a new record 
          09: index for the next data row
          10: new data row: commodity and date
          11: append location,remove dollar sign,convert/append price,convert date,replace date string
          12: close the input data file  
          13: create a list of unique commodity,sort it & print the list of products with their index numbers
          14: prompt the user to enter the index numbers of the products
          15: create a list of selected products based on the user's input & print it
          16: similarly do steps 13,14 & 15 for dates and locations
          17: create a variable to hold the count of matching records
          18: convert the date in selected_date into a datetime object
          19: create a dictionary to hold the data for each product and location
          20: Loop through the data to find matching records
          21: If the product and location match and the date is within the selected range, add the price to the list
          22: print the total count of matching records
          23: Create an empty list to hold the traces
          24: Set the title of the graph
          25: Create a dictionary of colors for each location
          26: Traverse the dictionary and calculate the average price for each product and location
          27: Calculate the average price for the current product and location
          28: Set the marker color for the current location
          29: Create a trace for the current product and location
          30: Create the layout for the graph
          31: Create the figure and plot the graph
          32: Save the graph to an HTML file
'''
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from datetime import datetime
import plotly.graph_objs as go
import plotly.offline as pyo

data = []

###! open the csv file for reading

csvfile = open( 'produce_csv.csv','r')

###! instantiate a csv file reader

reader = csv.reader(csvfile)

###! reorganize the data

###! main Loop reads one row at a time
###！each row produces five records (Lists) in data
for row in reader:
    
    ###! get the Location names from header row 1
    
    if reader.line_num == 1: 
        
        ###! slice to remove commodity and date
        ###! now we have a List of Locations
        locations = row[2:]  
    
    ###! iterate through Locations and values to build records    
    else:

        ###! each Location,value
        ###! creates a new record          
        for location, value in zip(locations,row[2:]):  
            
            ###! index for the next data row
            
            row_num = len(data)  
            
            ###! new data row: commodity and date
            
            data.append(row[:2])
            
            ###! append location

            data[row_num].append(location)
            
            ###！ remove dollar sign
            
            price = value.replace('$','')
            
            ###! convert/append price

            data[row_num].append(float(price)) 
            
            # convert date

            date = datetime.strptime(data[row_num][1],'%m/%d/%Y') 
            
            ###! replace date string

            data[row_num][1] = date;

###! close the input data file
csvfile.close()

# create a list of unique commodity from the data
uComList = list(set([row[0] for row in data]))

# sort the list of commodity in ascending order
sorted_uComList = sorted(uComList)

# print the list of products with their index numbers
print("SELECT PRODUCTS BY NUMBER")
for i, product in enumerate(sorted_uComList):
    if i % 3 == 0:
        print()
    print(f"< {i}> {product}", end="\t\t")

# prompt the user to enter the index numbers of the products they are interested in
selected_indices = input("\nEnter product numbers separated by spaces: ")

# create a list of selected products based on the user's input
selected_products = [sorted_uComList[int(index)] for index in selected_indices.split()]

# print the selected products
print("\nSelected products:", " ".join(selected_products))

# create a list of unique dates from the data
uDate = list(set([row[1] for row in data]))

# sort the list of dates in ascending order
sorted_uDate = sorted(uDate)

# print a message for the user to select a date range
print("SELECT DATE RANGE BY NUMBER")

# loop through the sorted dates, printing them in groups of 5 with their index number
for i, date in enumerate(sorted_uDate):
    if i % 5 == 0:
        print()
    # convert the date object to a string in the format "YYYY-MM-DD"    
    date_str = date.strftime('%Y-%m-%d')
    # print the index number and the formatted date, separated by a tab
    print(f"< {i}> {date_str}", end="\t")

# print a new line character for spacing    
print('\n')

# print the earliest and latest available dates in the data
print(f"Earliest available date is: {sorted_uDate[0].strftime('%Y-%m-%d')}")
print(f"Latest available date is: {sorted_uDate[52].strftime('%Y-%m-%d')}")

# ask the user to input the start and end date numbers separated by spaces
selected_indices_date = input("\nEnter start/end date numbers separated by spaces: ")

# create a list of selected dates based on the user's input
selected_date = [sorted_uDate[int(index)].strftime('%Y-%m-%d') for index in selected_indices_date.split()]

# print the selected date range
print("\nDates from:", selected_date[0], "to", selected_date[-1])

# create a list of unique locations from the data
locations = list(set([row[2] for row in data]))

# sort the list of locations in ascending order
sorted_locations = sorted(locations)

# print a message for the user to select locations
print("SELECT LOCATIONS BY NUMBER")

# loop through the sorted locations, printing them with their index number
for i, location in enumerate(sorted_locations):
    print(f'<{i}> {location}')

# ask the user to input the location numbers separated by spaces
selected_indices_location = input("\nEnter location numbers separated by space: ")

# create a list of selected locations based on the user's input
selected_location = [sorted_locations[int(index)] for index in selected_indices_location.split()]

# print the selected locations, separated by spaces
print('\nSelected locations:', ' '.join(selected_location))

# create a variable to hold the count of matching records
record_count = 0

#convert the date in selected_date into a datetime object
start_date, end_date = map(datetime.strptime, selected_date, ['%Y-%m-%d']*2)

# create a dictionary to hold the data for each product and location
selected_data = {}

# Loop through the data to find matching records
for row in data:
    if row[0] in selected_products and row[2] in selected_location and start_date <= row[1] <= end_date:
        # If the product and location match and the date is within the selected range, add the price to the list
        if row[0] not in selected_data:
            selected_data[row[0]] = {}
        if row[2] not in selected_data[row[0]]:
            selected_data[row[0]][row[2]] = []
        selected_data[row[0]][row[2]].append(row[3])
        record_count += 1

# print the total count of matching records
print("Total number of records:", record_count)

# Create an empty list to hold the traces
traces = []

# Set the title of the graph
title = 'Average Prices of Selected Products in Selected Cities'

# Create a dictionary of colors for each location
color_map = {'Atlanta': 'blue', 'Chicago': 'red', 'Los Angeles': 'green', 'New York': 'purple'}

# Traverse the dictionary and calculate the average price for each product and location
for product in selected_data:
    for location in selected_data[product]:
        # Calculate the average price for the current product and location
        avg_price = sum(selected_data[product][location]) / len(selected_data[product][location])
        # Set the marker color for the current location
        marker_color = color_map[location]
        # Create a trace for the current product and location
        trace = go.Bar(x=[product], y=[avg_price], name=location, marker=dict(color=marker_color))
        traces.append(trace)

# Create the layout for the graph
layout = go.Layout(title=title, xaxis=dict(title='Product'), yaxis=dict(title='Price', tickformat='$.2f'))

# Create the figure and plot the graph
fig = go.Figure(data=traces, layout=layout)
fig.show()

# Save the graph to an HTML file
pyo.plot(fig, filename='grouped-bar.html')












