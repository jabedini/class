def gc(Y):
    n = len(Y)
    count = 0
    for item in Y:
        if item == "C" or item == "G":
            count += 1
        elif item == "c" or item == "g":
            count += 1
        else:
            count += 0
    gc_content = count/n*100
    return '%.2f' % gc_content
