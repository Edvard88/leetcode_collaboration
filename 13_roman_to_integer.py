# class Solution:
#     def romanToInt(self, s: str) -> int:
#         number_dict = {'I': 1,
#                        'V': 5,
#                        'X': 10,
#                        'L': 50,
#                        'C': 100,
#                        'D': 500,
#                        'M': 1000,
#                        'IV': 4,
#                        'IX': 9,
#                        'XL': 50,
#                        'XC': 90,
#                        'CD': 400,
#                        'CM': 900
#                        }
#
#         test_arr = []
#         list_s = []
#         i = 0
#
#         print("v")
#         while i != len(s):
#             print("d")
#             if i + 1 != len(s):
#                 # print(i)
#                 if (s[i] == 'I' and s[i + 1] == 'V'):
#                     test_arr.append('IV')
#                     list_s.append(number_dict['IV'])
#                     i = i + 2
#                     continue
#
#                 if (s[i] == 'I' and s[i + 1] == 'X'):
#                     test_arr.append('IX')
#                     list_s.append(number_dict['IX'])
#                     i = i + 2
#                     continue
#
#                 if (s[i] == 'X' and s[i + 1] == 'L'):
#                     test_arr.append('XL')
#                     list_s.append('XL')
#                     i = i + 2
#                     continue
#
#                 if (s[i] == 'X' and s[i + 1] == 'C'):
#                     test_arr.append('XC')
#                     list_s.append(number_dict['XC'])
#                     i = i + 2
#                     continue
#
#                 if (s[i] == 'C' and s[i + 1] == 'D'):
#                     test_arr.append('CD')
#                     list_s.append(number_dict['CD'])
#                     i = i + 2
#                     continue
#
#                 if (s[i] == 'C' and s[i + 1] == 'M'):
#                     test_arr.append('CM')
#                     list_s.append(number_dict['CM'])
#                     i = i + 2
#                     continue
#
#                 test_arr.append(s[i])
#                 list_s.append(number_dict[s[i]])
#                 i = i + 1
#             test_arr.append(s[i])
#             list_s.append(number_dict[s[i]])
#
#         # print(test_arr)
#         # print(list_s)
#         # print(sum(list_s))
#         return sum(list_s)
#
#
# cl1 = Solution()
#
#
# cl1.romanToInt("III")
#


# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#         ans=0
#         for i in range(len(s)):
#             if i<len(s)-1 and a[s[i]]<a[s[i+1]]:
#                 ans-=a[s[i]]
#             else:
#                 ans+=a[s[i]]
#         return ans


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


sl = Solution()
print(sl.romanToInt("IV"))
print(sl.romanToInt("III"))
print(sl.romanToInt("IX"))
print(sl.romanToInt("LVIII"))
print(sl.romanToInt("MCMXCIV"))



