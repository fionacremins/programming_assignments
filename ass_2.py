"""
name: Fiona Cremins
desc: BMI
"""

# Print Introduction
print('This is a BMI test')

# Ask the user for their height in feet and inches
print('Please enter your height in feet and inches')
height1 = int(input('feet: '))
height2 = float(input('inches: '))

# Convert height into inches only
height = (height1*12)+height2

# Ask the user for their weight in stones and pounds
print('Please enter your weight in stones and pounds')
weight1 = int(input('stone: '))
weight2 = int(input('pounds: '))

# Convert weight into pounds only
weight = (weight1*14) + weight2

# BMI formula
bmi = weight*703/height**2

# Print the users BMI
print('Your BMI is:', round(bmi, 1))

# Input BMI range
if bmi <18.5:
    print('You are underweight')

elif bmi >= 18.5 and bmi <= 24.9:
    print('You are of normal weight')

elif bmi >= 25 and bmi <= 29.9:
    print('You are overweight')

else:
    print('You are obese')
