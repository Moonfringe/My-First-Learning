def Triangle_area(l,h):
    """
    根据三角形的底和高，计算三角形的面积
    :param l: 底
    :param h: 稿
    :return: 三角形的面积
    """
    return (l * h)/2
print(Triangle_area(5,4))

def char_Vowel(char) ->int:
    """
    判断输入的字符串中元音字母的个数
    :param char: 输入的字符串
    :return: 元音个数
    """
    Vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for i in char:
        if i in Vowels:
            count += 1
    return count
print(char_Vowel('If i am your father'))

def students_scores(score_list):
    """
    计算传入的班级学院高考成绩列表中的最高分、最低分、平均分
    :param score_list: 传入的成绩
    :return: 最高分，最低分，平均分
    """
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list)/len(score_list),1)
    return max_score,min_score,avg_score
print(students_scores([1,2,3,4,5,6,7,8,9]))

def score_grade(s):
    """
    根据传入的分数，计算对应的分数等级并返回
    :param s: 分数
    :return: 等级
    """
    if s >= 90:
        return 'A'
    elif s >= 80:
        return 'B'
    elif s >= 70:
        return 'C'
    elif s >= 60:
        return 'D'
    else:
        return 'F'
print(score_grade(95))

def char_p(char):
    """
    判断一个字符串是否是回文字符串，返回bool值
    :param char: 字符串
    :return: bool值(True or False)
    """
    if char == char[::-1]:
        return True
    else:
        return False
print(char_p("上海自来水来自海上"))

def time_convert(seconds):
    """
    将传入的秒转换为小时、分钟、秒
    :param seconds: 传入的
    :return: 转换后的
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds_after = (seconds % 3600) % 60
    return f"{seconds}秒 转换为 {hours} 小时 {minutes} 分钟 {seconds_after} 秒"

print(time_convert(3772))

def Traingle_leng(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            return "该三角形是等边三角形"
        elif a==b!=c:
            return "该三角形是等腰三角形"
        else :
            return "该三角形是普通三角形"
    return "这三条边不能构成三角形"
print(Traingle_leng(3, 4, 5))
print(Traingle_leng(3, 3, 5))
print(Traingle_leng(3, 4, 6))
print(Traingle_leng(3, 5, 6))
print(Traingle_leng(3, 4, 7))
print(Traingle_leng(8, 8, 8))

def calculate_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = round(sum(args)/len(args),1)
    return min_data,max_data,avg_data
print(calculate_data(1,2,3,4,5,6,7,8,9))
print(calculate_data(1,2,3,4,5,6,7,8,9.31221,421332,213213,3142.3))

def calculate_data(*args,**kwargs):
    """
    根据传入的这批数据，计算最小值、最大值、平均值
    :param args: 不定长位置参数
    :param kwargs: 不定长关键字参数
        round：保留的小数位个数
        print：是否打印输出
    :return: 最小值、最大值、平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"计算出来的最小值是{min_data},最大值是{max_data},平均值是{avg_data}")
    return min_data,max_data,avg_data
print(calculate_data(1,2,3,4,5,6,7,8,9,31231.421321321,round=3,print=True))

def jc(n):#递归调用
    if n == 1:
        return 1
    else:
        return n * jc(n-1)
result = jc(10)
print(result)


def total_price_cost(*args,coupon = 0,points = 0,fee:int = 0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、
    优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）
    :param coupon:优惠券
    :param points:积分抵扣
    :param fee:运费
    :return:订单的总金额
    """
    #1.计算商品的总价格--（价格 * 数量）再相加
    toal_price = [goods[1] * goods[2]for goods in args]
    total_cost = sum(toal_price)
    #2.计算优惠券及其使用条件
    if total_cost >= 5000 and coupon < total_cost:
        total_cost -= coupon
    #3.计算积分抵扣及其使用条件
    if total_cost >= 5000 and points//100 <total_cost:
        total_cost -= points //100
    #4.计算运费
    total_cost += fee
    return total_cost

print(total_price_cost(("鼠标",200,2),("键盘",500,1),("手机",10000,1),
coupon=450,points=10000,fee=9.9))














