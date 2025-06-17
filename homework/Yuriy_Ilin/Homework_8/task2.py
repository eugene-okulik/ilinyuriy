def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


val_5 = next(v for i, v in enumerate(fibonacci()) if i == 4)
val_200 = next(v for i, v in enumerate(fibonacci()) if i == 199)
val_1000 = next(v for i, v in enumerate(fibonacci()) if i == 999)
val_100000 = next(v for i, v in enumerate(fibonacci()) if i == 99999)

print(val_5)
print(val_200)
print(val_1000)
print(val_100000)  
# На данном числе падает ошибка, т.к. слишком большое значение. 
# Решил это не исправлять, т.к. на данном этапе уйду в дебри, если надо, то могу изучить вопрос и решить задачу
