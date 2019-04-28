import numpy as np

file1 = open("rosalind_rna.txt")
t =file1.read()
u = t.replace('T', 'U')
print(u)