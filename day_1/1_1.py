curr = 50
zc = 0
with open("1_input.txt", "r") as fp:
	all_lines = fp.readlines()

for line in all_lines:
	s = line.strip()
	if not s:
		continue
	if s.startswith("R"):
		val = int(s[1:])
		curr = (curr + val) % 100
	elif s.startswith("L"):
		val = int(s[1:])
		curr = (curr - val) % 100

	if curr == 0:
		zc += 1

print("final =", zc) 

# answer = 1129