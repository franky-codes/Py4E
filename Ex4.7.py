# computegrade function takes a float and outputs a letter grade
def computegrade(score):
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')

raw_score = input('Enter score: ')

try:
    score = float(raw_score) # is this variable global?
except:
    print('Score must be entered as a numeric value')
    quit()

try:
    score >= 0.0 and score <= 1.0
except:
    print('Score must be between 0.0 and 1.0')
    quit()

computegrade(raw_score)
