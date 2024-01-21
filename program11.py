fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    w = line.split()
    for stuff in w:
        if stuff in lst:
            continue
        else:
            lst.append(stuff)    
lst.sort()
print(lst)