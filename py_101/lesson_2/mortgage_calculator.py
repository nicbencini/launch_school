"""
A mortgage calculator.
"""

MIN_LOAN_TERM = 2 #years
MAX_LOAN_TERM = 50 #years
MAX_LOAN_AMOUNT = 1000 #dollars
MIN_APR = 0.01 #percent
MAX_APR = 100 #percent

def calculate_monthly_interest_rate(apr):
    return apr/12

def calculate_monthly_payment(loan_amount,
                              monthly_interest_rate,
                              loan_duration):

    monthly_paymemt = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (- loan_duration)))

    return monthly_paymemt

def valid_number(number):

    try:
        float(number)
        return True
    except:
        return False

def number_in_range(number, min, max):
    if number > min and number < max:
        return True
    return False

def get_loan_amount():

    print('Please enter the loan ammout that you would like to borrow.')

    while True:

        loan_amount = input()

        check_1 = valid_number(loan_amount)

        if check_1:
            check_2 = float(loan_amount) > MAX_LOAN_AMOUNT
            if check_2:
                break
            print(f'Please enter a loan value greater than ${MAX_LOAN_AMOUNT}')
        else:
            print('Please enter a valid number.')

    return float(loan_amount)


def get_loan_duration():

    print('Please enter the loan duration in years.')

    while True:

        loan_duration = input()

        check_1 = valid_number(loan_duration)

        if check_1:
            check_2 = number_in_range(float(loan_duration), MIN_LOAN_TERM, MAX_LOAN_TERM)
            if check_2:
                break
            print(f'Please enter a loan term within {MIN_LOAN_TERM} years and {MAX_LOAN_TERM} years.')
        else:
            print('Please enter a valid number.')

    return float(loan_duration)

def get_apr():

    print('Please enter the monthly interest rate as a percentage.')

    while True:

        loan_apr = input()

        check_1 = valid_number(loan_apr)

        if check_1:
            check_2 = number_in_range(float(loan_apr), MIN_APR, MAX_APR)
            if check_2:
                break
            print(f'Please enter an interest rate within {MIN_APR}% and {MAX_APR}%.')
        else:
            print('Please enter a valid number.')

    return float(loan_apr)


print('Welcome to Mortgage Calculator')

loan_amount_value = get_loan_amount()
loan_duration_years_value = get_loan_duration()
loan_duration_months_value = loan_duration_years_value * 12
loan_apr_value = get_apr()
loan_apr_decimal_value = loan_apr_value / 100

monthly_interest_rate_value = calculate_monthly_interest_rate(loan_apr_decimal_value)
monthly_payments = round(calculate_monthly_payment(loan_amount_value, monthly_interest_rate_value, loan_duration_months_value),2)

print(f'Your monthly load repayments are ${monthly_payments} per month for {loan_duration_years_value} years at an interest rate of {loan_apr_value}%.')
