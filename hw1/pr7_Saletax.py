STATE_SALES_TAX = 0.05
COUNTY_SALES_TAX = 0.025
purchase = float(input('enter the amount of the purchase.'))
stateTax = purchase*STATE_SALES_TAX
countyTax = purchase*COUNTY_SALES_TAX

totalTax = stateTax+countyTax

print("Purchase amount:", format(purchase,'.2f'))
print("State tax: ", format(stateTax,'.2f'))
print("County tax: ", format(countyTax,'.2f'))
print("Total tax: ", format(totalTax,'.2f'))