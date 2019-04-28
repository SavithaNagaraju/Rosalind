import numpy as np
import matplotlib as plt

file1 = open("rosalind_dna.txt")
file1_data =file1.read()
print("Data:", file1_data)
print(len(file1_data))
def count_string(data,substring):
    count_substring = 0
    for a in data:
        if (a == substring):
            count_substring += 1
    return count_substring

count_A = count_string(file1_data, 'A')
count_C = count_string(file1_data, 'C')
count_G = count_string(file1_data, 'G')
count_T = count_string(file1_data, 'T')


print("Count of A: ", count_A)
print("Count of C: ", count_C)
print("Count of G: ", count_G)
print("Count of T: ", count_T)




#count_G = file1_data.count("G")
#print("Count of G: ", count_G)
#count_A = file1_data.count('G')
#print("Count of A: ", count_A)
#count_C = file1_data.count('C')
#print("Count of C: ", count_C)
#count_T = file1_data.count('T')
#print("Count of T: ", count_T)
