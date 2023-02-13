# Напишите программу, удаляющую из текста все слова, содержащие ""abc""

file_1 = open('text with abc.txt', 'r')
file_result = open("file result.txt", "w")
list_read = []

while True:
    line = file_1.readline()
    print(line)
    list_read = line.split(" ")
    list_write = []

    for word in list_read:

        exist = "abc" in word
        if exist == False:
            list_write.append(str(word))

    if not line:
        break
    string = " ".join(list_write)
    file_result.write(string)

file_result.close()
file_1.close()