inp_range = []
t_sum = 0

def valid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    
    h = len(s) // 2
    f_half = s[:h]
    s_half = s[h:]
    
    return f_half == s_half and f_half[0] != '0'

with open("2_input.txt", "r") as fp:
    data = fp.read().strip() 
    
r = data.split(",")

for val in r:
    start, end = val.split("-")
    inp_range.append((int(start), int(end)))

print("input_ranges =", inp_range)

for start, end in inp_range:
    for i in range(start, end + 1):
        if valid(i):
            t_sum += i


print("final =", t_sum)