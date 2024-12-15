# Prompting the user for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assuming a simple annual interest rate of 5%
interest_rate = 0.05

# Calculate projected savings after one year with interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)

# Output the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
