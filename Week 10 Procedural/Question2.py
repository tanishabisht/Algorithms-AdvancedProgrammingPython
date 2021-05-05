# Write a Python function that prints out the first n rows of Pascal&#39;s triangle.

from math import factorial
  
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()