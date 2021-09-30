key = int(input())
symbols = int(input())

for i in range(0, symbols + 1):
    letter = str(input())
    letter_ascii = ord(letter) + key
    print(chr(letter_ascii), end="")
