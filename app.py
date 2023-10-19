import re
import psycopg2
import random

# Sample dress colors from the web page (replace with actual data)
dress_colors = [
    "red", "green", "pink", "brown", "blue", "yellow", "green", "orange", "cream", "white", "arsh"
]

# Calculate the mean color
mean_color = sum(dress_colors, 0) / len(dress_colors)

# Calculate the most worn color
most_worn_color = max(set(dress_colors), key=dress_colors.count)

# Calculate the median color
sorted_colors = sorted(dress_colors)
median_color = sorted_colors[len(sorted_colors) // 2]

# Calculate the variance
variance = sum((color - mean_color) ** 2 for color in dress_colors) / len(dress_colors)

# Calculate the probability of the color "red"
probability_red = dress_colors.count("red") / len(dress_colors)

# Save colors and their frequencies in PostgreSQL database
def save_to_postgresql(colors):
    conn = psycopg2.connect(database="your_database_name", user="your_username", password="your_password", host="your_host")
    cursor = conn.cursor()
    for color in set(colors):
        frequency = colors.count(color)
        cursor.execute("INSERT INTO dress_colors (color, frequency) VALUES (%s, %s)", (color, frequency))
    conn.commit()
    conn.close()

# Recursive searching algorithm
def recursive_search(arr, target, index=0):
    if index == len(arr):
        return -1  # Target not found
    if arr[index] == target:
        return index
    return recursive_search(arr, target, index + 1)

# Generate a random 4-digit binary number and convert to base 10
random_binary = ''.join(random.choice('01') for _ in range(4))
random_base_10 = int(random_binary, 2)

# Generate the first 50 Fibonacci numbers and calculate their sum
fibonacci_sequence = [0, 1]
for i in range(2, 51):
    next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fib)
fibonacci_sum = sum(fibonacci_sequence)

# Print results
print("Mean color:", mean_color)
print("Most worn color:", most_worn_color)
print("Median color:", median_color)
print("Variance of colors:", variance)
print("Probability of the color 'red':", probability_red)
print("Random 4-digit binary number:", random_binary)
print("Random number in base 10:", random_base_10)
print("Sum of the first 50 Fibonacci numbers:", fibonacci_sum)