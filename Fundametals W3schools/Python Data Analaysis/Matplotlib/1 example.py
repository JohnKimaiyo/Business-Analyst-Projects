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
