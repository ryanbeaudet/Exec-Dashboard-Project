# monthly_sales.py

#adapted from sales_reporting_exercise
import operator
import os
import csv
import pandas as pd

#adapted from https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
def to_usd(value):
    return '${:,.2f}'.format(value)

#adapted from https://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
file_name = input("Please input the file you would like to be read:")

#adapted from https://stackabuse.com/python-check-if-a-file-or-directory-exists/
if (os.path.isfile(file_name) == False):
    print("Sorry! That file path does not exist.")
    exit()


sales = pd.read_csv(file_name)

#adapted from https://github.com/s2t2/exec-dash-starter-py/commit/f790f124895db77920e37655c91e1e5a7a424aaa#diff-2bc9303c4e0187b3363d76974cc2fc8c
products = sales["product"]



unique_products = products.unique()

unique_products = unique_products.tolist()

top_sellers = []

for p in unique_products:
    corresponding_rows = sales[sales["product"] == p]
    #https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
    total_sales = sales["sales price"].sum()
    product_sales = corresponding_rows["sales price"].sum()
    top_sellers.append({"name": p, "monthly_sales":product_sales} )

#adapted from https://github.com/s2t2/exec-dash-starter-py/commit/1bf69cc8c8c4d26d8aa265b4fc984cd01ad894ff#diff-2bc9303c4e0187b3363d76974cc2fc8c
top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)

#I did this part totally on my own, I'm very proud of it
n = 1
print("\n")
print( "Top Selling Products:")
for f in top_sellers:
    print(str(n) + ") " + f["name"] + ": " + str(to_usd(f["monthly_sales"])))
    n = n + 1
print("Total monthly sales: " + str(to_usd(total_sales)))
#adapted from https://www.google.com/search?q=how+to+cause+a+python+program+to+stop+running&oq=how+to+cause+a+python+program+to+stop+running&aqs=chrome..69i57.8490j0j7&sourceid=chrome&ie=UTF-8
#try:
    #with open(file_name) as file:
        
#except:
    #"Sorry! That file path does not exist."









#adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_explore.py




    



import plotly
import plotly.graph_objs as go

title = "Top Selling Products"

xValues = []
yValues = []

for g in top_sellers:
    xValues.append(g["name"])
    yValues.append(to_usd(g["monthly_sales"]))

#thanks to Caroline Feeney for the guidance!!
def month_amend(month):
    month_adjust={'01':'January', '02':'February',
    '03':'March','04':'April','05':'May','06':'June',
    '07':'July','08':'August','09':'September','10':'October',
    '11':'November','12':'December'}
    return month_adjust[month]

month = month_amend(file_name[-6:-4])
year = int(file_name[6:10])


#adapted from https://plot.ly/python/bar-charts/
trace = go.Bar(x=xValues, y=yValues)
data = [trace]
layout = go.Layout(
    title = "Monthly Sales for " + month + " " + str(year),
    xaxis = dict(
        title = 'Top Selling Products'
    ),
    yaxis = dict(
        title = "Total Sales per Item",
        hoverformat = '${%1.0f}')
)  

fig = go.Figure(data=data,layout=layout)

#adapted from https://stackoverflow.com/questions/42913417/plotly-not-showing-axis-labels-or-title
plotly.offline.plot(fig, filename="basic_pie_chart.html",  auto_open=True)
    

