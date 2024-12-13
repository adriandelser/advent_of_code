import numpy as np
import matplotlib.pyplot as plt
import time

# Initialize the array
array = np.random.randint(0, 2, (10, 10))  # 10x10 array of 0s and 1s

# Set up the plot
fig, ax = plt.subplots()
im = ax.imshow(array, cmap='gray', interpolation='nearest')

# Function to update the array
def update_array(array):
    # Example: Randomly flip one cell per iteration
    x, y = np.random.randint(0, array.shape[0]), np.random.randint(0, array.shape[1])
    array[x, y] = 1 - array[x, y]  # Flip between 0 and 1
    return array

# While loop for changes
while True:
    # Update the array
    array = update_array(array)
    
    # Update the imshow plot
    im.set_array(array)
    
    # Redraw the plot
    plt.draw()
    plt.pause(0.1)  # Pause for animation effect
    
    # Optional: Break condition for the loop
    if np.random.rand() < 0.01:  # Break randomly for demonstration
        break

plt.show()
