def filter_numbers(numbers: list, threshold: int) -> list:
    return [number for number in numbers if number >= threshold]

print(filter_numbers([1, 5, 10, 3],5))