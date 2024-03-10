def ciag(ile_liczb):
    if ile_liczb == 0:
        return 0
    elif ile_liczb == 1:
        return 1
    else:
        a,b = 0,1
        for _ in range (2, ile_liczb +1):
            a,b = b, a + b
        return b


print(ciag(5))