"""
name: Fiona Cremins
student number: 118301286
Desc:  Handling Files & Exceptions

"""

# open files
input_file = open('numbers.txt' ,'r')
output_file = open('output.txt' , 'w')

# iniate original sum variable
sum = 0

# go through all lines in the file
for line in input_file:
    number = int(line)
    sum += number
    output_number = number * 2
    output_string = str(output_number) + "\n"

    # this writes to the output file
    output_file.write(output_string)

sum_string = "Orignal Sum: " + str(sum) + "\n"
output_file.write(sum_string)

# close the files to prevent corruption
input_file.close()
output_file.close()

