list = [1, 5, 3, 2, 4, 10, 9, 8, 7, 6]
# 一般版
def bubbleSort(list):
  n = len(list) # 10
  while n > 0:
    n-=1
    for i in range(0, len(list)-1):
      if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
    # n-=1 因為while放這邊也行
  return list

# 遞迴版
def bubbleSortRecursion(list, n):
  if n == 0:
    return list
  for i in range(0, len(list)-1):
    if list[i] > list[i+1]:
      list[i], list[i+1] = list[i+1], list[i]
  return bubbleSortRecursion(list, n-1)
  
  
print(bubbleSortRecursion(list, len(list)))
  