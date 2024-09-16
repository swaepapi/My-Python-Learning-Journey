#Importing libraries
# Pandas
import pandas as pd

# Import Pandas with alias
import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create a DataFrame using the data
df = pd.DataFrame(data)

# Display the DataFrame
print(df)


#Numpy

import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print ("1D array:", arr1)

# Create a 2D array
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print("2D array:\n", arr2)

# Basic operations
print("Sum of all elements in arr1:", np.sum(arr1))  # Sum of array elements
print("Mean of arr1:", np.mean(arr1))  # Mean of the array

# Reshape the array
reshaped_arr = arr2.reshape(2, 3)
print ("Reshaped array:\n", reshaped_arr)


#Matplotlib

import matplotlib.pyplot as plt

# Data to plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a line plot
plt.plot(x, y, label='Line 1')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Plot')

# Show the plot
plt.legend()  # Display legend
plt.show()


# Data to plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 10]

# Create a bar plot
plt.bar(categories, values, color='skyblue')

# Adding labels and title
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Chart Example')

# Show the plot
plt.show()





