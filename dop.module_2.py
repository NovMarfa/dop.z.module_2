
n = int (input ('Введите число от 3 до 20: '))
# проверка вводимых чисел
if n >= 3 and n <= 20:
    password = ''

    for i in range (1, n):
        # print(i)
        for j in range (i + 1, n):
            # print (f' {i}, {j}')
            if n % (i + j) == 0:
                # print (f'{i}{j}')
                password = password + str (i) + str (j)
    print (password)

