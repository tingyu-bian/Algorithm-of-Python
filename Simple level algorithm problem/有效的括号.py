
# 问题：
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
# 输入: "()"
# 输出: true
#
# 示例 2:
# 输入: "()[]{}"
# 输出: true
#
# 示例 3:
# 输入: "(]"
# 输出: false
#
# 示例 4:
# 输入: "([)]"
# 输出: false
#
# 示例 5:
# 输入: "{[]}"
# 输出: true


class ValidBracketsProblem(object):
    @staticmethod
    def valid_brackets(brackets):
        if brackets is None or len(brackets) == 0:
            print(True)
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in brackets:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif len(stack) == 0 or mapping[char] != stack.pop():
                print(False)
        return len(stack) == 0


brackets_str = "{[]}"
ValidBracketsProblem().valid_brackets(brackets_str)


# 思路：
# 特判：s为空时返回True
# 建立栈空间（列表stack）和括号匹配字典mapping
# 判断s中，若为左括号则进栈，若为右括号时栈为空或右括号与栈顶左括号不匹配，则返回False
# 遍历s结束后，若栈为空则返回True，栈不为空返回False
