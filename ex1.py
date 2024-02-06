from functools import lru_cache
from matplotlib import pyplot as plt
import timeit

# 1. This code returns the Fibonacci sequence using a recursive approach 
    
# 2. No this is not an example of divide and conquer algorithm as this code does not break the problem into sub parts 
#    rather it solves the probelm by taking the sum of two preceeding Fibonacci numbers. Also this recursive approach 
#    leads to excessive and repeated calculations.

# 3. The time complexity expression for the algorithm is : O(2^n)
    
# 4. 

# 5. The time complexity expression for the optimized algorithm is : O(n)

# origianal code 

def func(n):
    if n==0 or n==1:
        return n
    else:
        return func(n-1) + func(n-2)

# optimized code (4.) 
       
@lru_cache(maxsize=None)  
def func_optimized(n):
    if n==0 or n==1:
        return n
    else:
        return func_optimized(n-1) + func_optimized(n-2)

# 5. The time complexity expression for the optimized algorithm is : O(n)
    
#6. Plotting
    
n_range = range(36)

time_for_original = []

for n in n_range:
    time_original = timeit.timeit(lambda: func(n), number=1)
    time_for_original.append(time_original)

plt.figure(figsize=(10, 6))
plt.plot(n_range, time_for_original, marker='o',color = 'green', label='Original Function')
plt.xlabel('Integers between 0 to 35')
plt.ylabel('Time (seconds)')
plt.title('Performance of Original Function')
plt.grid(True)
plt.savefig('ex1.6.1.jpg')  


time_for_optimized = []

for n in n_range:
    time_optimized = timeit.timeit(lambda: func_optimized(n), number=1)
    time_for_optimized.append(time_optimized)

plt.figure(figsize=(10, 6))
plt.plot(n_range, time_for_optimized, marker='o', color='red', label='Optimized Function')
plt.xlabel('Integers from 0 to 35')
plt.ylabel('Time (seconds)')
plt.title('Performance of Optimized Function')
plt.grid(True)
plt.savefig('ex1.6.2.jpg')  
plt.show()