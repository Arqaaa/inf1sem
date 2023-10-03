import string
text = open("license", "r")
d = dict()

x = text.read().split()
print(x)
for i in x :
    if not (i in d.keys() ) :
        d[i]=1
    else:
        d[i] += 1
for key, val in sorted(list(d.items()), key = lambda x : x[1], reverse = True)[:10]:
    print(key,val)