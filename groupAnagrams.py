strs = ["eat","tea","tan","ate","nat","bat"]

ansDic = {}

ans = []

for i in range(len(strs)):
    sortedd = ''.join(sorted(strs[i]))

    if sortedd is not ansDic:
       ansDic[sortedd] = []



for i in range(len(strs)):
     sortedd2 = ''.join(sorted(strs[i]))
     
     if sortedd2 in ansDic:
         print('true')
         ansDic[sortedd2].append(strs[i])
            
answw = ansDic.values()

print(answw)
print(ansDic.values());
