immutable_var = 1,2,'a','b'
print(immutable_var)
#immutable_var [0] = [5]
#print(immutable_var) Кортеж не поддерживает изменения по элементам
mutable_list = [1, 2, 'a', 'b', 'Modified']
print(mutable_list)
mutable_list[0]=9
mutable_list[1]='l'
print(mutable_list)