Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def calculateStateTax(price):
    state_sales_tax = .05
    return price * state_sales_tax

def calculateCountyTax(price):
    county_sales_tax =  .025
    return price * county_sales_tax

def displayTotals(price):
    print('Original price', price)
    state_tax = calculateStateTax(price)
    print('State tax', state_tax)
    county_tax = calculateCountyTax(price)
    print('County tax', county_tax)
    print('Total', price + state_tax + county_tax)

def main():
    price = float(input('Enter the price of the purchase: '))
    displayTotals(price)
