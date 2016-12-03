with open("sygma.txt", "r", encoding = "utf-8") as f:
    list = []
    alltext = 0
    withmarks = 0
    for line in f.readlines():
        a = line.split( )
        alltext += len(a)
        for item in a:
            n = item[len(item) - 1]
            if n in ",.":
                withmarks += 1
    percentage = withmarks * alltext / 100
    print (percentage, "% слов в тексте заканчиваются точкой или запятой")

