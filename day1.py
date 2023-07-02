f = open("day1_input.txt", "r")
totals = []
curr_cals = 0
for x in f:
    x = x.strip()
    if (x!=""):
        # print(x)
        curr_cals += int(x)
        # print(curr_max_cals)
    elif (x == ""):
        totals.append(curr_cals)
        curr_cals = 0
totals.sort(reverse=True)
print(totals[0]) # total cals of highest elf
print(totals[0] + totals[1] + totals[2]) # sum of the top three elves