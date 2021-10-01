input_numbers = input()
output_list = list()
list_of_numbers = input_numbers.split(" ")
number = 0

for i in range (0, len(list_of_numbers)):
    number = int(list_of_numbers[i])
    if number == 0:
        number = 0
    else:
        number *= -1
    output_list.append(number)

print(output_list)