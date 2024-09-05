'''
2)	Write a Python Program and perform the following operations ?
I.	Create a List {1225, 4986, 6789, 7890, 2345, 6783, 0987, 1234, 8765, 3456}
II.	Iterate using a for loop
III.	Iterate using for loop and range
IV.	List Comprehension
V.	Enumerate
VI.	Iter function and next function
VII.	Map function
VIII.	Using zip
IX.	Using NumPy Module

'''


import numpy as np

# I. Create a List
num_list = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# II. Iterate using a for loop
print("II. Iterate using a for loop:")
for num in num_list:
    print(num, end=" ")
print("\n")

# III. Iterate using for loop and range
print("III. Iterate using for loop and range:")
for i in range(len(num_list)):
    print(num_list[i], end=" ")
print("\n")

# IV. List Comprehension
print("IV. List Comprehension:")
squares = [num**2 for num in num_list]
print("Squares:", squares)
print("\n")

# V. Enumerate
print("V. Enumerate:")
for index, num in enumerate(num_list):
    print(f"Index {index} has value {num}")
print("\n")

# VI. Iter function and next function
print("VI. Iter function and next function:")
iter_nums = iter(num_list)
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print("\n")

# VII. Map function
print("VII. Map function:")
doubled = list(map(lambda x: x * 2, num_list))
print("Doubled values:", doubled)
print("\n")

# VIII. Using zip
print("VIII. Using zip:")
list1 = [1, 2, 3, 4, 5]
zipped = list(zip(list1, num_list))
print("Zipped list1 with num_list:", zipped)
print("\n")

# IX. Using NumPy Module
print("IX. Using NumPy Module:")
np_array = np.array(num_list)
print("NumPy array:", np_array)
print("NumPy array + 10:", np_array + 10)


# Result

''' 
II. Iterate using a for loop:
1225 4986 6789 7890 2345 6783 987 1234 8765 3456 

III. Iterate using for loop and range:
1225 4986 6789 7890 2345 6783 987 1234 8765 3456 

IV. List Comprehension:
Squares: [1500625, 24860196, 46090521, 62252100, 5499025, 46009089, 974169, 1522756, 76825225, 11943936]


V. Enumerate:
Index 0 has value 1225
Index 1 has value 4986
Index 2 has value 6789
Index 3 has value 7890
Index 4 has value 2345
Index 5 has value 6783
Index 6 has value 987
Index 7 has value 1234
Index 8 has value 8765
Index 9 has value 3456


VI. Iter function and next function:
1225
4986
6789


VII. Map function:
Doubled values: [2450, 9972, 13578, 15780, 4690, 13566, 1974, 2468, 17530, 6912]

VIII. Using zip:
Zipped list1 with num_list: [(1, 1225), (2, 4986), (3, 6789), (4, 7890), (5, 2345)]

IX. Using NumPy Module:
NumPy array: [1225 4986 6789 7890 2345 6783  987 1234 8765 3456]
NumPy array + 10: [1235 4996 6799 7900 2355 6793  997 1244 8775 3466]

'''