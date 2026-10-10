
import numpy as np
import sys

1. Multiples of 7 between 7 and 100

print("\n1. Multiples of 7")
a = np.arange(7, 101, 7)
print(a)
print("Length:", len(a))

Output:

[ 7 14 21 28 35 42 49 56 63 70 77 84 91 98]

Length: 14

2. Create a 4x4 array filled with 9

print("\n2. 4x4 Array of 9")
a = np.full((4, 4), 9)
print(a)

Output:

[[9 9 9 9]

[9 9 9 9]

[9 9 9 9]

[9 9 9 9]]

3. Convert integer array to float

print("\n3. Integer to Float")
a = np.arange(1, 11)
b = a.astype(float)
print(b)
print("Data type:", b.dtype)

Output:

[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

Data type: float64

4. Compare memory size

print("\n4. Memory Size")
lst = [1, 2, 3, 4, 5]
a = np.array([1, 2, 3, 4, 5])
print("List memory:", sys.getsizeof(lst))
print("Array memory:", sys.getsizeof(a))

Output: Memory sizes are printed in bytes.

Exact values depend on the system.

5. Extract four corners of a 6x6 array

print("\n5. Four Corners")
a = np.arange(1, 37).reshape(6, 6)
print(a)
print("Corners:", a[0, 0], a[0, -1],
a[-1, 0], a[-1, -1])

Output:

[[ 1  2  3  4  5  6]

[ 7  8  9 10 11 12]

[13 14 15 16 17 18]

[19 20 21 22 23 24]

[25 26 27 28 29 30]

[31 32 33 34 35 36]]

Corners: 1 6 31 36

6. Every third element from index 1

print("\n6. Slicing")
a = np.arange(12)
print(a[1::3])

Output:

[ 1  4  7 10]

7. Reverse rows of a 5x5 array

print("\n7. Reverse Rows")
a = np.arange(1, 26).reshape(5, 5)
print(a[::-1])

Output:

[[21 22 23 24 25]

[16 17 18 19 20]

[11 12 13 14 15]

[ 6  7  8  9 10]

[ 1  2  3  4  5]]

8. Replace multiples of 3 with -1

print("\n8. Boolean Indexing")
a = np.arange(1, 11)
a[a % 3 == 0] = -1
print(a)

Output:

[ 1  2 -1  4  5 -1  7  8 -1 10]

9. Normalize array between 0 and 1

print("\n9. Normalization")
a = np.array([10, 20, 30, 40, 50])
b = (a - a.min()) / (a.max() - a.min())
print(b)

Output:

[0.   0.25 0.5  0.75 1.  ]

10. Transpose and verify

print("\n10. Transpose")
a = np.arange(1, 10).reshape(3, 3)
b = a.T
print(b)
print("Restored:", np.array_equal(b.T, a))

Output:

[[1 4 7]

[2 5 8]

[3 6 9]]

Restored: True

11. Maximum value and index

print("\n11. Maximum and Index")
a = np.random.randint(1, 100, 10)
i = np.argmax(a)
print("Array:", a)
print("Maximum:", a[i])
print("Index:", i)

Output: Random array, maximum and index are printed.

12. Element-wise remainder

print("\n12. Remainder")
a = np.array([10, 15, 20, 25])
b = np.array([3, 4, 6, 7])
print(np.remainder(a, b))

Output:

[1 3 2 4]

13. Stack two 2x3 arrays

print("\n13. Stack Arrays")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
c = np.stack((a, b))
print(c)
print("Shape:", c.shape)

Output:

[[[ 1  2  3]

[ 4  5  6]]

[[ 7  8  9]

[10 11 12]]]

Shape: (2, 2, 3)

14. Concatenate three arrays

print("\n14. Concatenate")
a = np.array([1, 2])
b = np.array([[3, 4]])
c = np.array([5, 6, 7])
result = np.concatenate(
(a.reshape(-1), b.reshape(-1), c.reshape(-1))
)
print(result)

Output:

[1 2 3 4 5 6 7]

15. Reshape and transpose

print("\n15. Reshape and Transpose")
a = np.arange(1, 17).reshape(4, 4)
print("Original:\n", a)
print("Transpose:\n", np.transpose(a))

Output:

Original:

[[ 1  2  3  4]

[ 5  6  7  8]

[ 9 10 11 12]

[13 14 15 16]]

Transpose:

[[ 1  5  9 13]

[ 2  6 10 14]

[ 3  7 11 15]

[ 4  8 12 16]]

16. Split 3D array into two parts

print("\n16. Split Array")
a = np.arange(32).reshape(2, 4, 4)
x, y = np.split(a, 2, axis=0)
print("Part 1:\n", x)
print("Part 2:\n", y)

Output: Two parts, each of shape (1, 4, 4).

17. Split 17 elements into 4 parts

print("\n17. Array Split")
a = np.arange(17)
for part in np.array_split(a, 4):
print(part, "Size:", part.size)

Output:

[0 1 2 3 4] Size: 5

[5 6 7 8] Size: 4

[ 9 10 11 12] Size: 4

[13 14 15 16] Size: 4

18. Identify and remove outliers

print("\n18. Outliers")
a = np.array([10, 12, 11, 13, 12, 11, 100])
m, s = np.mean(a), np.std(a)
outliers = a[np.abs(a - m) > 2 * s]
clean = a[np.abs(a - m) <= 2 * s]
print("Outliers:", outliers)
print("Clean array:", clean)

Output:

Outliers: [100]

Clean array: [10 12 11 13 12 11]

19. Student and subject averages

print("\n19. Averages")
marks = np.array([
[80, 85, 90, 75],
[70, 75, 80, 85],
[90, 95, 85, 80],
[60, 70, 75, 80],
[85, 80, 90, 95]
])
print("Student averages:", marks.mean(axis=1))
print("Subject averages:", marks.mean(axis=0))

Output:

Student averages: [82.5  77.5  87.5  71.25 87.5 ]

Subject averages: [77. 81. 84. 83.]

20. Correlation coefficient

print("\n20. Correlation")
a = np.array([10, 20, 30, 40, 50])
b = np.array([15, 25, 35, 45, 55])
print(np.corrcoef(a, b))

Output:

[[1. 1.]

[1. 1.]]

21. Save and reload CSV

print("\n21. CSV File")
a = np.random.randint(1, 100, (5, 5))
np.savetxt("data.csv", a, delimiter=",", fmt="%d")
b = np.loadtxt("data.csv", delimiter=",", dtype=int)
print("Original:\n", a)
print("Loaded:\n", b)
print("Match:", np.array_equal(a, b))

Output: Original and loaded arrays match.

Match: True

22. Save three arrays in NPZ

print("\n22. NPZ File")
np.savez(
"arrays.npz",
first=np.array([1, 2, 3]),
second=np.array([[4, 5], [6, 7]]),
third=np.array([8, 9, 10, 11])
)
data = np.load("arrays.npz")
print("Array names:", data.files)
data.close()

Output:

Array names: ['first', 'second', 'third']

23. Random 3x3 matrix and sort rows

print("\n23. Sort Rows")
a = np.random.randint(10, 51, (3, 3))
print("Original:\n", a)
print("Sorted:\n", np.sort(a, axis=1))

Output: Random matrix and sorted rows are printed.

24. Biased coin simulation

print("\n24. Biased Coin")
a = np.random.binomial(1, 0.7, 200)
print("Heads:", a.sum())
print("Proportion:", a.mean())

Output: Heads count and proportion are printed.

Results vary because the simulation is random.

25. Normal distribution

print("\n25. Normal Distribution")
a = np.random.normal(0, 2, 2000)
count = np.sum((a < -4) | (a > 4))
print("Outside [-4, 4]:", count)

Output: Random count, usually around 90 to 100.

26. Poisson website visits

print("\n26. Poisson Distribution")
a = np.random.poisson(5, 60)
print("Visits:", a)
print("Highest visits:", a.max())
print("Minute:", np.argmax(a) + 1)
 26. Poisson website visits
print("\n26. Poisson Distribution") a = np.random.poisson(5, 60) print("Visits:", a) print("Highest visits:", a.max()) print("Minute:", np.argmax(a) + 1)
Output: Visits per minute, maximum and minute number..
27. Multinomial survey

print("\n27. Multinomial Distribution")
a = np.random.multinomial(200, [0.5, 0.3, 0.2])
print("Product 1:", a[0])
print("Product 2:", a[1])
print("Product 3:", a[2])
print("Total:", a.sum())

Output: Product counts vary; total is always 200.

28. Shuffle a deck and deal 5 cards

print("\n28. Shuffle Deck")
deck = np.random.permutation(np.arange(1, 53))
print("Shuffled deck:", deck)
print("Hand of 5 cards:", deck[:5])

Output: Random shuffled deck and five cards.
