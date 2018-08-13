#!/usr/local/bin/python3
from prettytable import PrettyTable

#spending variables
RENT = 500
EAT_OUT = 3 #days/week
PRICE_PER_EAT_OUT = 25
AVG_MONTH_GROCERY = 70
ESSENTIALS_MONTH = 150
GYM_MONTH = 200
TRANSPORT_MONTH = 200
MISC_MONTH = 100

INVESTMENT_RATE = 1.07
INFLATION = 1.03
INCOME = 60000
TAX_RATE = 0.6502 # the percent of income you keep after all taxes

MAX_YEAR = 15 # how many years in the future you want to see

def get_monthly_expenses(year):
	return INFLATION**year * \
	        (RENT*12 + \
		    EAT_OUT*PRICE_PER_EAT_OUT*52 + \
		    AVG_MONTH_GROCERY*12 + \
		    ESSENTIALS_MONTH*12 + \
		    TRANSPORT_MONTH*12 + \
		    GYM_MONTH*12 + \
		    MISC_MONTH*12);

current_savings = 0.0

table = PrettyTable(["Year", "Current Savings", "Passive Income"])

for year in range(0,MAX_YEAR):
	take_home_pay = INCOME*TAX_RATE
	post_expenses = take_home_pay - get_monthly_expenses(year)
	current_savings = (current_savings + post_expenses)*INVESTMENT_RATE
	amt_to_live_on = current_savings * (INVESTMENT_RATE - 1)
	table.add_row([year, "%.2f" % current_savings, "%.2f" % amt_to_live_on])

print (table)