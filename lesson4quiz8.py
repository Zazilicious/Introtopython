start_num = 1
end_num = 6
count_by = 1
break_num = start_num

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while break_num < end_num:
    break_num = break_num + count_by

print(break_num)

start_num = 6
end_num = 1
count_by = 1
break_num = start_num

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

if end_num < start_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while break_num < end_num:
    break_num = break_num + count_by
if end_num > start_num:
    result = break_num
print(result)

limit = 40
count_by = 1 
nearest_square = 0
# write your while loop here
while nearest_square <= 40:
    nearest_square = count_by * count_by
    count_by = count_by + 1
nearest_square = (count_by - 2) * (count_by - 2)

print(nearest_square)
