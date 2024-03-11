# dependancies
import csv
import re

# files to load and output
file_to_load = "/Users/vrindapatel/Desktop/Homework/W3 Python challenge/python-challenge/PyBank/Resources/budget_data.csv"
file_to_output = "/Users/vrindapatel/Desktop/Homework/W3 Python challenge/python-challenge/PyBank/Analysis/Output.txt"

# revenue parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["", 999999999]
total_revenue = 0

# Read CSV file and convert into dictionaries   
with open(file_to_load) as revenue_data:
    csv.reader = csv.DictReader(revenue_data)

    for row in csv.reader:

        #calculate the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])

        #Track revenue change
        revenue_change = int(row["Revenue"]) - prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        #calculate greatest increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

         #calculate greatest decrease
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

#caculate Average revenue change
revenue_average = sum(revenue_change_list) / len(revenue_change_list)

# The Output summary
output = (
    f"\nFinancial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_average}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print Output
print(output)

#Export result to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)