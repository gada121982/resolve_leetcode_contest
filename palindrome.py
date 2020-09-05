# problem : https://leetcode.com/problems/palindrome-number/
import numpy as np


class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        so_nguyen = x
        queue = []
        flag_add_queue = True

        while(flag_add_queue):
            so_du = so_nguyen % 10
            so_nguyen = so_nguyen / 10

            queue.append(so_du)
            if so_nguyen is 0:
                flag_add_queue = False

        queue = np.array(queue)

        mid_index = len(queue) / 2
        left = 0
        right = len(queue) - 1
        found_result = False

        while(found_result is False):
            if right - left < 0:
                return True

            if queue[left] != queue[right]:
                return False

            left = left + 1
            right = right - 1


test = Solution()

print test.isPalindrome(11)
