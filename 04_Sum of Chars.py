char_num = int(input())
char = 0
total_sum = 0

for i in range (0,char_num):
    char = input()
    total_sum += ord(char)

print(f"The sum equals: {total_sum}")