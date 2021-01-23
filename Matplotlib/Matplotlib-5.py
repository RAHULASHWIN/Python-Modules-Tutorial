import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data1.csv')
ages = data['Age1']
dev_salaries = data['All_Devs1']
py_salaries = data['Python1']
js_salaries = data['JavaScript1']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs1')

plt.plot(ages, py_salaries, label='Python1')

overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, alpha=0.25, label='Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, color='red', alpha=0.25, label='Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()