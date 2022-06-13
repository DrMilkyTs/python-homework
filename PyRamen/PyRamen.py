# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('C:\\Users\\mfiaa\\OneDrive\\Desktop\\Github Projects\\python-homework-main\\PyRamen\\Resources\\menu_data.csv')
sales_filepath = Path('C:\\Users\\mfiaa\\OneDrive\\Desktop\\Github Projects\\python-homework-main\\PyRamen\\Resources\\sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') #open csvreader

    header = next(csvreader) #skip first line

    for row in csvreader: #append to menu, making a list of lists
        item = row[0]
        category = row[1]
        description = row[2]
        price = row[3]
        cost = row[4]
        menu.append([item, category, description, price, cost])

# @TODO: Read in the sales data into the sales list

with open(sales_filepath) as csvfile: 
    
    csvreader = csv.reader(csvfile, delimiter=',') #open csvreader

    header = next(csvreader) #skip first line

    for row in csvreader: #append to sales, making list of lists
        item_id = row[0]
        date = row[1]
        credit_card = row[2]
        quantity = int(row[3])
        menu_item = row[4]
        sales.append([item_id, date, credit_card, quantity, menu_item])
    
# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object

for sales_row in sales:

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(sales_row[3])
    sales_item = sales_row[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    
    if sales_item not in report: # add sales to report, without making duplicate menu items
        report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
    else:
        continue 
    
for sales_row in sales:

    quantity = int(sales_row[3])
    sales_item = sales_row[4]

    if sales_item in report:
        report[sales_item]["01-count"] += int(quantity) #have to place this separately or it doesnt count the quanitity correctly

    # @TODO: For every row in our sales data, loop over the menu records to determine a match

for sales_row in sales:

    quantity = int(sales_row[3])
    sales_item = sales_row[4]

    for menu_row in menu: # iterate through menu, to match with sales data

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        menu_item = menu_row[0]
        menu_price = float(menu_row[3])
        menu_cost = float(menu_row[4])

        # @TODO: Calculate profit of each item in the menu data
        
        menu_profit = menu_price - menu_cost #profit from each menu item

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item

        if sales_item == menu_item:
            
            # @TODO: Print out matching menu data

            #print(menu)

            # @TODO: Cumulatively add up the metrics for each item key

            report[sales_item]["02-revenue"] += menu_price * quantity
            report[sales_item]["03-cogs"] += menu_cost * quantity
            report[sales_item]["04-profit"] += menu_profit * quantity
        
        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match

        else:
            continue #printing the message gives an infinite loop....

    # @TODO: Increment the row counter by 1

    #what does this step mean?... instruction on readme stop here....

# @TODO: Print total number of records in sales data

#print(report)

# @TODO: Write out report to a text file (won't appear on the command line output)
output_path = 'C:\\Users\\mfiaa\\OneDrive\\Desktop\\Github Projects\\python-homework-main\\PyRamen\\output.txt'

with open(output_path, 'w') as csvfile: #write to output txt file
    for report_key, report_value in report.items():
        csvfile.write(f"{report_key}: {report_value}\n")