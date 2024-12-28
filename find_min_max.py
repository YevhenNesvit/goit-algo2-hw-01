def find_min_max(arr: list[int]) -> tuple[int, int]:
    """
    Функція знаходить мінімальний і максимальний елементи масиву за допомогою методу "розділяй і володарюй".

    :param arr: Список чисел
    :return: Кортеж (мінімум, максимум)
    """
    if len(arr) == 1:
        # Якщо в масиві один елемент, то він є і мінімумом, і максимумом
        return arr[0], arr[0]

    elif len(arr) == 2:
        # Якщо в масиві два елементи, порівнюємо їх
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    else:
        # Ділимо масив на дві частини
        mid = len(arr) // 2
        left_min, left_max = find_min_max(arr[:mid])
        right_min, right_max = find_min_max(arr[mid:])

        # Об'єднуємо результати
        return (min(left_min, right_min), max(left_max, right_max))

# Приклад використання
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_val, max_val = find_min_max(array)
print(f"Мінімум: {min_val}, Максимум: {max_val}")
