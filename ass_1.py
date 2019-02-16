"""
name: Fiona Cremins 
desc: degrees to latitude
"""


# Print Introduction
print('This application converts Latitude and Longitudes in degrees/minutes/seconds into decimal.')



# Ask the user for the degrees
degrees = input('Please enter degrees: ')

# Ask the user for the minutes
minutes = input('Please enter minutes: ')

# Ask the user for the seconds
seconds = input('Please enter seconds: ')

# Convert strings into floats
decimal = float(degrees) + float(minutes)/60.0 + float(seconds)/3600.0

# Print Answer
print('This your answer: ', round(decimal, 4))
