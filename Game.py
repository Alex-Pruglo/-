import random
print('Привет, я загадал слово. Твоя задача его отгадать.')
input("Нажмите 'Enter' чтобы начать! ")
print("Начинаем!")
words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)
letters = []
win = True
HP = 10
while HP >0:
    win = True
    letter = input("Введите букву. ")
    letters.append(letter)
    for i in word:
        if i in letters:
            print(i, end=" ")
        else:
            print("*", end=" ")
            win = False
    print()
    if win:
        print("Ты победил!")
        break
    if letter not in word:
        HP -= 1
        print(f"Осталось жизней: {HP}")
if HP == 0:
    print("Ты проиграл!")
