#Ща мы будем мутить моделирование бросков кубиков (Предлагаю начать с 2 кубиков). Краткий экскурс: при броске кубика, мы имеем равные шансы получить число от 1 до 6, но когда мы кидаем 2 кубика, эти шансы меняется.
#Plotly оч полезная вещь, если вы решили сделать визуализацию данных или прочих таких интересных вещей. Без лишних слов - ПОЕХАЛИ !

from random import randint

class Die():
  def __init__(self, num_sides=6 ):
    self.num_sides=num_sides # Тут мы берем число сторон кубика и объявляем его
    print (f"Well, we've got D{self.num_sides}")

  def roll (self):
    return randint(1, self.num_sides) # тут мы получаем число от 1 до 6 (если мы по дефолту ничего не вписали)

die=Die()
results=[]
for roll_num in range(1000):
  result = die.roll()
  results.append(result)

...
