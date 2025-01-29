
# 3184. Count Pairs That Form a Complete Day I

hours = [24,24]

total_count = 0
for i in range(len(hours)-1):
    for j in (hours[i+1:]):
        sum = hours[i] + j
        if sum%24 == 0:
           total_count +=1

print(total_count)


                
