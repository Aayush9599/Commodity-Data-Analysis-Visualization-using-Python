# Python-Final-Project

This Python project involves the analysis and visualization of commodity data. It includes reading data from a CSV file, organizing it into individual data records, selecting data records of interest through user interaction, consolidating the selected data records, and generating graphical representations of the data. The project uses Plotly to create grouped bar graphs. 

**Project Steps**

The project consists of several steps, which are listed below:

Revisions: The initial step is importing the required modules.
Step 01: Initializing a list to store the data.

Step 02: Opening the CSV file for reading.

Step 03: Instantiating a CSV file reader.

Step 04: Reorganizing the data by looping through it, one row at a time.

Step 05: Getting the location names from the header row.

Step 06: Slicing to remove commodity and date, resulting in a list of locations.

Step 07: Iterating through locations and values to build records.

Step 08: For each location and value, creating a new record.

Step 09: Index for the next data row.

Step 10: Processing a new data row with commodity and date.

Step 11: Appending location, removing dollar sign, converting/appending price, converting date, and replacing date string.

Step 12: Closing the input data file.

Step 13: Creating a list of unique commodities, sorting it, and printing the list of products with their index numbers.

Step 14: Prompting the user to enter the index numbers of the products.

Step 15: Creating a list of selected products based on the user's input and printing it.

Steps 16: Similarly repeating steps 13, 14, and 15 for dates and locations.

Step 17: Creating a variable to hold the count of matching records.

Step 18: Converting the date in selected_date into a datetime object.

Step 19: Creating a dictionary to hold the data for each product and location.

Step 20: Looping through the data to find matching records.

Step 21: Adding the price to the list if the product, location, and date match.

Step 22: Printing the total count of matching records.

Step 23: Creating an empty list to hold the traces.

Step 24: Setting the title of the graph.

Step 25: Creating a dictionary of colors for each location.

Step 26: Calculating the average price for each product and location.

Step 27: Calculating the average price for the current product and location.

Step 28: Setting the marker color for the current location.

Step 29: Creating a trace for the current product and location.

Step 30: Creating the layout for the graph.

Step 31: Creating the figure and plotting the graph.

Step 32: Saving the graph to an HTML file.
