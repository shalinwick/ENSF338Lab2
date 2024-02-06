# Part 1
# A profiler keeps track of how long a program takes to run and how much resources it uses. It figures out which parts of the program are slowing it down by looking at how long each function takes to run and how often they are called. This helps programmers make the code run faster.

# Part 2
# Profiling looks closely at how a program runs to make it faster. Benchmarking, on the other hand, tests how well a program performs compared to others or certain standards. Profiling helps find and fix problems with speed, while benchmarking sees how well the program performs overall.







# Part 3
import timeit
import cProfile

def sub_function(n):
    #sub function that calculates the factorial of n 
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function ():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

test_function()
third_function()

cProfile.run('test_function(); third_function()')

# PART 4 explaing a sample output 

# Sample Output - 

# 71 function calls (26 primitive calls) in 44.757 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    7.228    7.228   44.751   44.751 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 ex3.py:11(test_function)
#         1    0.011    0.011   37.522   37.522 ex3.py:17(third_function)
#         1   37.512   37.512   37.512   37.512 ex3.py:19(<listcomp>)
#     55/10    0.000    0.000    0.000    0.000 ex3.py:4(sub_function)
#         1    0.004    0.004   44.755   44.755 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.002    0.002    0.002    0.002 {method 'disable' of '_lsprof.Profiler' objects}

#Analysis:

# ncalls: The number of calls to the function. The format "x/y" indicates x total calls, but only y of them were primitive (i.e., not recursive).
# tottime: The total time spent in the given function (excluding time made in calls to sub-functions).
# percall: The time per call. This is the quotient of tottime divided by ncalls.
# cumtime: The cumulative time spent in this and all subfunctions (from the perspective of the function). It's the total time spent, including calls to other functions.
# percall: The second percall column relates to the cumulative time per call and is calculated by dividing cumtime by primitive calls.
# filename:lineno(function): This column shows the location (file and line) and name of the function.
# 
# <module> (1 call, 44.751 sec): This entry represents the overall time to run the script passed to cProfile.run, which includes the execution of both test_function and third_function. The total execution time for the module is approximately 44.757 seconds, indicating the bulk of the execution time is within this script's scope.
# test_function (1 call, 0.001 sec): This function has a negligible execution time. It calls sub_function to generate a list of factorials for numbers 0 through 9. Despite calling a recursive function, its execution time is minimal compared to the total execution time.
# third_function (1 call, 37.522 sec): A significant amount of time is spent in third_function, which calculates the squares of numbers from 0 to 99,999,999. Notably, the list comprehension within this function (<listcomp>) is where the vast majority of time (37.512 seconds) is spent, indicating that the operation of squaring each number in a large range is the primary bottleneck in this script.
# sub_function (55/10 calls, negligible time): This function is called 55 times in total, but only 10 of those are primitive calls. The discrepancy in the call count indicates recursion. Despite the recursive calls, the total time spent in this function is negligible.