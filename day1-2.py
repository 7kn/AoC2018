#f!/usr/bin/python3

file = "data.txt"
curr_freq = 0
freq_list = []

with open(file) as f:
    read_data = f.readlines()

for line in read_data:
    line = line.strip('\n')
    if line[0] == "+":
        curr_freq += int(line[1:])
    else:
        curr_freq += int(line)

    if curr_freq not in freq_list:
        freq_list.append(curr_freq)
    elif curr_freq in freq_list: 
        print(curr_freq + " already exists!!")