"""
open the file for reading and close it at the end.
each line is the same kind of data, soe we can process it with a definite loop, doing the same thing per line.
use the "accumulation pattern" by now, so the total and average should be easy.

total = 0.0
count = 0
open "scores.txt: for reading as in_file
for line in in_file
    score =n line as float
    total = total + score
    count = count + 1
close in_file
average = total / count
print average
"""



total = 0.0
count = 0
filename = input("Filename: ")
in_file = open(filename, "r")
for line in in_file:
    score = float(line)
    total += score
    count += 1
    print(f"Score = {score}   Total so far = {total:.1f}")
in_file.close()
average = total / count
print(f"Average = {average:.1f}")
