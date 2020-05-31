
import math
def calc_mortgage(principal, interest, years):
    # monthly rate from annual percentage rate
    interest_rate = interest/(100 * 12)
    # total number of payments
    payment_num = years * 12
    # calculate monthly payment
    payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
    return payment
# mortgage loan principal
principal = 100000
# percent annual interest
interest = 7.5
# years to pay off mortgage
years = 30
# calculate monthly payment amount
monthly_payment = calc_mortgage(principal, interest, years)
# calculate total amount paid
total_amount = monthly_payment * years * 12
# show result ...
# {:,} uses the comma as a thousands separator
sf = '''\
For a {} year mortgage loan of ${:,}
at an annual interest rate of {:.2f}%
you pay ${:.2f} monthly'''
print(sf.format(years, principal, interest, monthly_payment))
print('-'*40)
print("Total amount paid will be ${:,.2f}".format(total_amount))
