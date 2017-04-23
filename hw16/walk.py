# 4. на какую букву начинается название большинства папок (если таких много, можно печатать только одну); 

import os

letters = {}

for root, dirs, files in os.walk('.'):
    for name in dirs:
        n = name.split('.')[0]
        if len(n) >=1:
            n = n[0]
            if n not in letters:
                letters[n] = 1
            else:
                letters[n] += 1
maximum = max(letters, key=letters.get)
            
print(letters)
