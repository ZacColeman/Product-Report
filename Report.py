import csv
import os

# Retrieves data from Product Master and Sales
with open('ProductMaster.csv', 'r') as productMaster:
    read = csv.reader(productMaster)
    productID = {}

    for row in read:
        productID[row[0]] = {'ProductName': row[1], 'Price': row[2], 'LotSize': row[3]}

with open('Sales.csv', 'r') as sales:
    read = csv.reader(sales)
    salesID = {}

    for row in read:
        salesID[row[0]] = {'ProductID': row[1], 'TeamID': row[2], 'Quantity': row[3]}

# Calculates the gross revenue and the total units sold
totalUnit_sale1 = int(salesID['1']['Quantity']) * int(productID['1']['LotSize'])
totalUnit_sale2 = int(salesID['2']['Quantity']) * int(productID['1']['LotSize'])
totalUnit_sale3 = int(salesID['3']['Quantity']) * int(productID['2']['LotSize'])
totalUnit_sale4 = int(salesID['4']['Quantity']) * int(productID['3']['LotSize'])
totalUnit_sale5 = int(salesID['5']['Quantity']) * int(productID['3']['LotSize'])

grossRevenue_sale1 = float(productID['1']['Price']) * totalUnit_sale1
grossRevenue_sale2 = float(productID['1']['Price']) * totalUnit_sale2
grossRevenue_sale3 = int(productID['2']['Price']) * totalUnit_sale3
grossRevenue_sale4 = int(productID['3']['Price']) * totalUnit_sale4
grossRevenue_sale5 = int(productID['3']['Price']) * totalUnit_sale5

itemSold1_totalUnits = totalUnit_sale1 + totalUnit_sale2
itemSold2_totalUnits = totalUnit_sale3
itemSold3_totalUnits = totalUnit_sale4 + totalUnit_sale5

itemSold1_totalRevenue = grossRevenue_sale1 + grossRevenue_sale2
itemSold2_totalRevenue = grossRevenue_sale3
itemSold3_totalRevenue = grossRevenue_sale4 + grossRevenue_sale5

# Creates names for items
minorWidget = productID['1']['ProductName']
criticalWidget = productID['2']['ProductName']
completeSystem_Basic = productID['3']['ProductName']
completeSystem_Deluxe = productID['4']['ProductName']

# Brings sold item's information together
product1 = [criticalWidget, itemSold1_totalRevenue, itemSold1_totalUnits]
product2 = [completeSystem_Deluxe, itemSold2_totalRevenue, itemSold2_totalUnits]
product3 = [minorWidget, itemSold3_totalRevenue, itemSold3_totalUnits]

# Header
name = "Name"
totalRevenue = "TotalRevenue"
totalUnits = "TotalUnits"
header = name, totalRevenue, totalUnits

# Writes new data to Product Report file
with open('ProductReport.csv', 'w') as productReport:
    writer = csv.writer(productReport)
    writer.writerow(header)
    writer.writerow(product3)
    writer.writerow(product1)
    writer.writerow(product2)

# Lets user know the calculation process is done
print("Process complete! Opening file in default program.")

# Opens file using default program
os.startfile('ProductReport.csv')
