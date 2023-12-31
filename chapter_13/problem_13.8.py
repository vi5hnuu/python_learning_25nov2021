def freq(s):
    freq={}
    for word in s.split():
        freq[word]=freq.get(word,0)+1;
    return freq;

sentence='it is true for all that that that that\
refers refers'
d=freq(sentence)
words=sorted(d)

for w in words:
    print(w,d[w])
