# s = "Hi my name is aly i am in UMSI and xo"

# def string_manip(s):
#     stringone = s.strip()
#     stringtwo = stringone.upper()
#     stringthree = stringtwo.replace(" ", "#")
#     stringfour = stringthree.replace("UMSI", "")
#     return stringfour[::-1]

# print (s[::-1])

# s = "abcdef"
# print (s.split())

# L1 = ['a', 'b', 'c']
# L2 = [1, 2, 3]
# zipped = zip(L1, L2)
# print (len(zipped), zipped[1], zipped[1][0])

####################

# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))

# t.sort(reverse=True)

# res = list()
# for length, word in t:
#     res.append(word)

# print(res)
###############

lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)