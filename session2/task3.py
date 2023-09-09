str1 = "milan"
str2 = "nmila"

def Check(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return -1
    else:
        str1_sorted = sorted(str1)
        str2_sorted = sorted(str2)
        if str1_sorted == str2_sorted:
            return 1
        else:
            return 0

Res = Check(str1, str2)
if Res == 1:
    print("strings are Anagrams")
else:
    print("strings are not Anagrams")