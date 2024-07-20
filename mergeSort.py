arr = [12, 8, 9, 3, 11, 5, 4]

def split(arr, le):
  new_arr = []
  if len(arr) == le:
    return arr
  for i in arr:
    if isinstance(i, int):
      print(13)
      new_arr.append([i])
      continue
    middle = len(arr) // 2
    l_arr = i[:middle]
    r_arr = i[middle:]
    new_arr.append(l_arr)
    new_arr.append(r_arr)
    
  split(new_arr, le)
  


def main(arr):
  new_arr = []
  middle = len(arr) // 2
  l_arr = arr[:middle]
  r_arr = arr[middle:]
  new_arr.append(l_arr)
  new_arr.append(r_arr)
  split(new_arr, len(arr))
  return 

main(arr)
