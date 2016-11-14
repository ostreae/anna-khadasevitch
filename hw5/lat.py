word = 'пупупу'
inf_list = []
N_in_list = 0
while word != '':
    word = input('введите латинское слово:')
    if word[-2:] == 're' or word[-2:] == 'ri' or word [-3:] == 'sse':
        inf_list.append(word)
        N_in_list += 1
for i in range (N_in_list):
    print(inf_list[i])
