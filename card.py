import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def printString(self):
        strValue = ''
        if self.value==1:
            strValue = "A"
        elif self.value==11:
            strValue = "J"
        elif self.value ==12:
            strValue = "Q"
        elif self.value==13:
           strValue = "K"
        else:
           strValue = str(self.value)
        return self.color+strValue

class Poke:
    colors = ["红桃", "黑桃", "方片", "草花"]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    cards={}
    def __init__(self):
        # 生成52张扑克，印刷扑克
        index = 0
        for i in range(4):
            for j in range(13):
                self.cards[index] = Card()
                self.cards[index].value=self.values[j]
                self.cards[index].color=self.colors[i]
                index+=1

    def outputCards(self):
        index2 = 0;
        for i in self.cards:
            if index2 % 13 == 0:
                print()
            print(self.cards[i].printString(),end=" ")
            index2 += 1
        print()

    # 洗牌
    def shuffle(self): 
        random.shuffle(self.cards)

   # 一手牌
    def getOneHands(self): 
        cardHands = {}
        for i in range(5):
            cardHands[i] = self.cards[i]
        return cardHands

    # 判断牌型
    def judgeHandType(self,hands):
        bIsSameColor = False
        bIsShunzi = False
        col = []
        val = []
        colset = []
        valset = []
        for i in hands:
            col.append(i.getColor())
            val.append(i.getValue())

        colset = set(col)
        valset = set(val)

        if len(colset) == 1:
            bIsSameColor = True  # 同色
        if (max(valset) - min(valset) == 4) and len(valset) == 5:
            bIsShunzi = True  # 顺子

        if (bIsSameColor and bIsShunzi):
            print('同花顺')
        elif bIsSameColor:
            print('同花')
        elif bIsShunzi:
            print('顺子')
        elif len(valset) == 5:
            print('无对')
        elif len(valset) == 4:
            print('一对')
        else:
            num = []  # 不同值的个数统计集合
            for i in valset:
                num.append(val.count(i))
            if max(num) == 4:
                print('四条')
            elif 1 not in num:
                print('满堂红')
            elif max(num) == 3:
                print('三条')
            else:
                print('两对')

        return


pock=Poke()
pock.outputCards()
pock.shuffle()
print()
print("\n洗牌后")
pock.outputCards()

hands=pock.getOneHands()
print()
print("分到的一手牌是")
print()
for i in hands:
    print(hands[i].color,hands[i].value,end=' ')
print('\n\n牌型是：')
pock.judgeHandType(hands)
