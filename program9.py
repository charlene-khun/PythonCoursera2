text = "X-DSPAM-Confidence:    0.8475"
find1 = text.find(' ')
pos = text[find1+4:]
print(pos)
print(float(pos))