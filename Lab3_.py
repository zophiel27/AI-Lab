"""Q1 - Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order in linear time.
"""

def Merge(l1, l2):
  l3 = []
  i = 0
  j = 0
  #if len(l1) >= len(l2):
  while(i < len(l1) and j < len(l2)):
    if(l1[i]<=l2[j]):
      l3.append(l1[i])
      i+=1
    else:
      l3.append(l2[j])
      j+=1

  if(i < len(l1)):
    while(i < len(l1)):
      l3.append(l1[i])
      i+=1
  if(j < len(l2)):
    while(j < len(l2)):
      l3.append(l2[j])
      j+=1
  return l3

#main
l1= [1, 4, 6, 10]
l2= [2, 3, 6]
l3 = Merge(l1, l2)
print(l3)

"""Q2 - Initialize dictionary with default values. One line solution."""

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

my_dictionary = {employees[i]:defaults for i in range(len(employees))}
print(my_dictionary)

"""Q3 - Delete set of keys from a dictionary. Give one line solution.

"""

sampleDict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york" }
keysToRemove = ["name", "salary"]

for keys in keysToRemove: del sampleDict[keys]
print(sampleDict)

"""Q4 - Consider two sets X and Y. You may take any type of values for these sets. Try to find a solution to get a set having all elements in either X or Y, but not both."""

X={1,4,5,'ABC'}
Y={1,2,5,'AAA'}

X.union(Y)-X.intersection(Y)

"""Q5 - Write a function to divide two numbers P and Q. Implement exception handling
technique
(try..except clause) for handling possible exceptions in the scenario.
"""

P= 2
Q= 0
try:
  num = P / Q
except ValueError: print("You should have given either an int or a float")
except ZeroDivisionError: print("Infinity")

print(num)
