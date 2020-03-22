

score = []
info = []
# score = ['','',[]]
# 建立空列表
for i in range(3):
    score.append(input('请输入姓名：'))
    score.append(input('请输入学号：'))
    score.append([])
    for j in range(3):
        score[2].append(input('成绩：'))
    info.append(score)
    score = []
print(info)

for i in range(3):
    print(f'姓名：{info[i][0]}',end = '\t ')
    print(f'学号：{info[i][1]}',end = '\t ')
    for j in range(3):
        print(info[i][2][j],end = ' ')
    print()
