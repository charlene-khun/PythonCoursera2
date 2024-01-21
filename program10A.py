# Use the file name mbox-short.txt as the file name
count = 0
line1 = 0.0
line4 = 0.0
total = 0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    line3 = line.find(' ')
    line2 = line[line3:]
    line4 = float(line2)
    total = total  + line4
    
print('Average spam confidence:', total/count)