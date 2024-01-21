name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
dic1 = dict()
handle = open(name)
for line in handle:
    if line.startswith('From '):
        words = line.split()
        word1 = words[5][0:2]
        dic1[word1] = dic1.get(word1,0) + 1

lst = list()
for key, val in dic1.items():
    lst.append((key,val))

lst = sorted(lst)

for k, v in lst:
    print(k, v)
    