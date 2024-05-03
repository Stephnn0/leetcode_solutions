



haystack = "sadbutsad"
needle = "sad"


if needle  in haystack:
    print("halaaaa")
else:
    print("noooo")

print(haystack.index("sad"))

    def strStr(self, haystack: str, needle: str) -> int:

        if needle in haystack:
            return haystack.index(needle)

        else:

            return -1
