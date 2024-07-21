# list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 幾個特殊情境：
# 1. list[8:8] == []
# 2. list[j:i]，i得>j不然也是得到空陣列
# 基於以上兩點等下巢狀迴圈可設計i > j，可以少跑出幾個空陣列減少運行時間
# （雖然迴圈照跑就是了...）

# 暴力解
# def maxSubArrayViolence(list):
#   temp_list = []
#   temp_sum = ''
#   # create every SubArray
#   for i in reversed(range(0, len(list)+1)):  # j == 8 7 6 5 4 3 2 1 0
#     for j in range(0, len(list)):  # j == 0 1 2 3 4 5 6 7 8
#       if i > j:
#         new_list = list[j:i] # 小心處理左開右閉!!
#         print('when i =' + str(i) + ' j =' + str(j))
#         print(new_list)
#         new_list_sum = sum(new_list)
#         # 首次加總或新總和比就有陣列還大，取代之
#         if temp_sum == '' or new_list_sum > temp_sum: 
#           temp_sum = new_list_sum
#           temp_list = new_list

#   return {temp_sum : temp_list} # 都暴力了順便告訴你是哪一組陣列吧-.-
# print(maxSubArrayViolence(list))

list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 動態規劃解
def maxSubArrayDp(list):
  curr_sum = None
  max_sum = None
  for e in list:
    if curr_sum == None and max_sum == None:
      curr_sum = e
      max_sum = e
    elif e < curr_sum: 
        curr_sum = curr_sum + e 
        max_sum = max(curr_sum, max_sum)
    elif e > curr_sum: 
        curr_sum = e 
        max_sum = max(curr_sum, max_sum)
  return max_sum

print(maxSubArrayDp(list)) # 6