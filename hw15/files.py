import os

def main():
    count = 0
    all_f = os.listdir()
    for item in all_f:
        test = item.split('.')
        if len(test) > 1 and latin(test[0]):
            count += 1

    print(count)

def latin(word):
    alph = 'qwertyuiopasdfghjklzxcvbnnmQWERTYUIOPASDFGHJKLZXCVBNM '
    for letter in word:
        if letter not in alph:
            return False
    return True

if __name__ == '__main__':
    main()
