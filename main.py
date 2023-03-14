from  random import choice
z = ["Бабушка", "Марафон", "Корабль", "Сэр", "Альянс", "Датчик", "Ералаш", "Завод", "Овсянка", "Стоп", "Утка", "Енот", "Россия", "Волга", "Сталин", "Медведь", "Пельмень", "Рабство", "Печенье", "Куртка", "Мать", "Канава", "Дорога", "Хлопок", "Поля", "Данжен", "Спортзал", "Клуб", "Лес", "Лопата", "Яма", "Тело", "Побег", "Сосиска", "Утконос", "Утка", "Топор", "Меч", "Щит" ] 
hp = 9
x = choice(z).lower()
xp = x
x = list(x.lower())
print("Wellcome to the club'Виселица'")
v = ""
win = False
zv = z
v = list(len(x)*"*")
while hp != 0:
  print("Твои попытки:", hp)
  print("Слово:", *v)
  print("Слово или буква?")
  print("[1] Слово")
  print("[2] Буква")
  heh = input("Ты выбрал: ")
  if heh == "1":
    hoho = input("Слово(пишите бувы через пробел): ").lower()
    if hoho == xp:
      print("Ты победил!")
      won = True
      break
    else:
      print("А вот и нет. Переделывай")
      hp -= 1
  if heh == "Im Racist":
    print(xp)
  if heh == "2":
    hoho = input("Буква: ").lower()
    if hoho in x:
      for c in range(len(x)):
        if hoho == x[c]:
          v[c] = hoho
    else:
      print("Этой буквы тут нет")
      hp -= 1
  if v == x :
    win = True
    break
if win == True:
  print("Ты угадал слово! ТЫ победил")
else:
  print("Ты не угадал. Это слово было - ", xp)