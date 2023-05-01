import random

qussesTaken =0
print('Привет !Как тебя зовут?')

myName=input()

number=random.randint(1,20)
print('Что ж,'+myName+',я загадываю число 1 до 20.')

for qussesTaken in range(6):
    print('Попробуй угадать .')
    quess=input()
    quess=int(quess)

    if quess<number:
        print('Твое число слишком маленькое.')

    if quess>number:
        print ('Твое число слишком большое .')

    if quess==number :
        break
if quess==number :
   qussesTaken =str(qussesTaken +1)
   print ('Отлично ,'+myName+'!Ты справился за'+qussesTaken +'попытки!')
if quess!=number:
    number =str(number)
    print('Увы.Я загадал число '+number+'.')
