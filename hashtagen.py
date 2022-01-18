from random import randint
import hashlst
hashes = []
while len(hashes) < 29:
    randhash = hashlst[randint(0, len(hashlst)-1)]
    if randhash in hashes:
        continue
    else:
        hashes.append(randhash)
hashes.append('#htmlisnotaprogramminglanguage')
for i in hashes:
    print(i, end=' ')
print()
