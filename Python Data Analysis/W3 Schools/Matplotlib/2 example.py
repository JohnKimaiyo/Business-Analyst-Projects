import matplotlib.pyplot as plt

# inittailizing the data
x =  [20,30,40,50]
y = [30,40,50,60]

# plotting the data
plt.plot(x,y)

# adding the title
plt.title("Simple Plot")

# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()


#example 2
# python program to show pyplot module
import matplotlib.pyplot as plt
plt.plot([2,3,4,5],[2,5,10,11])
plt.axis([1,7,1,21])
plt.show()