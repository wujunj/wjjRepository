import random
words = ['program','apple','banana','like','love','pear']
idnex = random.randint(0,len(words) - 1)
word = words[idnex]
print(word)
wordbak = '-' * len(word)
print(wordbak)
guessTimes = 5
wordlst = list(wordbak)
while True:
    if guessTimes <= 0:
        break
    if '-' not in wordlst:
        break
    char = input('请输入一个字符')
    if char in word:
        for i,c in enumerate(word):
            if c == char:
                wordlst[i] = char
    else:
        guessTimes -= 1
        print('你还剩下{}次机会'.format(guessTimes))

    print(''.join(wordlst))

if guessTimes > 0 :
    print('you win')
else:
    print('you lose')
