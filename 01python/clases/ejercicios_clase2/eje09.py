'''
9.	Escriba un programa en Python que realice las siguientes 9 multiplicaciones 
y muestre el resultado de cada producto
1 * 1 = 1
11 * 11 = 121
111 * 111 = ?
'''

str_num = '1'

for fila in range(1, 10):

    num = int(str_num * fila)
    prod = num * num

    print(f'{num:>10d} * {num:<10d} = {prod:<20d}')
