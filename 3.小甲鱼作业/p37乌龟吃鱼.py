# 游戏场景10*10
# 游戏生成1只乌龟和10只鱼，移动方向随机
# 乌龟最大移动能力是2（1或者2），鱼是1
# 移动到边缘，自动反方向移动
# 乌龟体力初始（上限）是100，每次移动消耗1，鱼没有体力限制
# 乌龟，鱼坐标重叠，乌龟吃掉鱼，同时增加体力20
# 乌龟体力为0或者鱼数量为0，游戏结束

# 思路 乌龟和鱼建立两个类， 移动就是对象方法， 乌龟类有属性（体力）
import random


class Tortoise(object):
    def __init__(self, power, location_x, location_y):
        self.power = power  #体力值
        self.location_x = location_x
        self.location_y = location_y

    def move(self):
        self.power -= 1  # 移动体力槽减一
        self.location_x += random.choice([-2, -1, 0, 1, 2])  # 每次随机移动1或者2或者0个坐标值
        self.location_y += random.choice([-2, -1, 0, 1, 2])
        # 判断是否越界需要反弹
        if self.location_x < 0:
            self.location_x = abs(self.location_y)
        if self.location_x > 10:
            self.location_x = 10 - (self.location_y - 10)
        if self.location_y < 0:
            self.location_y = abs(self.location_y)
        if self.location_y > 10:
            self.location_y = 10 - (self.location_y - 10)
        return(self.location_x, self.location_y)


class Fish(object):
    def __init__(self, location_x, location_y):
        self.location_x = location_x
        self.location_y = location_y

    def move(self):
        self.location_x += random.choice([-1, 0, 1])
        self.location_y += random.choice([-1, 0, 1])
        if self.location_x < 0:
            self.location_x = abs(self.location_y)
        if self.location_x > 10:
            self.location_x = 10 - (self.location_y - 10)
        if self.location_y < 0:
            self.location_y = abs(self.location_y)
        if self.location_y > 10:
            self.location_y = 10 - (self.location_y - 10)
        return(self.location_x, self.location_y)


def battle():
    num = 10 # 初始鱼数量
    # 先生成实际对象
    tortoise = Tortoise(100, random.randint(1, 10), random.randint(1, 10))
    print(f'乌龟出生点:{tortoise.location_x}，{tortoise.location_y}')
    # 10只鱼生成一个列表保存
    fishs = []
    for i in range(0, 10):
        fishs.append(Fish(random.randint(1, 10), random.randint(1, 10)))  # 迭代添加10个鱼对象
        print(f'第{i}只鱼的出生点:{fishs[i].location_x}，{fishs[i].location_y}')
    # 游戏开始 while循环
    while 1:
        if tortoise.power == 0:
            print('乌龟没有体力，乌龟失败')
            break
        # 这里判断鱼列表为0，肯定要有个判断鱼列表为什么为0（定义一个方法，当坐标重合，删除当前对应的鱼对象）
        elif len(fishs) == 0:
            print('鱼被全部吃掉。乌龟胜利',end = ' ')
            print(f'乌龟的位置坐标是{tortoise.location_x},{tortoise.location_y}')
            print(f'乌龟的体力还有{tortoise.power}')
            break
        else:
            # 乌龟和10只金鱼同时移动一次
            tortoise.move()
            # 下面这个for循环问题在每次删除一直鱼，循环长度会变化，对应的i不一定正确
            # 尝试建立个列表，保存待删除的元素，循环完，再来一起删除对应元素！明天解决
            # 鱼列表随时在变动总数。所以按照序列删除会有问题，可能越界，只能按照值删除
            # 即便写成for i in range(0, len(fishs))还是会越界。因为里面循环是按原始len算的。但是每次循环len可能会变化
            for t in fishs:
                t.move()
                if tortoise.location_y == t.location_y and tortoise.location_x == t.location_x:
                    print(f'第{11-num}只鱼被吃掉了')
                    # 从列表删除掉这只鱼
                    fishs.remove(t)
                    num -= 1 # 鱼数量减一
                    print(f'当前还剩下{num}只鱼')
                    tortoise.power+=20
                    if tortoise.power>100:
                        tortoise.power = 100
                    # 如果恰好此时鱼吃光，继续循环，会导致下标越界    
                    if len(fishs) == 0:
                        break


if __name__ =='__main__':
    battle()
