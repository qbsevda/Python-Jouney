# Define a function named my_min to find the min of the inputted numbers.
# For example:

# Test	Result
# print(my_min(5,6,7))
# 5
# print(my_min(3,8,-9,0,12,1.2))
# -9
# print(my_min(-100))
# -100

def my_min(*ls):
  a = []
  for i in ls:
    a = a + [i]
  a = sorted(a)
  return a[0]

print(my_min(3,8,-9,0,12,1.2))