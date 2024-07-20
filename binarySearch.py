# 二分搜尋的陣列得是排序過的~~
arr = [165, 167, 169, 170, 176, 179]

# 可以用老師需要找出特定身高的小朋友想像~~
def binarySearch(arr, target):
  left_index = 0
  right_index = len(arr) - 1  # 5
  while left_index <= right_index:
    mid_index = (left_index + right_index) // 2 # 2
    if arr[mid_index] == target:
      return mid_index
    elif target > arr[mid_index]:
      left_index = mid_index 
    elif target < arr[mid_index]:
      right_index = mid_index


def dd(any):
  print(any)
  exit()

dd('指定身高小朋友的索引號是: ' + str(binarySearch(arr, 170)))