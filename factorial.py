def factorial(n):
  if n == 1:
    return 1
  else:
    print(n)
    return n * factorial(n-1)
    
print(factorial(6))