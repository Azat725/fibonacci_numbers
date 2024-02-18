def fibanucci_numbers(number: int) -> list:
    # Проверка на то, является ли число положительным
    if number <= 0:
        return []
    # Если число = 1, то возвращаем первое число из последовательности фиббоначи -> 0
    elif number == 1:
        return [0]
    # Если число = 2, то возвращаем список из первых двух чисел фиббоначи -> 0, 1
    elif number == 2:
        return [0, 1]
    
    # Если число больше 2(2 включительно), то выполняется цикл while, пока длина списка fib не будет равна параметру функциии
    else:
        fib = [0, 1]
        
        while len(fib) < number:
            # Добавляем число фиббоначи в список fib
            fib.append(fib[-1] + fib[-2])
            
        return fib
    
user_number_for_fibanucci = int(input("Введите цифру >>>> "))
print(
    f"Последовательность цифр фиббоначи для цифра {user_number_for_fibanucci} = {fibanucci_numbers(user_number_for_fibanucci)}"
    )
