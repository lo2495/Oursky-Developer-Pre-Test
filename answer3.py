def calculate_series(n):
    if n < 2:
        raise ValueError('Invalid input')
    
    cur = 0
    for i in range(2, n+1):
        cur += 1 / (i * (i - 1))
    
    return cur

# Example:
n = 5
result = calculate_series(n)
print(result)