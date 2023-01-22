# 4. Read a String from a File

in_file = open("name.txt", "r")
text = in_file.read().strip()
in_file.close()
print(f"Greetings {text}!")



# 5. Greater-Than Counter

# Algorithm
# count = 0
# get threshold from use input
# open "recentrain.txt for reading as in_file
# for line in in_file
#     number = line as float
#     if number > threshold
#         count = count + 1
# print count, count / 10 percentage, threshold

count = 0
total = 0
filename = input("Filename: ")
threshold = float(input("Threshold: "))
in_file = open(filename, "r")
for line in in_file:
    number = float(line)
    total += 1
    if number > threshold:
        count += 1
in-file.close()
print(f"{count} out of {total} ({100 * count / total:.1f}%) values in {filename} are greater than {threshold}.")



# 6. File Filter

# Algorithm
# get input file name
# get output file name
# get search string
# filtered_strings = []
# open the input file for reading as in_file
# for line in in_file
#     if search string in line
#         add the line to filtered_strings
# close input file
# open output file for writting as out_file
# for string in filtered_strings
#     write string to output file
# close output file


input_file = input("Input file: ")
output_file = input("Output file: ")
search_string = input("Search string: ")
filtered_lines = []
in_file = open(input_file, "r")
for line in in_file:
    if line.find(search_string) >= 0:
        filtered_lines.append(line)
in_file.close()
out_file = open(output_file, 'a')
for line in filtered_lines:
    out_file.write(line)
out_file.close()


# Version 2

input_file = input("Input file: ")
output_file = input("Output file: ")
search_string = input("Search string: ")
filtered_lines = []
in_file = open(input_file, "r")
for line in in_file:
    if line.strip().startswith(search_string):
        filtered_lines.append(line)   
in_file.close()
out_file = open(output_file, 'a')
for line in filtered_lines:
    out_file.write(line)
out_file.close()