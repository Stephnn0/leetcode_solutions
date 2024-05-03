#Given a string s, return the longest palindromic substring in s.
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.#


s = "babad"

print(s[0:1])
print(s[1:2])
print(s[2:3])
print(s[3:4])
print(s[4:5])
print("----------------------------------")
print(s[0:2])
print(s[1:3])
print(s[2:4])
print(s[3:5])
print(s[4:6])
print("----------------------------------")

print(s[0:3])
print(s[1:4])
print(s[2:5])
print(s[3:6])
print(s[4:7])
print("----------------------------------")
ans = []
def isPalindrom(s):
    return s[::-1]==s

for i in range(1, len(s)+1):
    start = 0
    end = i
    print(i)
    while end<len(s)+1:
        if isPalindrom(s[start:end]):
              print(s[start:end])
              a = s[start:end]
              ans.append(a)
        start+=1
        end+=1
print(ans)
print(max(ans, key=len))


