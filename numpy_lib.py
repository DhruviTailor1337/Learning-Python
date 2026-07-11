# """
# ===============================================================================
#                     NUMPY STEP-BY-STEP NOTES + EXAMPLES
# ===============================================================================

# File Name:
# 03_numpy_step_by_step_notes.py

# How to use this file:
# 1. Open this file in VS Code.
# 2. Read each topic in order.
# 3. Run the file.
# 4. Try the practice questions after each topic.

# Learning Flow:
# 1. Definition of NumPy
# 2. Why NumPy is needed
# 3. Where NumPy is used
# 4. Installation
# 5. Importing NumPy
# 6. NumPy version check
# 7. Python List vs NumPy Array
# 8. Creating NumPy Arrays
# 9. Array dimensions
# 10. Array attributes
# 11. Indexing
# 12. Slicing
# 13. Array creation functions
# 14. Mathematical operations
# 15. Statistical functions
# 16. Filtering
# 17. Sorting
# 18. Reshaping
# 19. Random numbers
# 20. Mini project
# 21. Quiz
# 22. Practice questions
# 23. Homework
# """

# # =============================================================================
# # 1. WHAT IS NUMPY?
# # =============================================================================

# """
# Definition:
# -----------
# NumPy stands for Numerical Python.

# NumPy is a Python library used for numerical and mathematical calculations.

# In simple words:
# NumPy helps us work with numbers, arrays, matrices, and large datasets easily.

# Why the name NumPy?
# -------------------
# Num  -> Numerical
# Py   -> Python

# So NumPy means Numerical Python.

# Main object of NumPy:
# ---------------------
# The main object in NumPy is called ndarray.

# ndarray means:
# n-dimensional array

# Array means a collection of values.

# Example:
# Marks of students:
# [80, 75, 90, 88, 67]

# This can be stored as a NumPy array.
# """

# # =============================================================================
# # 2. WHY DO WE NEED NUMPY?
# # =============================================================================

# """
# Python already has Lists.
# Then why do we need NumPy?

# Python List Example:
# marks = [80, 75, 90, 88, 67]

# Lists are good for normal programming, 
# but they are not best for large numerical data.

# Problems with Python Lists:
# ---------------------------
# 1. Slower for large calculations
# 2. Uses more memory
# 3. Mathematical operations are not direct
# 4. Not suitable for large datasets
# 5. Not ideal for Data Science and Machine Learning

# NumPy solves these problems.

# Benefits of NumPy:
# ------------------
# 1. Faster than Python Lists
# 2. Uses less memory
# 3. Supports mathematical operations directly
# 4. Supports multi-dimensional arrays
# 5. Used in Data Science, AI, ML, Deep Learning
# 6. Works with Pandas, Matplotlib, Scikit-learn, TensorFlow
# """

# # =============================================================================
# # 3. REAL LIFE EXAMPLE
# # =============================================================================

# """
# Imagine you are analyzing marks of 10 lakh students.

# Without NumPy:
# --------------
# You may use Python Lists.
# But calculations like average, maximum, minimum, standard deviation will be slower.

# With NumPy:
# -----------
# You can calculate everything easily and quickly.

# Example:
# np.mean(marks)
# np.max(marks)
# np.min(marks)

# This is why NumPy is important in Data Science.
# """

# # =============================================================================
# # 4. WHERE IS NUMPY USED?
# # =============================================================================

# """
# NumPy is used in:

# 1. Data Science
# 2. Machine Learning
# 3. Artificial Intelligence
# 4. Deep Learning
# 5. Image Processing
# 6. Computer Vision
# 7. Scientific Computing
# 8. Statistics
# 9. Financial Analysis
# 10. Data Analysis
# 11. Matrix Operations
# 12. Engineering Calculations
# """

# # =============================================================================
# # 5. HOW TO INSTALL NUMPY
# # =============================================================================

# """
# Before using NumPy, we need to install it.

# Open VS Code Terminal and write:

# # install NumPy
# pip install numpy

# # wanna see installed linbrary
# pip list


# If you are using Jupyter Notebook, write:

# !pip install numpy

# To check if NumPy is installed:

# pip show numpy

# To upgrade NumPy:

# pip install --upgrade numpy

# To uninstall NumPy:

# pip uninstall numpy

# Important:
# ----------
# You install NumPy only one time in your environment.
# After installation, you can import it in any Python file.
# """

# # =============================================================================
# # 6. HOW TO IMPORT NUMPY
# # =============================================================================

# """
# After installation, we need to import NumPy.

# Syntax:
# -------
# import numpy as np

# Explanation:
# ------------
# import  -> Python keyword used to bring a library into our file
# numpy   -> Library name
# as      -> Used to give a short name / alias
# np      -> Short name for numpy

# Why do we write np?
# -------------------
# Because writing numpy again and again is long.

# Instead of:
# numpy.array()

# We write:
# np.array()

# np is the industry standard alias for NumPy.
# """

import numpy as np

print("NumPy imported successfully!")

# # =============================================================================
# # 7. CHECK NUMPY VERSION
# # =============================================================================

# """
# To check the version of NumPy:

# np.__version__

# Why check version?
# ------------------
# Sometimes old versions may not support new features.
# """

print("NumPy Version:", np.__version__)

# # =============================================================================
# # 8. PYTHON LIST VS NUMPY ARRAY
# # =============================================================================

# """
# Python List:
# ------------
# A list is a collection of items.
# It can store different data types.

# Example:
# [10, "Python", 45.5, True]

# NumPy Array:
# ------------
# A NumPy array is a collection of values, usually of the same data type.

# Example:
# [10, 20, 30, 40]

# Important Difference:
# ---------------------
# List is general purpose.
# NumPy array is made for numerical calculation.
# """

python_list = [10, 20, 30, 40, 50] # List
numpy_array = np.array([10, 20, 30, 40, 50]) # NumPy Array

print("Python List:", python_list)
print("NumPy Array:", numpy_array)

# # Example: Multiply by 2

print("List multiplied by 2:", python_list * 2)
print("Array multiplied by 2:", numpy_array * 2)

# """
# Output Explanation:
# -------------------
# python_list * 2 repeats the list.
# numpy_array * 2 multiplies every element by 2.

# This is one of the biggest advantages of NumPy.
# """

# # =============================================================================
# # 9. CREATING NUMPY ARRAY
# # =============================================================================

# """
# To create a NumPy array, we use:

# np.array()

# Syntax:
# -------
# variable_name = np.array([values])
# """

# arr = np.array([1, 2, 3, 4, 5])

# print("Array:", arr)
# print("Type:", type(arr))

# """
# Output Explanation:
# -------------------
# type(arr) gives:
# <class 'numpy.ndarray'>

# ndarray means n-dimensional array.
# """

# # Practice:
# """
# Q1. Create an array of numbers from 10 to 50.
# Q2. Create an array of 5 student marks.
# Q3. Print the type of array.
# """

# # =============================================================================
# # 10. TYPES OF NUMPY ARRAYS BASED ON DIMENSION
# # =============================================================================

# """
# Dimension means level/depth of array.

# 1D Array:
# ---------
# Single row of values.

# Example:
# [10, 20, 30]

# 2D Array:
# ---------
# Rows and columns.
# Like a table or matrix.

# Example:
# [[10, 20, 30],
#  [40, 50, 60]]

# 3D Array:
# ---------
# Collection of 2D arrays.
# Used in images, deep learning, etc.
# """

# 1D Array
arr_1d = np.array([10, 20, 30])  # 1 row 3 columns
print("1D Array:")
print(arr_1d)

# 2D Array
arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60]]) # # 2 rows, 3 columns
print("2D Array:")
print(arr_2d)

# 3D Array
arr_3d = np.array([[[1, 2], [3, 4]], 
                   [[5, 6], [7, 8]]]) # 2 blocks, 2 rows, 2 columns
print("3D Array:")
print(arr_3d)

# # =============================================================================
# # 11. ARRAY ATTRIBUTES
# # =============================================================================

# """
# Array attributes give information about an array.

# Important attributes:
# ---------------------

# 1. ndim
#    Shows number of dimensions.

# 2. shape
#    Shows rows and columns.

# 3. size
#    Shows total number of elements.

# 4. dtype
#    Shows datatype of elements.

# 5. itemsize
#    Shows memory size of one element.

# 6. nbytes
#    Shows total memory used by array.
# """

arr = np.array([[10, 20, 30],
                [40, 50, 60]])  # 2D array with 2 rows and 3 columns

print("Array:")
print(arr)

print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape) # (row, column)
print("Total elements:", arr.size)
print("Datatype:", arr.dtype)
print("Memory of one element:", arr.itemsize)
print("Total memory:", arr.nbytes)

# """
# Example Explanation:
# --------------------
# Shape is (2, 3)

# This means:
# 2 rows
# 3 columns
# """

# # Practice:
# """
# Q1. Create a 3x3 array.
# Q2. Print ndim.
# Q3. Print shape.
# Q4. Print size.
# Q5. Print dtype.
# """

# # =============================================================================
# # 12. INDEXING IN NUMPY
# # =============================================================================

# """
# Indexing means accessing a single 
# element from an array.

# Python indexing starts from 0.

# Example:
# Array:  [10, 20, 30, 40]
# Index:    0   1   2   3

# Negative Index:
# Array:  [10, 20, 30, 40]
# Index:   -4  -3  -2  -1
# """

arr = np.array([10, 20, 30, 40])  # 1 row 4 column

print("First element:", arr[0]) # 10
print("Third element:", arr[2]) # 30
print("Last element:", arr[-1]) # 40

# # 2D Indexing
# """
# For 2D array:

# array[row_index, column_index]
# """

arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60]])

print("Element at row 0 column 1:", arr_2d[0, 1]) # ([row, col]) # 20
print("Element at row 1 column 2:", arr_2d[1, 2]) # 60

# # Practice:
# """
# Q1. Create an array 
arr = np.array([5, 10, 15, 20, 25])

# Q2. Print first element.
print("First element:", arr[0])
# Q3. Print last element.
print("Last element:", arr[-1])
# Q4. Create 2D array and access middle element.
var = np.array([[1, 2, 3], 
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]]) # 4 rows, 3 columns

# Q5. Access element 11 using negative indexing.
print("Element 11 using negative indexing:", var[-1, -2])
# Q6. Access element 3 using positive indexing.
print("Element 3 using positive indexing:", var[0, 2])
# """

# # =============================================================================
# # 13. SLICING IN NUMPY
# # =============================================================================

# """
# Slicing means accessing a range of elements.

# Syntax:
# -------
# array[start : stop : step]

# Important:
# ----------
# stop index is not included.
# """

arr = np.array([10, 20, 30, 40, 50, 60])
            #    0,  1,  2,  3,  4,  5

print("From index 1 to 4:", arr[1:5])
print("From start to index 3:", arr[:4])
print("From index 2 to end:", arr[2:])
print("Every second element:", arr[::2])
print("Reverse array:", arr[::-1])

# # 2D Slicing

arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print("First row:", arr_2d[0]) # Access first row
print("First column:", arr_2d[:, 0]) # Access first column
print("First two rows:")
print(arr_2d[:2]) # Access first two rows
print("First two columns:")
print(arr_2d[:, :2]) # Access first two columns

# # =============================================================================
# # 14. CREATING ARRAYS USING BUILT-IN NUMPY FUNCTIONS
# # =============================================================================

# """
# NumPy provides many functions to create arrays quickly.
# """

# # zeros()
# """
# np.zeros() creates an array filled with 0.
# """

zeros_array = np.zeros((2, 3))
print("Zeros Array:")
print(zeros_array)

# # ones()
# """
# np.ones() creates an array filled with 1.
# """

ones_array = np.ones((3, 2))
print("Ones Array:")
print(ones_array)

# # arange()
# """
# np.arange() works like range(), 
# but returns NumPy array.

# Syntax:
# np.arange(start, stop, step)
# """

range_array = np.arange(1, 11)
print("Arange Array:", range_array)

even_numbers = np.arange(2, 21, 2)
print("Even Numbers:", even_numbers)

# # linspace()
# """
# np.linspace() creates equally spaced numbers.

# Syntax:
# np.linspace(start, stop, number_of_values)
# """

line_array = np.linspace(1, 10, 3)
print("Linspace Array:", line_array)

# # eye()
# """
# np.eye() creates identity matrix.
# Identity matrix has 1 on diagonal and 0 elsewhere.
# """

identity_matrix = np.eye(3) 
print("Identity Matrix:")
print(identity_matrix)

# # =============================================================================
# # 15. MATHEMATICAL OPERATIONS
# # =============================================================================

# """
# NumPy allows direct mathematical 
# operations on arrays.
# """

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Power:", a ** 2)

# """
# Important:
# ----------
# Operations happen element by element.

a = [10, 20, 30]
b = [1, 2, 3]
a + b = [11, 22, 33]

# """

# # =============================================================================
# # 16. STATISTICAL FUNCTIONS
# # =============================================================================

# """
# Statistics is very important in Data Science.

# Common NumPy statistical functions:

# 1. np.sum()     -> total
# 2. np.mean()    -> average
# 3. np.median()  -> middle value
# 4. np.max()     -> maximum value
# 5. np.min()     -> minimum value
# 6. np.std()     -> standard deviation
# 7. np.var()     -> variance
# """

marks = np.array([78, 85, 90, 65, 88])

print("Marks:", marks)
print("Total:", np.sum(marks)) # 
print("Average:", np.mean(marks)) 
print("Median:", np.median(marks)) 
print("Highest:", np.max(marks)) 
print("Lowest:", np.min(marks)) 
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))

# # =============================================================================
# # 17. FILTERING ARRAYS
# # =============================================================================

# """
# Filtering means selecting values based on condition.

# Example:
# Select marks greater than 70.
# """

marks = np.array([45, 80, 67, 92, 33, 75])

passed_students = marks[marks >= 35]
top_students = marks[marks >= 75]

print("Passed Students Marks:", passed_students)
print("Top Students Marks:", top_students)

# """
# Explanation:
# ------------
# marks >= 75 creates True/False values.
# NumPy uses those True/False values to filter data.
# """

# # =============================================================================
# # 18. SORTING ARRAYS
# # =============================================================================

# """
# Sorting means arranging values in order.
# """

numbers = np.array([50, 10, 80, 30, 20])

sorted_numbers = np.sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)
print("Descending:", sorted_numbers[::-1])

# # =============================================================================
# # 19. RESHAPING ARRAYS
# # =============================================================================

# """
# Reshape means changing the shape of an array.

# Important Rule:
# ---------------
# Total number of elements must remain same.

# Example:
# 6 elements can be reshaped into:
# 2x3
# 3x2
# 1x6
# 6x1
# """

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original:", arr)
print("2x3:")
print(arr.reshape(2, 3)) # 2 rows 3 columns
print("3x2:")
print(arr.reshape(3, 2)) # 3 rows 2 columns

# # =============================================================================
# # 20. RANDOM NUMBERS IN NUMPY
# # =============================================================================

# """
# NumPy can generate random numbers.

# Used in:
# - Machine Learning
# - Simulations
# - Games
# - Random sampling
# - OTP style examples
# """

# # Random integers
# 1. np.random.randint(start, stop, size)
random_numbers = np.random.randint(1, 100, 5)
print("Random Integers:", random_numbers)

# Random decimal values between 0 and 1
# 2. np.random.rand(size)
random_decimal = np.random.rand(5)
print("Random Decimal Numbers:", random_decimal)

# Random 2D matrix
random_matrix = np.random.randint(1, 10, (3, 3)) 
#(3 rows, 3 columns)
print("Random Matrix:")
print(random_matrix)

# # =============================================================================
# # 21. BROADCASTING
# # =============================================================================

# """
# Broadcasting means NumPy automatically performs 
# operations between arrays of different shapes when 
# possible.

# Simple Example:
# ---------------
# Array + single number
# """

arr = np.array([10, 20, 30])

print("Add 5:", arr + 5)
print("Multiply by 2:", arr * 2)

# """
# Here 5 is added to every element.
# This is broadcasting.
# """

# # =============================================================================
# # 22. COMMON MISTAKES
# # =============================================================================

# """
# Mistake 1:
# Forgetting to import NumPy.

# Wrong:
# arr = np.array([1,2,3])

# Correct:
# import numpy as np
# arr = np.array([1,2,3])


# Mistake 2:
# Wrong reshape size.

# Wrong:
# np.array([1,2,3,4,5]).reshape(2,3)

# Because 5 elements cannot become 2x3 matrix.


# Mistake 3:
# Confusing shape and size.

# shape -> rows and columns
# size  -> total elements


# Mistake 4:
# Using list logic with arrays.

# List * 2 repeats list.
# Array * 2 multiplies each element.
# """

# # =============================================================================
# # 23. MINI PROJECT: STUDENT MARKS ANALYSIS
# # =============================================================================

# """
# Project Objective:
# Analyze marks of students using NumPy.

# Tasks:
# 1. Store marks
# 2. Find highest marks
# 3. Find lowest marks
# 4. Find average marks
# 5. Find passed students
# 6. Find top students
# 7. Sort marks
# """

student_marks = np.array([88, 45, 76, 92, 67, 34, 59, 81])

print("----- Student Marks Analysis -----")
print("Marks:", student_marks)
print("Highest Marks:", np.max(student_marks))
print("Lowest Marks:", np.min(student_marks))
print("Average Marks:", np.mean(student_marks))
print("Passed Marks:", student_marks[student_marks >= 35])
print("Top Marks:", student_marks[student_marks >= 75])
print("Sorted Marks:", np.sort(student_marks))

# # =============================================================================
# # 24. QUICK QUIZ
# # =============================================================================

# """
# Q1. What is the full form of NumPy?
# A. Numerical Python

# Q2. What is the main object of NumPy?
# A. ndarray

# Q3. Which command is used to install NumPy?
# A. pip install numpy

# Q4. How do we import NumPy?
# A. import numpy as np

# Q5. What is the difference between list and NumPy array?
# A. List is general purpose. NumPy array is faster for numerical operations.

# Q6. What does ndim return?
# A. Number of dimensions.

# Q7. What does shape return?
# A. Rows and columns.

# Q8. What does size return?
# A. Total number of elements.

# Q9. Which function creates an identity matrix?
# A. np.eye()

# Q10. Which function gives average?
# A. np.mean()
# """

# # =============================================================================
# # 25. PRACTICE QUESTIONS
# # =============================================================================

# """
# Practice Set:

# Q1. Create a NumPy array of numbers from 1 to 10.

# Q2. Create a NumPy array of 5 student marks.

# Q3. Print:
#     - ndim
#     - shape
#     - size
#     - dtype

# Q4. Create a 2D array with 3 rows and 3 columns.

# Q5. Access the first element of a 1D array.

# Q6. Access the last element using negative indexing.

# Q7. Access one element from a 2D array.

# Q8. Slice first 3 elements from an array.

# Q9. Reverse an array.

# Q10. Create an array of even numbers from 2 to 20.

# Q11. Create an array of 5 equally spaced numbers between 1 and 100.

# Q12. Create a 4x4 identity matrix.

# Q13. Add two arrays.

# Q14. Multiply two arrays.

# Q15. Find mean, median, max, min from marks.

# Q16. Filter marks greater than 60.

# Q17. Sort an array.

# Q18. Reshape 1D array of 12 elements into 3x4.

# Q19. Generate 10 random numbers between 1 and 50.

# Q20. Create a 3x3 random matrix.
# """

# # =============================================================================
# # 26. HOMEWORK
# # =============================================================================

# """
# Homework:

# Create a new file:
# homework_numpy.py

# Complete these tasks:

# 1. Student Marks Analyzer
#    - Create marks array
#    - Find total
#    - Find average
#    - Find highest
#    - Find lowest
#    - Find students above 75
#    - Sort marks

# 2. Sales Analysis
#    - Create sales array for 7 days
#    - Find total sales
#    - Find average sales
#    - Find highest sales day
#    - Find lowest sales day

# 3. Temperature Analysis
#    - Create temperature array for 10 days
#    - Find average temperature
#    - Find maximum temperature
#    - Find minimum temperature
#    - Filter days where temperature > 35

# 4. Matrix Practice
#    - Create 3x3 matrix
#    - Print shape
#    - Print size
#    - Print first row
#    - Print first column
#    - Print diagonal values

# 5. Random Practice
#    - Generate 6 digit OTP using NumPy
#    - Generate 5x5 random matrix
#    - Generate random marks for 20 students
# """

# # =============================================================================
# # 27. CHAPTER SUMMARY
# # =============================================================================

# """
# Today you learned:

# 1. Definition of NumPy
# 2. Need of NumPy
# 3. Uses of NumPy
# 4. Installation command
# 5. Import statement
# 6. NumPy version check
# 7. List vs NumPy Array
# 8. Creating arrays
# 9. 1D, 2D, 3D arrays
# 10. Array attributes
# 11. Indexing
# 12. Slicing
# 13. zeros, ones, arange, linspace, eye
# 14. Mathematical operations
# 15. Statistical functions
# 16. Filtering
# 17. Sorting
# 18. Reshaping
# 19. Random numbers
# 20. Mini project
# """

# print("NumPy step-by-step notes completed.")
