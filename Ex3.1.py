hours = float(input('How many hours did you work?: '))
rate = float(input('What is your hourly rate?: '))

overtime_rate = rate * 1.5
if hours > 40.0:
    pay = (hours - 40) * overtime_rate + (rate * 40)
    print("Overtime")
else:
    pay = hours * rate
    print("Regular")

print('You have earned: $',pay)
