# monthly_sales.py

# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...

#adapted from sales_reporting_exercise
import os
import csv
import pandas as pd



#adapted from https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
file_name = input("Please input the file you would like to be read:")

#adapted from https://stackabuse.com/python-check-if-a-file-or-directory-exists/
if (os.path.isfile(file_name) == False):
    print("Sorry! That file path does not exist.")
    exit()


sales = pd.read_csv(file_name)

products = sales["product"]

unique_products = products.unique()

#adapted from https://www.google.com/search?q=how+to+cause+a+python+program+to+stop+running&oq=how+to+cause+a+python+program+to+stop+running&aqs=chrome..69i57.8490j0j7&sourceid=chrome&ie=UTF-8
#try:
    #with open(file_name) as file:
        
#except:
    #"Sorry! That file path does not exist."



print("-----------------------")
print("MONTH: March 2018")



print("-----------------------")
print("CRUNCHING THE DATA...")

#adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_explore.py
total_sales = sales["sales price"].sum()
print(total_sales)

#https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
product_grouping = sales.groupby("product")["sales price"].sum()

sales_val = product_grouping.nlargest(7).values
#product_val = sales_val.unstack(index="sales price",columns = "product")

i = 0

#while (i < 7):
    #print(sales_val[i])
    #current = sales_val[i]
    #q = 0
    #while(current != product_grouping[q]):
        #q = q + 1
    #print(sales.groupby("product").apply()

for p in sales:
    print(p[2])

    

print(product_grouping[0])



#print(str(product_grouping.nlargest(7).values))

import plotly
import plotly.graph_objs as go

labels = []
values = []

#for g in product_grouping:
    #if (g < product_grouping.count()):
        #labels.append(g)
    #values.append(g["sales price"])

trace = go.Bar(x=int(product_grouping["sales price"]), y=int(product_grouping.index), name = "Monthly Sales")

plotly.offline.plot([trace], filename="basic_pie_chart.html",  auto_open=True)
    

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")