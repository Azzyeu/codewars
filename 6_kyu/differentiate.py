def differentiate(poly):

    if "x" not in poly:
        return "0"
    elif "^" not in poly:
        return poly[:-1]
    else:
        x = "x"
        p = "^"
        fx = poly.find("x")
        a = int(poly[:fx]) * int(poly[fx+2:])
        n = int(poly[fx+2:]) - 1
        if n == 1:
            n = ""
            p = ""
        return "{}{}{}{}".format(a,x,p,n)

print(differentiate("x"))