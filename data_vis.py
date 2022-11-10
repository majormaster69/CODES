import pandas as pd
import matplotlib.pyplot as plt
# reading the database
x = [32,31,64,78]
y = [76,12,65,32]
data=list(zip(x,y))
# Scatter plot
#plt.scatter(data[day], data[tip])
# Adding Title to the Plot
#plt.title("Scatter Plot")
# Setting the X and Y labels
plt.xlabel("day")
plt.ylabel("tip")
plt.show()
# Histogram
plt.hist(data)
plt.title("Histogram")
plt.show()
