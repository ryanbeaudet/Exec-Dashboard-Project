# monthly_sales.py

# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...

#adapted from sales_reporting_exercise
import os
import csv
import pandas as pd



#adapted from https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
file_name = input("Please input the file you would like to be read:")

sales = pd.read(file_name)

print("-----------------------")
print("MONTH: March 2018")



print("-----------------------")
print("CRUNCHING THE DATA...")

total_sales = sales["sales price"].sum()

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")