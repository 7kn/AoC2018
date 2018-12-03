#f!/usr/bin/python3

file = "input_day1.txt"
curr_freq = 0
freq_list = []
duplicate_freq = False

def run_freq_calc(curr_freq):
    global curr_freq

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
            print(str(curr_freq) + " already exists!!")
            duplicate_freq = True
            exit()

while duplicate_freq == False:
    run_freq_calc(curr_freq)
    