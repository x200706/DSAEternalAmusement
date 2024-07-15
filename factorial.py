def factorial(n):
  if n == 1:
    return 1
  else:
    print(n)
    return n * factorial(n-1)
    
print(factorial(6))
# 6 * f(5)
# 6 * 5 * f(4)
# 6 * 5 * 4 * f(3)
# 6 * 5 * 4 * 3 * f(2)
# 6 * 5 * 4 * 3 * 2 * f(1)
# 6 * 5 * 4 * 3 * 2 * 1 = 720