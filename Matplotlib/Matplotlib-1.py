print("Hello Rahul!") # Sample Code

from matplotlib import pyplot as plt #here you import matplotlib as plt

#print(plt.style.available)

#plt.style.use('fivethirtyeight')  #This is one of the inbuild function for styling

plt.xkcd()#this is also for styling in a comical way

dev_x = [25,27,28,29,30,31,32] #This is the data for the x-axis

dev_y = [38496, 42000, 46752, 53200,
        56000, 62316, 64928]  # This is the data for the y-axis

plt.plot(dev_x, dev_y, 'k--o',label='Rahul')  # In this one you plot the data and give the name as Rahul

dev_y1 = [384961, 420001, 467521, 532001,
        560001, 623161, 649281]

plt.plot(dev_x, dev_y1, 'b-.o',label='Ashwin') # In this one you plot the data and give the name as Ashwin

plt.xlabel('Ages')  # This is for adding label to the x-axis
plt.ylabel('Median Slary (USD)') # this is for adding label to the y-axis
plt.title('Median Salary (USD) by Age') # This is for adding title 
plt.legend()  # This one places the data on the right position gaining the data of the x and y axis
# and another purpose is to that for showing the labels in the window which we are going to show
plt.show()  # This is for showing the data in another window