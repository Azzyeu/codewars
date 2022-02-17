def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        sum = 0
        for i in range(len(str(n))):
            sum += int(str(n)[i])
        return digital_root(sum)