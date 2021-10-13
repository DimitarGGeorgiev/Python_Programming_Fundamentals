character_one = input()
character_two = input()
chr_list = list()
chr_string = " "

def characters_in_range():
    start_character = ord(character_one)
    end_character = ord(character_two)

    for i in range (start_character + 1, end_character):
        chr_character = chr(i)
        chr_list.append(chr_character)

    return " ".join(chr_list)


print(characters_in_range())