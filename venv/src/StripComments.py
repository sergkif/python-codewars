def solution(string,markers):
    list = []
    for s in string.split('\n'):
        for marker in markers:
            if s.find(marker) != -1:
                s = s[:s.find(marker)]
        list.append(s.strip())
    return "\n".join(list)

# def solution(string,markers):
#     parts = string.split('\n')
#     for s in markers:
#         parts = [v.split(s)[0].rstrip() for v in parts]
#     return '\n'.join(parts)

# from re import split, escape
#
# 
# def solution(string, markers):
#     if markers:
#         pattern = "[" + escape("".join(markers)) + "]"
#     else:
#         pattern = ''
#     return '\n'.join(split(pattern, line)[0].rstrip() for line in string.splitlines())

# Strip Comments
#
# 4 kyu
#
# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
#
# apples, pears
# grapes
# bananas
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"