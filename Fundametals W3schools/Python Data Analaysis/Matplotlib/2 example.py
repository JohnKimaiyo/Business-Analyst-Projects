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