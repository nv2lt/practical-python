# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
months = 1

while principal >0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        cur_payment = payment + extra_payment
    else:
        cur_payment = payment

    if (principal * (1+rate/12)) >= cur_payment: 
        principal = principal * (1+rate/12) - cur_payment
        total_paid = total_paid + cur_payment
    else: 
        total_paid = total_paid + principal
        principal = 0


    print(f'{months} {total_paid:>12,.2f} {principal:>12,.2f}')
    
    months = months + 1

print(f'Total paid: {total_paid:>5,.2f}')
print(f'Months: {months-1}')
