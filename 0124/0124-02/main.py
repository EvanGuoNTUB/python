import myLexi

'''''''''''''''''''''''''''''''''''''''
            讀入文字檔
'''''''''''''''''''''''''''''''''''''''

with open('data.txt', 'r', encoding='UTF-8') as file:
    data=file.read()
    EV,SV,SS =myLexi.senti(data)

    print(EV)
    print(SS)
    print(SV)

