score = input('Enter score: ')
num_score = float(score)

if num_score > 1.0 or num_score < 0.0:
  print('Score must be between 0.0 and 1.0')
  quit()
elif num_score >= 0.9:
  grade = 'A'
elif num_score >= 0.8:
  grade = 'B'
elif num_score >= 0.7:
  grade = 'C'
elif num_score >= 0.6:
  grade = 'D'
elif num_score < 0.6:
  grade = 'F'

print('Grade is ',grade)
