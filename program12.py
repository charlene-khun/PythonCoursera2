fname = input("Enter file name: ")
count = 0
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
for line in fh:
    if line.startswith('From:'):
        stuff = line.split()
        print(stuff[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
