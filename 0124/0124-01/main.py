import myLexi

'''''''''''''''''''''''''''''''''''''''
            讀入文字檔
'''''''''''''''''''''''''''''''''''''''
right=0
wrong=0
with open('testSentences.csv', 'r', encoding='UTF-8') as file:
    for data in file.readlines():
        items=data.split(',')

        result,rs,ns =myLexi.senti(items[1])
        senti = float(items[3]) - 5

        k=0
        if result == 'POSITIVE!':
            k=1
        else:
            k=-1
        if senti*k > 0:
            right+=1
        else:
            wrong+=1

        print(result)
        print(senti)
        print('right:',right)
        print('wrong:',wrong)
        print('percent:',right/(right+wrong)*100)

