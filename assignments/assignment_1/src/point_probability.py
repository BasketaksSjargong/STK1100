# A small python script for calculating the point
# probability in problem 2, first mandatory assignment
# STK1100, V15 UiO.

import matplotlib.pyplot as plt

# Reading data file
age = []
death_prob = []
year_offset = 30
with open("dodelighet-oblig1.txt", 'r') as data_file:
  data_file.next()
  for line in data_file:
    age.append(int(line.split()[0]))
    death_prob.append(float(line.split()[1])/1000)

def S(x):
  prob_of_living = 1
  for y in range(0, x):
    prob_of_living *= (1 - death_prob[y + year_offset])
  return prob_of_living

def p(x):
  return (1 - S(x)) - (1-S(x-1))

point_prob = []
for x in range(76+1):
  point_prob.append(p(x))

plt.axes([0, 100, 0, 0.05])
plt.plot(range(0, 77), point_prob)
plt.legend(["$p(x), \quad x = 0, 1, \ldots, 76$"])
plt.show()