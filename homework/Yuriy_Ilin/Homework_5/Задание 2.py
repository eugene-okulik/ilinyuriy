result = 'результат операции: 42'  # result хранит результат выполнения программы

ind = result.index(':')
print(int(result[ind + 2:]) + 10)

#  Данная программа универсальна для любой текста, где в конце будет число
