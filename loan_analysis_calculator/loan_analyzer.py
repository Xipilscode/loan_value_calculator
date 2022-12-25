# coding: utf-8
import csv
from pathlib import Path

# Declare a list of loan prices.
loan_costs = [500, 600, 200, 1000, 450]

# Use the `len` function to calculate the total number of loans in the list.
number_of_loans = len(loan_costs)

# Print the number of loans from the list
print("-----------------------------------------\n")
print(f"The number of loans is: {number_of_loans}\n")

# Use the `sum` function to calculate the total of all loans in the list.
total_value_of_loans = sum(loan_costs)

# Print the total value of the loans
print(f"The total value of loans is: ${total_value_of_loans}\n")

# Using the sum of all loans and the total number of loans, calculate the average loan price.
average_loan_amount = total_value_of_loans / number_of_loans

# Print the average loan amount
print(f"The average loan price is: ${average_loan_amount}\n")
print("-----------------------------------------")

# Declare loan data, you will need to calculate the present value for the loan.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

# Print each variable.
print("-----------------------------------------")
print("Loan # 1\n")
print(f"The future value of the loan is: ${future_value}\n")
print(f"The remaining month for the loan: {remaining_months}\n")


# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
# You'll want to use the **monthly** version of the present value formula.
# Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
discount_rate = 0.2
present_value = future_value / (1 + discount_rate/12) * remaining_months

#  Conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#  If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#  Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
if present_value > loan.get("loan_price") or present_value ==loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it.\n")
else :
    print("THe loan is too expensive and not worth the price.\n") 
    
# Declare the loan data, you will need to calculate the present value for the loan.
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",   
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
# It includes parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`.
# The function returns the `present_value` for the loan.
# Use an `annual_discount_rate` of 0.2 for this new loan calculation.
future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")
annual_discount_rate = 0.2

def calculate_present_value(future_value, remaining_months, annual_discount_rate ):
    present_value = future_value / (1 + annual_discount_rate/12) * remaining_months
    
    return present_value 

# Call the function to calculate the present value of the new loan given below.
print("-----------------------------------------")
print("----------------------------------------- \n")
print("Loan # 2 \n ") 
print(f"The present value of the loan is: {calculate_present_value(future_value, remaining_months, annual_discount_rate )} \n")
print("-----------------------------------------")

# Declare list of dictionaries for multiple loans.
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans = []
# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list.
for loan in loans:
    if loan["loan_price"]  <= 500:
        inexpensive_loans.append(loan)

# Print the `inexpensive_loans` list
print("-----------------------------------------\n")
print(inexpensive_loans,"\n")
print("-----------------------------------------")

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# Open the output CSV file path using 'write open'
with open(output_path, "w") as csvfile:
    # Create a csvwriter
    csvwriter =csv.writer(csvfile, delimiter=",")
    # Write the header to the CSV file
    csvwriter.writerow(header)
    # Write the values of each dictionary inside of `inexpensive_loans`
    # as a row in the CSV file
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())