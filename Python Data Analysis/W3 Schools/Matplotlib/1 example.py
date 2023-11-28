import matplotlib.pyplot as plt 
  
# initializing the data 
x = [10, 20, 30, 40] 
y = [20, 30, 40, 50] 
  
# plotting the data 
plt.plot(x, y) 
  
# Adding the title 
plt.title("Simple Plot") 
  
# Adding the labels 
plt.ylabel("y-axis") 
plt.xlabel("x-axis") 
plt.show()


# Python progrsm to show pyplot module
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,10])
plt.axis([0,6,0,20])
plt.show()


# Python program to show pyplot module 
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure 

# Creating a new figure with width = 5 inches 
# and height = 4 inches 
fig = plt.figure(figsize =(5, 4)) 

# Creating a new axes for the figure 
ax = fig.add_axes([1, 1, 1, 1]) 

# Adding the data to be plotted 
ax.plot([2, 3, 4, 5, 5, 6, 6], 
		[5, 7, 1, 3, 4, 6 ,8]) 
plt.show()
