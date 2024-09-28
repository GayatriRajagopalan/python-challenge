# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
from csv import reader, writer
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months_list = []
total_net_list = []
change_profit_loss_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = reader(financial_data)
    next(reader)   
    # Process each row of data    
    for row in reader:
        total_months_list.append(row[0])
        total_net_list.append(int(row[1]))
    prev_amt = int(total_net_list[0])

    for x in total_net_list:
        change_profit_loss_list.append(x - prev_amt)
        prev_amt = x
    
    # Generate the output summary
    #total months
    total_months = len(total_months_list)
    # Track the total
    total_net = sum(total_net_list)
    # Calculate the average of change in profit/loss across the months
    average_change_profit_loss = round(sum(change_profit_loss_list)/(len(total_months_list) - 1),2)
    # Calculate the greatest increase in profits (month and amount)
    greatest_increase_profit = max(change_profit_loss_list)
    greatest_increase_profit_month = total_months_list[change_profit_loss_list.index(greatest_increase_profit)]
    # Calculate the greatest decrease in losses (month and amount)
    greatest_decrease_profit = min(change_profit_loss_list)
    greatest_decrease_profit_month = total_months_list[change_profit_loss_list.index(greatest_decrease_profit)]
    # Print the output
    print(f"Financial Analysis\n -------------\n Total months:{total_months}\n Total: ${total_net}\n Average change: {average_change_profit_loss}\n Greatest Increase in Profits: {greatest_increase_profit_month} (${greatest_increase_profit})\n Greatest Decrease in Profits: {greatest_decrease_profit_month} (${greatest_decrease_profit})")
    
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-----------------------------------\n")
    txt_file.write(f"Total Months: {total_months} \n")
    txt_file.write(f"Total: ${total_net} \n")
    txt_file.write(f"Average Change: $ {average_change_profit_loss} \n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_profit_month} (${greatest_increase_profit}) \n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_profit_month} (${greatest_decrease_profit}) \n")
