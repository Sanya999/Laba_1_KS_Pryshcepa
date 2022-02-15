import xlsxwriter
import math

def read_text(text):
    with open(text, encoding="utf-16") as myfile:
        data = myfile.read()

    print("Назва: " + text)
    return data
def frequency_symbols(string_text):
    symbolsCount = len(string_text)
    uniqueSymbolsList = []
    for i in string_text:
        alreadyExist = False
        for j in uniqueSymbolsList:
            if len(uniqueSymbolsList) == 0:
                break
            if (i == list(j.keys())[0]):
                alreadyExist = True
                break

        if False == alreadyExist:
            uniqueSymbolsList.append({i: 1})
        else:
            for j in uniqueSymbolsList:
                if (list(j.keys())[0] == i):
                    j[list(j.keys())[0]] += 1


    for uniqueSymbol in uniqueSymbolsList:
        uniqueSymbol[list(uniqueSymbol.keys())[0]] /= symbolsCount

    counter = 0
    for uniqueSymbol in uniqueSymbolsList:
        key = list(uniqueSymbol.keys())[0]
        if key == ' ':
            key = 'space'
        if key == '\n':
            key = 'enter'
        value = uniqueSymbol[list(uniqueSymbol.keys())[0]]
        if (counter % 5 == 0 and counter != 0):
            print("{}: {};".format(key, round(value, 3)))
        else:
            print("{}: {}; \t".format(key, round(value, 3)), end="")
        counter += 1
    print('\n')
    return uniqueSymbolsList

def printXlxs (frequency_symbols, fileName):
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet("Frequency")
    worksheet.write(0, 0, "S") # row,col,value
    worksheet.write(0, 1, "Freq")

    j = 1
    for n in frequency_symbols:

        worksheet.write(j, 0, list(n.keys())[0])
        worksheet.write(j, 1, n[list(n.keys())[0]])
        j+=1

    workbook.close()


def entropiya (uniqueSymbolsList ):
    entropiya_value = 0
    for dictionary in uniqueSymbolsList:
        entropiya_value+=(dictionary[list(dictionary.keys())[0]]) * math.log(1/(dictionary[list(dictionary.keys())[0]]), 2)
    print("Ентропія: " + str(round(entropiya_value, 5)))
    return entropiya_value

def information(entropiya, text_len):
    info = entropiya*text_len/8 #в байтах
    print("Кількість інформації: " +  str(round(info)) + " б.")
    print("##############################\n\n")

def total(textName):
    text = read_text(textName+".txt")
    freq = frequency_symbols(text)
    printXlxs(freq, textName+'.xlsx')
    entrop = entropiya(freq)
    information(entrop, len(text))