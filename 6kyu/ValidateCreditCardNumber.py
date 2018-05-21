def validate(n):
    
    conv = map(int,str(n))

    if (len(conv) % 2 != 0):
        return (doubdigits(conv[1:])+conv[0]) % 10 == 0;
    else:
        return doubdigits(conv)% 10 == 0


def doubdigits(n):
    return sum((x * 2 if (x * 2 < 9) else (x*2 % 10 + 1)) if i % 2 == 0 else x for (i, x) in enumerate(n,0))
            