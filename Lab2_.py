"""
Question 5.1
"""

# Check if a given element in a list is divisible by 3 or not
def checkDivisibility(ls):
  output = []
  for x in ls:
    if(x%3==False):
      output.append(x)
  return output

#main
ls= [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
out = checkDivisibility(ls)
print(out)

"""Question 5.2"""

# Given 2 strings, a and b, return a string of the form: a-front + b-front + a-back + b-back
def frontBack(s1, s2):
  output= ""
  output+= s1[:-(len(s1)//2)]
  output+= s2[:-(len(s2)//2)]
  output+= s1[-(len(s1)//2):]
  output+= s2[-(len(s2)//2):]
  return output

#main
input1 = "abcde"
input2= "pqrst"
output = frontBack(input1, input2)
print(output)

"""Question 5.3"""

# Transpose of a matrix
def transpose(X):
  result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
  return result

#main
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
output = transpose(matrix)
for i in output:
   print(i)

"""Question 5.4"""

# Sort a tuple of tuples by 2nd item
#main
tuple1 = (('a', 23),
          ('c', 37),
          ('b', 11),
          ('d', 29))

print(sorted(tuple1, key = lambda x: x[1])) #key becomes function and takes parameter x(tuple) and returns its 2nd digit or value (x[1])

"""Question 5.5"""

# Write a function which returns a tuple that is formed by multiplying adjacent elements

def multiplyAdjacent(t):
  # Using the tuple() method to make a tuple
  return tuple(x * y for x, y in zip(t, t[1:])) #t[:1] so it doesnt go out of bounds when it gets to the end two elements
  # if t is [1, 2, 3], then zip(t, t[1:]) will give pairs = [(1, 2), (2, 3)]
  # t is assumed to be an iterable, like a list or a tuple
  # t[1:] creates a new iterable that includes all elements of t starting from the second element (index 1) to the end

tuple1 = (1, 5, 7, 8, 10)
output = multiplyAdjacent(tuple1)
print(output)

"""Question 5.6"""

# Write a function which constructs a dictionary where its keys are the integer
# factors and values are the count of those factors when applied on a list of elements
def factorCount(ls):

  # assigning keys uptil the highest number in list
  factor_dict = {i: 0 for i in range(1, max(ls) + 1)}

  for num in ls:
      for factor in range(1, num + 1):
          if num % factor == 0:
              factor_dict[factor] += 1

  return factor_dict

#main
ls = [2, 4, 6, 8]
d = factorCount(ls)
print(d)

"""Question 5.7"""

# Develop a function to represent the given information in table in the form of tuple.
# Develop a function that examines each block, multiplies shares by purchase price and shares by
# current price to determine the total amount gained or lost.

def computeAmount(stocks):
  i = 0
  for x in stocks:
    amount = x[2]*x[4]-x[2]*x[1]
    print(stocks[i][len(stocks)-1]+"\t$"+str(amount))
    i = i + 1

#main
stocks = (
    ("25 Jan 2001", 43.50, 25, "CAT", 92.45),
    ("25 Jan 2001", 42.80, 50, "DD", 51.19),
    ("25 Jan 2001", 42.10, 75, "EK", 34.87),
    ("25 Jan 2001", 37.58, 100, "GM", 37.58))

computeAmount(stocks)
