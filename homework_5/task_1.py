credit_amount = float(input("Enter credit amount: "))
months_in_1_year = 12
total_years = 5

print("Month   |  Payout amount  |  Percent")
print("-" * 35)

for month in range(1, total_years * months_in_1_year + 1):
    if month <= 2 * months_in_1_year:
        percent_rate = 0.02
    else:
        percent_rate = 0.04

    monthly_interest = credit_amount * percent_rate
    monthly_payment = monthly_interest + credit_amount / (total_years * months_in_1_year)

    print(f"{month:5}   |  {monthly_payment:14.2f}  |  {percent_rate * 100:8.2f}%")
    credit_amount -= monthly_payment
