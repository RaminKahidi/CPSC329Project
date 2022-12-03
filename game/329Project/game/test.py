# Open the file with read only permit
f = open("C:/University/third year/CPSC 329/CPSC329Project/game/329Project/game/john-the-ripper.txt", "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = f.readlines()
print(lines)
# close the file after reading the lines.
f.close()