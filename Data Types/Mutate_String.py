first_string = input()
second_string = input()
mutate_string = 0
final_string = first_string


for x in range(0, len(first_string)+1):
    mutate_string = second_string[:x+1]+first_string[x+1:]
    if mutate_string != final_string:
        final_string = mutate_string
        print(final_string)