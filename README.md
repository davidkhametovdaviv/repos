# repos
## Программа для вычисления расстояния между двумя прямоугольниками. (v. 1.0.0)


* Умеет считать расстояние между центрами тяжести двух прямоугольников
*  Умеет считать расстояние между правым верхним и нижним левым углами двух прямоугольников
* Программа проста как $c^2 = a^2 + b^2$

![прямоугольники](https://github.com/DefBritva/repos/blob/main/image.PNG?raw=true, "Прямоугольники")



Пример кода:
```python
def corner_distance(b:int, b1:int, d:int, d1:int) -> float:
    """
    Функция для нахождения суммы растояний между верхними
    левыми и нижними правыми углами двух прямоугольников.
    
    Входные данные: соответсвующие координаты вершин двух прямоугольников.
    Выходные данные: сумма растояний между верхними левыми и нижними правыми углами двух прямоугольников.
    Генерируемые исключения: Value error ("Некорректный ввод")
    Пример использования: Вызываем функцию, передав в неё соответвующие координаты вершин прямоугольников
    """
    list1 = [b, b1, d, d1]
    x1 = list1[0][0]
    x2 = list1[1][0]
    y1 = list1[0][1]
    y2 = list1[1][1]
    x3 = list1[2][0]
    x4 = list1[3][0]
    y3 = list1[2][1]
    y4 = list1[3][1]
    res = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) + sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
    return res
```
***Данная программа была написана в ходе выполнения 5 Практической работы по предмету Введение в профессиональную деятельность. ИКИТ Прог. Инж.***
___
- [X] END
  - [X] END
    - [X] END
      - [X] END

[My vk](https://vk.com/defbritva)
___

