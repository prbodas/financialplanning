#!/usr/local/bin/python3
from prettytable import PrettyTable

#spending variables
RENT = 500
EAT_OUT = 3 #days/week
PRICE_PER_EAT_OUT = 25
AVG_MONTH_GROCERY = 70
ESSENTIALS_MONTH = 250
GYM_MONTH = 200
TRANSPORT_MONTH = 350
MISC_MONTH = 100

INVESTMENT_RATE = 1.07
INFLATION = 1.03
PERCENT_LIVE_ON = 0.04
INCOME = 60000
TAX_RATE = 0.6502 # the percent of income you keep after all taxes
WAGE_TO_INFLATION_RATE = 0.5
PERCENT_401K = 0.1
CURRENT_SAVINGS = 60000
EXPECTED_INCOME_GROWTH = 1.05

MAX_YEAR = 20 # how many years in the future you want to see
START_AGE = 21


def get_yearly_expenses(year):
	return INFLATION**year * \
	        (RENT*12 + \
		    EAT_OUT*PRICE_PER_EAT_OUT*52 + \
		    AVG_MONTH_GROCERY*12 + \
		    ESSENTIALS_MONTH*12 + \
		    TRANSPORT_MONTH*12 + \
		    GYM_MONTH*12 + \
		    MISC_MONTH*12);

current_savings = CURRENT_SAVINGS

table = PrettyTable(["Year", "Current Income", "Current Savings", "Live On"])

for year in range(0,MAX_YEAR):
	post_401k = INCOME*(1-PERCENT_401K)
	take_home_pay = post_401k*TAX_RATE
	post_expenses = take_home_pay - get_yearly_expenses(year)
	current_savings = (current_savings + post_expenses)*INVESTMENT_RATE
	passive_income = current_savings * PERCENT_LIVE_ON
	table.add_row([year+START_AGE, "%.2f" % INCOME, "%.2f" % current_savings, "%.2f" % passive_income])
	#assuming wage increases
	INCOME = INCOME*(1+WAGE_TO_INFLATION_RATE*(1-INFLATION))*EXPECTED_INCOME_GROWTH

print("Base Monthly Expenses", get_yearly_expenses(0)/12)
print (table)