from collections import deque

# 驗證迴文字串考你列隊跟堆疊
str = 'ppapp'
def validPalindrome(str):
  str_stack = list(str) # 先進後出
  str_queue = deque(list(str)) # 先進先出
  n = len(str_stack)
  while n > 0:
    n-=1
    if str_stack.pop() != str_queue.popleft():
      return False
  return True

print(validPalindrome(str))