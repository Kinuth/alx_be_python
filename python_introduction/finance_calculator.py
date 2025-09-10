# Simple Finance Calculator
# This program calculates projected annual savings based on monthly income and expenses.
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
#calculate projected annual savings with 5% interest
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
#display the monthly savings and projected annual savings
print("your monthly savings is:", monthly_savings)
print("Your projected annual savings with 5% interest is:", projected_savings)


