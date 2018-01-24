import jieba

def senti(doc):

    '''''''''''''''''''''''''''''''''''''''
            
    '''''''''''''''''''''''''''''''''''''''
    sentiWord={}

    sentiSeg=[]
    sentiVal=[]

    '''''''''''''''''''''''''''''''''''''''
            讀入文字檔
    '''''''''''''''''''''''''''''''''''''''
    with open('sentimentWords.csv', 'r', encoding='UTF-8') as file:
        for data in file.readlines():
            data = data.strip()
            items = data.split(',')
            sentiWord[items[1]] = items[2]
            s = jieba.cut(doc)

        for k in s:
            try:
                  sentiVal.append(sentiWord[k])
                  sentiSeg.append(k)
            except:
               pass
        ev=0
        for k in sentiVal:
            ev = ev+(float(k)-5)

    return ev/len(sentiVal),sentiVal,sentiSeg
