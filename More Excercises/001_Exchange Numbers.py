a = int(input())
b = int(input())
c = 0

a += b



c = a
a = b
b = c

print(f"""
Before:
a = {b}
b = {a}
After:
a = {a}
b = {b}
""")