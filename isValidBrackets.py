# 先不用想整理成丟到做題平台會AC的格式
s = "()[{}"
str_list = list(s)
check_stack = []

for e in str_list:
  if e == '(':
    check_stack.append(')')
  elif e == '[':
    check_stack.append(']')
  elif e == '{':
    check_stack.append('}')
  elif e == check_stack[len(check_stack)-1]:
    check_stack.pop()
    
print(check_stack)
is_valid = len(check_stack) == 0 if True else False
print(is_valid)