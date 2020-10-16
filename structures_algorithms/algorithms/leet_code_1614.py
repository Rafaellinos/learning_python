

def maxDepth(s: str) -> int:
    mc = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] == "(":
            tmp += 1
        if s[i] == ")":
            tmp -= 1
        if tmp > mc:
            mc = tmp

    return mc

"""
"(1+(2*3)+(1+(8)/4))+1
(()(()))
"""



print(maxDepth(s="(1+(2*3)+((8)/4))+1"))