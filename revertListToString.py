# 把輸入的數字變成倒過來的字串 1230 0321
list = [1, 2, 3, 0]
string = ''

# 一般迴圈解
def revertItLoop(string, list):
  for i in reversed(range(0, len(list))): 
    string += str(list[i])
  return string

# 限定遞迴解
# stack版（網友提供的思路）
stack = list
def revertItStack(string, stack): # 如果區域變數叫str會害str()方法壞掉
  if len(stack) == 0:
    return string
  else:
    string += str(stack.pop())
    return revertItStack(string, stack) # 遞迴要返回欸...
    # 至於在debug看到string退回原樣，是因為遞迴展開，區域變數銷毀

# 尋常遞迴版
def revertItRecursion(list, list_len):
  if list_len == 0:
    return ''
  elif list_len == 1:
    return list[0]
  else:
    return str(list[list_len - 1]) + str(revertItRecursion(list, list_len - 1))

print(revertItRecursion(list, len(list)))