import jieba

posWord = set()
negWord = set()
'''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''
def senti(doc):
    global posWord
    global negWord

    posSeg = []
    negSeg = []
    '''''''''''''''''''''''''''''''''''''''   
                讀入正負面用詞檔
    '''''''''''''''''''''''''''''''''''''''
    if len(posWord) == 0:
        with open('positives.txt', 'r', encoding='UTF-8') as file:
            for data in file.readlines():
                data = data.strip()
                posWord.add(data)
    if len(negWord) == 0:
        with open('negatives.txt', 'r', encoding='UTF-8') as file:
            for data in file.readlines():
                data = data.strip()
                negWord.add(data)

    '''''''''''''''''''''''''''''''''''''''
                讀入文字檔
    '''''''''''''''''''''''''''''''''''''''

    s = jieba.cut(doc)
    for k in s:
        if k in posWord:
            posSeg.append(k)
        if k in negWord:
            negSeg.append(k)

    '''''''''''''''''''''''''''''''''''''''
                輸出結果
    '''''''''''''''''''''''''''''''''''''''

    if len(posSeg)>len(negSeg):
        return 'POSITIVE!',posSeg,negSeg
    else:
        return 'NEGATIVE!',posSeg,negSeg



