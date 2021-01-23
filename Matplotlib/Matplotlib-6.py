import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data2.csv')
ids = data['Responder_id']
ages = data['Age']

#ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [5,10,15,20,25,30,40,50,60,70,80,90,100]

plt.hist(ages, bins=5, edgecolor='black',log = True)

median_age = 29
color = 'red'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

# median_age = 29
# color = '#fc4f30'

# plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()

"""
Difference between Histogram and Bargraph
 
HISTOGRAM

* In Histogram there is no space betweeen the bars.
* It is based on Quantitative Data i.e it can have only numerical data on x and y axis
* Here the bars can't be reordered

BARGRAPH

* In Bargraph there is space between each and every bar graph
* In this one the bars can be reordered
* It is based on Qualitative Data
"""