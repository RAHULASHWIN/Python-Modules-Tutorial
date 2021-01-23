import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    row = next(csv_reader)
    print(row)







"""
ages_x = [25, 27, 28, 29, 30, 31, 32]

x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 53200,
         56000, 62316, 64928]
plt.bar(x_indexes+width, dev_y,width=width, color="blue",label="world")

dev_y1 = [384961, 420001, 467521, 532001,
          560001, 623161, 649281]
plt.bar(x_indexes-width, dev_y1, width=width,color="green", label="hello")

dev_y2 = [3849612, 4200012, 4675212, 5320012,
          5600012, 6231612, 6492812]
plt.bar(x_indexes, dev_y2,width=width, color="yellow", label="hello")

dev_y3 = [3849612, 4200012, 4675212, 5320012,
          5600012, 6231612, 6492812]
plt.bar(x_indexes+width, dev_y3,width=width, color="black", label="hello")

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("salaried")
plt.legend()

plt.tight_layout()
plt.show()
"""