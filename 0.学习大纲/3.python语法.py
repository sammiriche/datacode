1：疑难重点
    不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
    可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
    a = 3
    a += 3
    最后 id(a)是会变得 但是list 使用append方法添加元素，id 不会变。

    ---------------------------
    for 双层循环跳出外循环的方法
    正常情况, break 只会跳出离他最近的内循环，（j循环）
    for i in range(1, 10):
        for j in range(1, i):
            print(f'i*j= {i*j}')
            if i * j > 20:
                break
    --------------------------            
    如果想实现i * j > 20时 外循环（i循环）也终止。
    for i in range(1, 10):
        for j in range(1, i):
            print(f'i*j= {i*j}')
            if i * j > 20:
                break
        else:
            continue
        break

    该循环正常执行内循环完继续执行continue, 跳过外层break，继续外循环。
    一旦内部break，跳出内部循环（for和else同属于内循环）else语句不会执行。
    所以就继续执行line24的break。这样通过连续两个break跳出了外循环。
    关键理解：for---else代表for循环体循环完运行的语句，内部break，else也不会执行
    但是line24的语句不属于内部循环，内部break对他无效。这就是区别。
