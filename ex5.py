import timeit
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_performance(search_func, arr, target):
    return timeit.timeit(lambda: search_func(arr, target), number=100)

def linear_func(x, a, b):
    return a * x + b

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# Generate sorted vectors of different sizes
sizes = [1000, 2000, 4000, 8000, 16000, 32000]

for size in sizes:
    arr = sorted([random.randint(0, size*10) for _ in range(size)])
    target = random.randint(0, size*10)

    print(f"Size: {size}")

    # Measure linear search performance
    linear_times = [measure_performance(linear_search, arr, target) for _ in sizes]
    linear_avg_time = sum(linear_times) / len(linear_times)
    print(f"Linear Search: {linear_avg_time:.8f} seconds")

    # Measure binary search performance
    binary_times = [measure_performance(binary_search, arr, target) for _ in sizes]
    binary_avg_time = sum(binary_times) / len(binary_times)
    print(f"Binary Search: {binary_avg_time:.8f} seconds")

    # Plotting
    x = sizes

    plt.scatter(x, linear_times, label='Linear Search', color='blue')
    plt.scatter(x, binary_times, label='Binary Search', color='red')

    # Fit curves
    popt_linear, _ = curve_fit(linear_func, x, linear_times)
    popt_quadratic, _ = curve_fit(quadratic_func, x, binary_times)

    x_fit = range(min(x), max(x) + 1)
    plt.plot(x_fit, [linear_func(i, *popt_linear) for i in x_fit], '--', color='blue', label='Linear Fit')
    plt.plot(x_fit, [quadratic_func(i, *popt_quadratic) for i in x_fit], '--', color='red', label='Quadratic Fit')

    plt.xlabel('Vector Size')
    plt.ylabel('Time (seconds)')
    plt.title(f'Search Performance (Target: {target})')
    plt.legend()
    plt.show()

    print("=" * 40)
