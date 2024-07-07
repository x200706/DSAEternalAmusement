str = input('輸入點東西吧\n')
str_stack = list(str)

command = input('\n接下來的操作（記得按enter送出）：輸入vi查看當前文字，輸入dd刪除整段，輸入b刪去一個字，輸入i繼續輸入，輸入q離開\n')
while command != 'q':
  if command == 'vi':
    print(''.join(str_stack))
  elif command == 'dd':
    str_stack.clear()
    new_str = ''.join(str_stack)
    print(new_str)
  elif command == 'b':
    if len(str_stack) != 0:
      str_stack.pop()
      new_str = ''.join(str_stack)
      print(new_str)
  elif command == 'i':
    add_str = input('請輸入：')
    for char in list(add_str): 
      str_stack.append(char)
    new_str = ''.join(str_stack)
    print(new_str)
  elif command != 'q':
    print('沒有這個命令')
  command = input('\n接下來的操作（記得按enter送出）：輸入vi查看當前文字，輸入dd刪除整段，輸入b刪去一個字，輸入i繼續輸入，輸入q離開\n')
    

print('程式結束')