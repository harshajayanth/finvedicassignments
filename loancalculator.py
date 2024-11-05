def loan_calculator(loan_amount, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = loan_term_years * 12
    
    if monthly_interest_rate == 0:  # For zero interest rate loans
        monthly_payment = loan_amount / number_of_payments
    else:
        monthly_payment = (
            loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments
        ) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    
    return monthly_payment

# Example usage
if __name__ == "__main__":
    loan_amount = float(input("Enter loan amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (in %): "))
    loan_term_years = int(input("Enter loan term (in years): "))

    monthly_payment = loan_calculator(loan_amount, annual_interest_rate, loan_term_years)
    
    print(f"Monthly payment for the loan is: ${monthly_payment:.2f}")
