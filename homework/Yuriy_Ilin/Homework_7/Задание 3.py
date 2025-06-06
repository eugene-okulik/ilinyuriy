def result(s):
    lst = s.split()
    return int(lst[-1]) + 10


s = "результат работы программы: 209"  # Допустим, программа вернула результат в таком виде
print(result(s))
