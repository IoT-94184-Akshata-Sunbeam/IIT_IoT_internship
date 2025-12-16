l1=[11,22,33,44,55]
l2=[43,32,87,94,22]

def overlap():
    for x in l1:
        for y in l2:
            if x==y:
                return print("True")
    else:
        return print("false")

overlap()
