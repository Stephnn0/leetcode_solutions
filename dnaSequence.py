


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

length = 10

subs = []

seen = set()
repe = set()
for i in range(len(s) - length + 1):

    subs.append(s[i:i+length])

print(subs)

for element in subs:
    if element in seen:
        repe.add(element)
    else:
        seen.add(element)

print(list(repe))
