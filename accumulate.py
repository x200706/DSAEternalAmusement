count = 0
def accumulate(count):
  if count == 11:
    return count
  print(count)
  count += 1
  return accumulate(count)

print(accumulate(count))