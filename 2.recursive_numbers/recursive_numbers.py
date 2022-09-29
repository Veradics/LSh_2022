# рекурсивная функция: возвращает значения от 1 до N
# число рекурсивных вызовов <= 995 (ограничение системы)

# Принято, что N должно быть целым (в задании это не указано, 
# но если оно будет дробным, непонятно, что следует вывести)

def recursive_number(N):
    if type(N) == int and N in range(-993, 996):  # проверка N
        if N > 1:
            recursive_number(N-1)
        elif N < 1:
            recursive_number(N+1)
        print(N)
    else:   # вывод сообщения об ошибке
        print('Ошибка. Введенное число не является целым или максимальная глубина рекурсии превышена.')

# N = int(input())
# recursive_number(N)