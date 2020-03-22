# 游戏场景10*10
# 游戏生成1只乌龟和10只鱼，移动方向随机
# 乌龟最大移动能力是2（1或者2），鱼是1
# 移动到边缘，自动反方向移动
# 乌龟体力初始（上限）是100，每次移动消耗1，鱼没有体力限制
# 乌龟，鱼坐标重叠，乌龟吃掉鱼，同时增加体力20
# 乌龟体力为0或者鱼数量为0，游戏结束

# 思路 乌龟和鱼建立两个类， 移动就是对象方法， 乌龟类有属性（体力）
import random


class Turtle(object):
    def __init__(self, power, x, y):
        self.power = power
        self.x = x
        self.y = y

    def move(self):
        self.x += random.choice([-2, -1, 0, 1, 2])
        self.y += random.choice([-2, -1, 0, 1, 2])
        self.power -= 1
        if self.x < 0:
            self.x = abs(self.x)
        if self.x > 10:
            self.x = 20 - self.x
        if self.y < 0:
            self.y = abs(self.y)
        if self.y > 10:
            self.y = 20 - self.y


class Fish(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        if self.x < 0:
            self.x = abs(self.x)
        if self.x > 10:
            self.x = 20 - self.x
        if self.y < 0:
            self.y = abs(self.y)
        if self.y > 10:
            self.y = 20 - self.y


def game():
    global global_num
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    turtle = Turtle(100, a, b)
    print(f'乌龟的初始坐标是{a},{b}')
    fishs = []

    for i in range(0, 10):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        fishs.append(Fish(a, b))
        print(f'第{i}只鱼的坐标{a},{b}')
    eat_num = 0
    print(f'乌龟初始体力{turtle.power}')
    while 1:
        if turtle.power == 0:
            print(f'乌龟没有力气了。鱼胜利！当前还剩下{len(fishs)}只鱼')
            break
        elif len(fishs) == 0:
            print('鱼被吃光，乌龟胜利')
            break
        else:
            turtle.move()
            # print('乌龟当前坐标', turtle.x, turtle.y)
            # print('乌龟当前体力', turtle.power)
            for i in fishs:
                i.move()
                # print('鱼当前坐标', i.x, i.y)
                if turtle.x == i.x and turtle.y == i.y:
                    eat_num += 1
                    print('鱼被吃掉了:其编号是', eat_num)
                    turtle.power += 20
                    if turtle.power > 100:
                        turtle.power = 100
                    fishs.remove(i)
                    if len(fishs) == 0:
                        break


game()


