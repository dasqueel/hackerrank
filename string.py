def simplify(s):
    s = list(s)
    if s == []:
        return 'Empty String'
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            del s[i]
            del s[i]
            newStr = ''
            for i in s: newStr = newStr + i
            return simplify(newStr)
        else:
            i += 1

    newStr = ''
    for i in s:
        newStr = newStr + i
    return newStr

print simplify('aa')