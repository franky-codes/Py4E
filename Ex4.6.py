# cumputepay function determines if hours > 40 and applies a pay rate to pay for overtime
def computepay(hours, rate):
    if hours > 40.0:
        overtime_rate = rate * 1.5
        pay = (hours - 40) * overtime_rate + (rate * 40)

    else:
        pay = hours * rate

    return pay

hours = input('How many hours did you work?: ')
rate = input('What is your hourly rate?: ')
f_hours = float(hours)
f_rate = float(rate)

x = computepay(f_hours, f_rate)
print('You have earned: $', x)
