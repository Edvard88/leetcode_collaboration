class Solution:
    def romanToInt(self, s):
        ans = 0

        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lenght = len(s)

        iter = list(range(lenght))
        print(iter)

        for i in range(lenght):
            if i<lenght-1:

                current = a[s[i]]
                next = a[s[i+1]]

                if current < next:
                    ans -= current
                else:
                    ans += current
            else:
                current = a[s[i]]
                ans += current
        return ans


# s1 = Solution()
# print(s1.romanToInt("IV"))
# print(s1.romanToInt("III"))
# print(s1.romanToInt("IX"))
# print(s1.romanToInt("LVIII"))
# print(s1.romanToInt("MCMXCIV"))


class Solution2:
    def romanToInt(self, s):
        ans = 0

        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
             'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        lenght = len(s)
        i=0
        while i<=lenght-1:
            tmp = s[i:i+2]
            if s[i:i+2]  in a:
                ans = ans + a[s[i:i+2]]
                i = i + 2
            else:
                tmp = s[i]
                ans = ans + a[s[i]]
                i+=1

        return ans


s2 = Solution2()
print(s2.romanToInt("IV"))
print(s2.romanToInt("III"))
print(s2.romanToInt("IX"))
print(s2.romanToInt("LVIII"))
print(s2.romanToInt("MCMXCIV"))




