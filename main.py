import heapq
from collections import deque
# # Python DSA Cheat Sheet
# 用Python練習演算法題目的代價是
# 雖然簡短，但要去了解不熟悉的API
# 這個地方提供整理常用的演算法解題內建工具：
# （先跳過清單推導式，面試官不一定熟悉Python，有時候解釋越多延伸問題越多..）

#TODO 建構子

# ✅檢查element有沒有在資料結構內
list_which_have_element = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(1 in list_which_have_element)

# 創各種資料結構

# ✅ez Hashtable(...)
dict = {'k': 'v', 'k2': 'v2'}
print(dict)
# 所有鍵
key_set = dict.keys()
print(key_set)
# 所有值
print(dict.values())
# 移除鍵值對
dict.pop('k')
print(dict)
# key exist，為了避免keyError在取值前要做這樣的事情
is_key_k2_exist = 'k2' in dict # 可以寫得像下方，但會提示你別這樣
print(is_key_k2_exist)
# value exist
is_key_v2_exist = 'v2' in dict.values()
print(is_key_v2_exist)
# kv foreach
for k, v in dict.items():
    print(k, v)

# ✅隊列又叫佇列 先進先出結構
# queue單向隊列 頭消尾插；deque雙向隊列 頭尾皆可pop push
# 官方文件說你儘管吧list當作多用途! https://docs.python.org/zh-tw/3/tutorial/datastructures.html
# 但list變成隊列要先做轉換
list_as_queue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
queue = deque(list_as_queue)
# pop 消掉最先進來的東西 並返回被消掉的是誰
print(queue.popleft())
# push
# queue.append(11) # 這樣會自己印一次
print(queue.append(11))


# ✅Stack 先進後出結構
# pop 消掉最後進來的東西 並返回被消掉的是誰
list_as_stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_as_stack.pop())
print(list_as_stack)
# push
list_as_stack.append(11)
print(list_as_stack)
# peek
print(list_as_stack[len(list_as_stack)-1])

# ✅heap: https://weikaiwei.com/algorithm/heap/
# Python提供了最小堆積（最小的總是在下方）
list_as_heap = [543, 21, 3, 4, 5, 6, 7, 8, 9, 10]
heapq.heapify(list_as_heap) # list轉最小堆積
print(list_as_heap)
heapq.heappop(list_as_heap) # 頂端消失一個元素；得留意只能傳入list型態
print(list_as_heap)
heapq.heappush(list_as_heap, 100) # 上面blog內文程式範例寫反了
print(list_as_heap) # 推入一個元素

# ✅set 不重複的資料結構
set = {1, 1, 2} # 長得好像字典
print(set) # 1, 2

# ✅substring的方法
str = 'meow'
new_str = str[0:3]
print(new_str)  # meo

# ✅String to List
s = "你好 喔"
x = list(s)
print(x)
y = s.split(" ")
print(y)

# ✅Python三元運算
boolean =  1 > 0 if True else False
print(boolean)

# ✅python逆迴圈寫法1 太不直覺了...
# for i in range(len(list)-1, -1, -1):
# python逆迴圈寫法2，這個好一點 另外range(0, 4)是0 1 2 3，就是其他語言的i < 4
# for i in reversed(range(0, len(list))): 

# `pass書目會教` 做顆樹（應用：建立實體並傳入TreeNode）: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

# 其他參考資料
# https://www.stationx.net/python-data-structures-cheat-sheet/
# https://github.com/cy69855522/Shortest-LeetCode-Python-Solutions
