immutable_var = [1,2], (1,2,3), bool(2*2 > 3+5), 'Urban' # Задание 2
print(immutable_var)
immutable_var[0][1] = 5 # Задание 3 (Изменять кортеж нельзя т.к. он не поддерживает обращение по элементам, а так же нужен для хранения данных которые не должны изменяться.
print(immutable_var)
mutable_list = [1,2,3,4, 'Sergey'] # Задание 4
print(mutable_list)
mutable_list[0] = 3
mutable_list[4] = 'Anna'
print(mutable_list)