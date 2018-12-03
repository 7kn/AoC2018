#f!/usr/bin/python3

file = "input_day1.txt"
result = 0

with open(file) as f:
    read_data = f.readlines()

for numb in read_data:
    a = numb.strip('\n')
    if a[0] == "+":
        add_numb = a[1:]
        result += int(add_numb)
    else:
        result += int(a)

print(result)