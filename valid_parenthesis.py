'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        closing = ')]}'
        output = ''
        for i in s:
            if i in closing:
                if output == '': return False
                else:
                    if d[output[-1]] == i:
                        output = output[:-1]
                    else: return False
            else: output += i
        if output == '' : return True
        else : return False

            