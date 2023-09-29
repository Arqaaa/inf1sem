import csv

with open('NP.csv') as csvfile:
    NP = csv.DictReader(csvfile)
with open('A.csv') as csvfule:
    A = csv.DictReader(csvfile)

[r, c] = size(NP);
[r2, c2] = size(A);

for i in range(0, r):
    for j in range(0, c):
        NP(i, j) = float(NP(i, j));
for i in range(0, r2):
    for j in range(0, c2):
        A(i, j) = float(A(i, j))

print()