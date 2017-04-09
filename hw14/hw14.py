# Нужно взять какой-нибудь файл с достаточно большим текстом, прочитать его,
# поделить на предложения (просто по знакам конца предложения), удалить знаки препинания.
# Затем в зависимости от варианта сделать следующее (обязательно использовать
# list comprehensions и formatting):
# Создать словарь, в котором ключами являются предложения,
# а в качестве значения выступает словарь с ключами-словами и
# значениями-длинами слов (например, {"Мама вымыла раму": {"Мама": 4, "вымыла": 6, "раму": 4}, ...})






def fileopen():
    sentences = []
    sent2 =[]
    with open('text.txt', "r", encoding="utf-8") as f:
        for line in f.readlines():
            sentences.extend(line.split('.'))
        for s in sentences:
            words = []
            for w in s.split(' '):
                    words.append(w.strip('.,!?:;—«»\n'))
            sent2.append(' '.join(words))

    return sent2

def main():
    dic = {}
    sentences = fileopen()
    for i in sentences:
        len_dic = {}
        for word in i.split(' '):
            len_dic[word] = len(word)
        dic[i] = len_dic


if __name__ == '__main__':
    main()