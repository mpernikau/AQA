alpha='абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
alphaUP=str.upper(alpha)
number = int(input('Введите ключ, на который нужно сдвинуть текст: '))

summary = ''

def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUP:
        return alphaUP[(alphaUP.index(char) + number) % len(alphaUP)]
    else:
        return char

    with open('filename.txt', encoding='utf8') as myFile:
        for line in myFile:
            for char in line:
                summary += changeChar(char)

with open('output.txt', 'w', encoding='utf8') as myFile:
    myFile.write(summary)