def computepay(hours, rate):
    if hours > 40.0:
        overtime_rate = rate * 1.5
        pay = (hours - 40) * overtime_rate + (rate * 40)
        #print("Overtime")
    else:
        pay = hours * rate
        #print("Regular")
    return pay
hours = input('How many hours did you work?: ')
rate = input('What is your hourly rate?: ')

try:
    f_hours = float(hours)
    f_rate = float(rate)
except:
    print('Please enter a numeric')
    quit()

computepay(f_hours, f_rate)
print('You have earned: $',pay)
