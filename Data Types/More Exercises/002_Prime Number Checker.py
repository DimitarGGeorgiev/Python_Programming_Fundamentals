number = int(input())
result = 0

for i in range(1, number + 1):

    if number % i == 0:
       result += 1

if i == number and result == 2:
    print("True")
else:
    print("False")

