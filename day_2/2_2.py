inp_range = []
t_sum = 0

def valid(n):
    s = str(n)
    L = len(s)
    for k in range(1, L//2 + 1):
        if L % k == 0:
            b = s[:k]
            if b[0] != '0' and b * (L // k) == s:
                return True
    return False


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