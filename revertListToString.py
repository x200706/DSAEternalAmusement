# (限定遞迴解)把輸入的數字變成倒過來的字串 1230 0321
# stack版
list = [1, 2, 3, 0]
stack = list
string = ''

def revertIt(string, stack): # 如果區域變數叫str會害str()方法壞掉
  if len(stack) == 0:
    return string
  else:
    string += str(stack.pop())
    return revertIt(string, stack) # 遞迴要返回欸...
    # 至於在debug看到string退回原樣，是因為遞迴展開，區域變數銷毀

print(revertIt(string, stack))

# 一般迴圈轉換版