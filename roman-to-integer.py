# problem : https://leetcode.com/problems/roman-to-integer

dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

special_cases = {
    'V': 'I',
    'X': 'I',
    'L': 'X',
    'C': 'X',
    'D': 'C',
    'M': 'C'
}


class Solution(object):

    def isSpecialCase(self, sp1, sp2):
        if sp2 in special_cases and sp1 == special_cases[sp2]:
            return True
        return False

    def sumSpecialValue(self, sp1, sp2):
        return dic[sp2] - dic[sp1]

    def romanToInt(self, s):
        end = len(s) - 1
        result = 0

        while(True):
            if self.isSpecialCase(s[end - 1], s[end]) and (end - 1 >= 0):
                result += self.sumSpecialValue(s[end - 1], s[end])
                end = end - 2

            else:
                result += dic[s[end]]
                end = end - 1

            if end < 0:
                return result


test = Solution()

print test.romanToInt('IV')
