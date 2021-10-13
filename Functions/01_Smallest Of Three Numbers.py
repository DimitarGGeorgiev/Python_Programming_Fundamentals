number_one = int(input())
number_two = int(input())
number_three = int(input())


def smallest_number():
    if number_one < number_two and number_one < number_three:
        return number_one
    elif number_two < number_one and number_one < number_three:
        return  number_two
    else:
        return number_three

print(smallest_number())