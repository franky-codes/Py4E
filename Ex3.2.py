hours = input('How many hours did you work?: ')

rate = input('What is your hourly rate?: ')

try:
    fhours = float(hours)
    frate = float(rate)
except:
    print('Please enter a numeric')
    quit()

if fhours > 40.0:
    overtime_rate = frate * 1.5
    pay = (fhours - 40) * overtime_rate + (frate * 40)
    print("Overtime")
else:
    pay = fhours * frate
    print("Regular")

print('You have earned: $',pay)
