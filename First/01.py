# Huashi = float(input("请输入华氏温度："))
# Sheshi = (Huashi - 32)/1.8
# print(" 对应的摄氏温度是：%.2f" % Sheshi)

# r = float(input("请输入半径："))
# l = 2 * 3.14 *r
# s = 3.14 * r **2
# print("周长是：%.2f, 面积是：%.2f" %(l , s))

# x = float(input("请输入一个x："))
# if x > 1:
#     y = 3 * x - 1
# elif -1<=x<=1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print(f"{y = }")

# import random
#
# f1 = 0
# f2 = 0
# f3 = 0
# f4 = 0
# f5 = 0
# f6 = 0
# for _ in range(6000):
#     face = random.randrange(1, 7)
#     if face == 1:
#         f1 += 1
#     elif face == 2:
#         f2 += 1
#     elif face == 3:
#         f3 += 1
#     elif face == 4:
#         f4 += 1
#     elif face == 5:
#         f5 += 1
#     else:
#         f6 += 1
# print(f'1点出现了{f1}次')
# print(f'2点出现了{f2}次')
# print(f'3点出现了{f3}次')
# print(f'4点出现了{f4}次')
# print(f'5点出现了{f5}次')
# print(f'6点出现了{f6}次')

# languages = ['Python', 'Java', 'C++', 'Kotlin']
# for index in range(len(languages)):
#     print(languages[index])

# scores = []
# for _ in range(5):
#     temp = []
#     for _ in range(3):
#         score = int(input('请输入: '))
#         temp.append(score)
#     scores.append(temp)
# print(scores)

'''
#输入十个数字，找出最小值，最大值和平均值
num = []#创建一个列表
for _ in range(10):#循环10次
    temp = int(input("请输入一个数字："))
    num.append(temp)#将输入的数字添加到列表中
num.sort()
print(f"最小值是：{num[0]},最大值是：{num[-1]}，平均值是：{sum(num)/len(num)}")
'''

'''
#合并两个列表，并对合并的结果进行去除处理
num01 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num02 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

newnum = [*num01, *num02]#解包合并两个列表，也可以用"+"号合并
print(newnum)

num03 = []
for num in newnum:
    if num not in num03:
        num03.append(num)
print(num03)
'''

'''
#编写一个程序，生成1到20的平方列表

# #第一种方式
# num_list1 = []
# for i in range(1,21):
#     num_list.append(i ** 2)
# print(num_list1)

# #第二种方式
# num_list2 = [i ** 2 for i in range(1,21) ]
# print(num_list2)

# #从一个数组里面提取所有偶数，并将其平方组成一个新数组
# num_list3 = [321,3213,32133,42143,24213,32,22,44,55,44]
# num_list4 = [i ** 2 for i in num_list3 if i % 2 == 0]
# print(num_list4)
'''

# email = str(input("请输入您的邮箱："))
# if email.count("@") == 1 and "." in email:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

# sentence = str(input("请输入一句话："))
# if sentence == sentence[::-1]:
#     print(f"{sentence}是回文")
# else:
#     print(f"{sentence}不是回文")

'''
#将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
word = []
for i in range(10):
    s = str(input("请您输入十个字符串"))
    word.append(s[::-1].upper())
for s in word:
    print(s)
'''

'''
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]} {s[1]} {s[2]} {s[3]} {s[4]} {total} {avg:.1f}")
chinese_scores = [i[2] for i in students]
math_scores = [i[3] for i in students]
english_scores = [i[4] for i in students]
print(f"语文的最低分：{min(chinese_scores)}，最高分：{max(chinese_scores)}, 平均分：{sum(chinese_scores) / len(chinese_scores)}")
print(f"数学的最低分：{min(math_scores)}，最高分：{max(math_scores)}, 平均分：{sum(math_scores) / len(math_scores)}")
print(f"英语的最低分：{min(english_scores)}，最高分：{max(english_scores)}, 平均分：{sum(english_scores) / len(english_scores)}")

for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg >= 90:
        print(f"学生：{s[0]} 姓名：{s[1]} 平均分：{avg:.1f}")
'''

'''
#集合案例
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

print(french_set.intersection(art_set))
print(football_set & basketball_set & french_set & art_set)
print(football_set.difference(basketball_set))

all_set = football_set | basketball_set | french_set | art_set
all_list = [*football_set, *basketball_set, *french_set, *art_set]
for s in all_list:
    print(f"{s}选修了{all_list.count(s)}门课程")
'''














