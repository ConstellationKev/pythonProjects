#asking for some numbers
nums = input("""Input the numbers
e.g. 1 2 23 54 1 4
Note: Please separate numbers with spaces only

""")

#putting inputted numbers into a list
nums_ls = []
current_num = ""
nums_str_len = len(nums)
itera = 0
for ch in nums:
    itera += 1
    if ch == " ":
        try:
            nums_ls.append(int(current_num))
            current_num = ""
        except:
            pass
    elif ch != " ":
        try:
            int_check = int(ch)
            current_num += ch
            if itera == nums_str_len:
                nums_ls.append(int(current_num))
        except:
            pass

#finding the total
total = 0
for num in nums_ls:
    total += num

#finding the average
average = total/len(nums_ls)

#finding difference of each number to the average and adding it together
t_diff = 0
for num in nums_ls:
    diff = abs(num - average)
    t_diff += diff

#calculating the MAD
mad = t_diff/len(nums_ls)
print(f"""\n
Here is the total, average, and MAD of {nums_ls}
----------------------
The TOTAL is:
{total}

The AVERAGE is:
{average}

The MAD is: 
{mad}
""")