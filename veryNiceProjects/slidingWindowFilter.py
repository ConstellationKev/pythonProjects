# creating a list of the raw data
raw_data = []
file = open("data.txt", "r") # data.txt is the raw data
for value in file:
    raw_data.append(float(value))
file.close()
    
# I used a median filter

# I used an odd window size so it would be easier to find the median
window_size = 13
i = 0 # index of the raw data
filtered_data = []

# makes sure that the window size is not larger than the length of the remaining values 
# in the raw data
while i < len(raw_data) - window_size + 1:
    # creates a list of the values of the raw data in the window
    window = raw_data[i : i + window_size] 
    # to find median we need to first sort the numbers in ascending order
    window.sort() 
    # the median is the middle value
    window_med = window[window_size//2] 
    # add this median to the filtered data
    filtered_data.append(window_med) 
    # we move the window one value down
    i += 1

"""
However, the filter above will be missing 12 outputs since when the window gets to the
last few values, there will not be enough values in the raw data to fill the window.
So, I will continuously make the window smaller for the last few values so that they 
will fit into the window as the window moves down.
"""

while window_size > 1:
    # window gets smaller
    window_size -= 1
    # filtering
    window = raw_data[i : i + window_size]
    window.sort()
    window_med = window[window_size//2]
    filtered_data.append(window_med)
    i += 1
    
# writting the filtered data to a separate file so I can copy and paste onto google sheets
file = open("newdata.txt", "w")
for value in filtered_data:
    file.write(str(value) + "\n")
file.close()