from app.monthly_sales import *
import operator
import os
import csv
import pandas as pd


#adapted from https://github.com/s2t2/shopping-cart-screencast/blob/testing/shopping_cart_test.py
def test_to_usd():
    assert to_usd(7) == "$7.00"

    assert to_usd(7.25) == "$7.25"

    assert to_usd(7.2) == "$7.20"

    assert to_usd(7.88888888) == "$7.89"

    assert to_usd(1000000) == "$1,000,000.00"


#adapted from https://github.com/s2t2/shopping-cart-screencast/blob/testing/shopping_cart_test.py
def test_get_top_sellers():
    csv_name = "data/sales-201710.csv"
    
    

    sales = pd.read_csv(csv_name)

    output = get_top_sellers(sales)

    test_results = [
        {'name': 'Button-Down Shirt', 'monthly_sales': 5464.2}, 
        {'name': 'Super Soft Sweater', 'monthly_sales': 2249.8500000000004}, 
        {'name': 'Super Soft Hoodie', 'monthly_sales': 1800.0}, 
        {'name': 'Khaki Pants', 'monthly_sales': 1780.0}, 
        {'name': 'Vintage Logo Tee', 'monthly_sales': 526.35}, 
        {'name': 'Sticker Pack', 'monthly_sales': 283.5}, 
        {'name': 'Brown Boots', 'monthly_sales': 250.0}, 
        {'name': 'Winter Hat', 'monthly_sales': 155.4}
    ]
    
    assert output == test_results
