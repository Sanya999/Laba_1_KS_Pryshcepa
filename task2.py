import task1
import bz2
def decimalToBinary(decimal_value):
    return bin(decimal_value).replace("0b", "")

def base64Custom(string_text):
    bitsList = ""
    for symbol in string_text:
        decimalValue = ord(symbol)
        binaryValue = decimalToBinary(decimalValue)
        lenToAdd = 16 - len(binaryValue)
        binaryValue = lenToAdd*'0' + binaryValue
        bitsList += binaryValue
    remainder = len(bitsList) % 24
    quarteds = len(bitsList) // 24
    needToAdd = 0
    if (remainder != 0):
        needToAdd = 24 - remainder


    base64ABC = []
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    for i in range(0, 64):
        base64ABC.append({symbols[i]: (6 - len("{0:b}".format(int(i)))) * '0' + "{0:b}".format(int(i))})
    base64String = ""
    for quart in range(quarteds):
        for i in range(4):
            bits = bitsList[:6]
            for base64Symbol in base64ABC:
                if (list(base64Symbol.values())[0] == bits):
                    base64String += list(base64Symbol.keys())[0]
            bitsList = bitsList[6:]
    if (needToAdd == 16): # 8 бітів лишилось
        bitsList += '0000'
        for i in range(2):
            bits = bitsList[:6]
            for base64Symbol in base64ABC:
                if (list(base64Symbol.values())[0] == bits):
                    base64String += list(base64Symbol.keys())[0]
            bitsList = bitsList[6:]
        base64String += "=="
    if (needToAdd == 8): # 16 бітів лишилось
        bitsList += '00'
        for i in range(3):
            bits = bitsList[:6]
            for base64Symbol in base64ABC:
                if (list(base64Symbol.values())[0] == bits):
                    base64String += list(base64Symbol.keys())[0]
            bitsList = bitsList[6:]
        base64String += "="
    return base64String
def decodeInputOriginalText(textName):
    text = task1.read_text(textName + ".txt")
    base64text = base64Custom(text)
    freq = task1.frequency_symbols(base64text)
    # task1.printXlxs(freq, textName + '.xlsx')
    entrop = task1.entropiya(freq)
    task1.information(entrop, len(base64text))
    with open(textName+"Base64.txt", "w") as f:
        f.write(base64text)
def decodeInputArchivedText(textName):
    with bz2.open(textName + ".txt.bz2", "rt") as f:
        text = f.read()
    base64text = base64Custom(text)
    freq = task1.frequency_symbols(base64text)
    # task1.printXlxs(freq, textName + '.xlsx')
    entrop = task1.entropiya(freq)
    task1.information(entrop, len(base64text))
    with open(textName+"ArcBase64.txt", "w") as f:
        f.write(base64text)