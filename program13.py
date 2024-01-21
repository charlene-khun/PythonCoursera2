name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic1 = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        word1 = words[1]
        dic1[word1] = dic1.get(word1,0) + 1
 
max1 = None
bigword = None
for word,count in dic1.items():
    if max1 is None or count > max1:
        bigword = word
        max1 = count
        
print(bigword,max1)