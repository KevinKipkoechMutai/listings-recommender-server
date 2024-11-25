
#compute monthly mortgage rate
def calculate_monthly_mortgage(payment_price, annual_interest_rate, loan_term_years):
    payment_price = float(payment_price)  
    # convert annual interest rate to monthly
    r = (annual_interest_rate / 100) / 12  
    # find the total number of payments (months)
    n = loan_term_years * 12  
    #apply mortage compounding formula
    monthly_payment = payment_price * (r * (1 + r)**n) / ((1 + r)**n - 1)
    
    return monthly_payment
