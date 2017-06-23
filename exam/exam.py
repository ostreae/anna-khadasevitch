# (5 баллов). Посчитайте, сколько в каждом файле слов, запишите эту информацию в новый текстовый файл
# в формате "название файла<табуляция>количество слов", для каждого файла информация на новой строчке.

import os


def count_words(lines):
    count = 0
    for line in lines:
        if '<w>' in line:
            count +=1
    return count

def write_file(data):
    text = ''
    for file in data:
        text += file['file_name'] + '\t' + str(file['word_count']) + '\n'
    with open('word_count.txt', 'w') as f:
        f.write(text)

def main():
    files = os.listdir('news')
    final = []
    for file in files:
        if file.startswith("_"):
            path = os.path.join('news', file)
            with open(path, 'r') as f:
                temp = {"file_name": file, "word_count": count_words(f.readlines())}
            final.append(temp)
    write_file(final)


if __name__ == '__main__':
    main()
