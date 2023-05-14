import numpy as np

my_array = np.random.random(100)
my_array[my_array == np.max(my_array)] = 1
my_array[my_array == np.min(my_array)] = 0

#print(np.max(my_array), np.min(my_array))
#print(my_array)


my_array = np.random.randint(0,50,[5,6])## Your code here
selected_column = my_array[my_array.max(axis = 0).argmax()]## Your code here
print('Shape: ',my_array.shape)
print('Array')
print(my_array)
print(selected_column)