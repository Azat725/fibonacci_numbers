def fibanucci_numbers(number):
    if number <= 0:
        return []
    elif number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    
    else:
        fib = [0, 1]
        
        while len(fib) < number:
            fib.append(fib[-1] + fib[-2])
            
        return fib
    
user_number_for_fibanucci = int(input("Введите цифру >>>> "))
print(
    f"Последовательность цифр фиббоначи для цифра {user_number_for_fibanucci} = {fibanucci_numbers(user_number_for_fibanucci)}"
    )
