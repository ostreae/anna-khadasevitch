slovo = input("vvedite slovo: ")
for i in range(len(slovo) , 0, -1):
    print(slovo[i:] + slovo[:i])
