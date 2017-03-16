def  prison(n, m, h, v):
    if len(h) == 0 and len(v) == 0:
        return 1
    elif len(h) == n and len(v) == m:
        return (n+1)*(m+1)
    else:
        #find the longest executive chain in h,v
        longestH = 1
        longestV = 1
        consec = 0
        i = 0
        while i < len(h)-1:
            if h[i+1] == h[i]+1:
                consec = consec + 1
                if consec > longestH:
                    longestH = consec
            else:
                consec = 0
            i += 1

        while i < len(v)-1:
            if v[i+1] == v[i]+1:
                consec = consec + 1
                if consec > longestV:
                    longestV = consec
            else:
                consec = 0
            i += 1
        return (longestH+1)*(longestV+1)

print prison(3,3,[1,2],[1,2])