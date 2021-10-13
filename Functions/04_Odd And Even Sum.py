input_number = input()


def find_even_sum():
    sum_even = int
    for i in input_number:
        num = int(i)
        if num % 2 == 0:
            sum_even = sum_even + num
    return sum_even


def find_odd_sum():
    sum_odd = int
    for i in input_number:
        num = int(i)
        if num % 2 > 0:
            sum_odd = sum_odd + num
    return sum_odd


end_odd = find_odd_sum()
end_even = find_even_sum()

print(f"Odd sum = {end_odd}, Even sum = {end_even}")