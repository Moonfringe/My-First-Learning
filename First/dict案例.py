"""
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车
"""

print("欢迎使用购物车管理系统")
menu = """
########## 购物车系统 ##########
#        1.添加购物车          #
#        2.修改购物车          #
#        3.删除购物车          #
#        4.查询购物车          #
#        5.退出购物车          #
###############################
"""
shopping_cart = {}
while True:
    print(menu)

    choice = input("请选择要执行的操作（1-5）：")
    match choice:
        case "1":
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))
            if goods_name in shopping_cart:
                print("该商品已经存在")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("添加成功")
        case "2":
            goods_name = input("请输入您要修改的商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在")
                continue
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("修改成功")
        case "3":
            goods_name = input("请输入您要删除的商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在")
            else:
                del shopping_cart[goods_name]
                print("删除成功")
        case "4":
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name},商品价格：{goods_info['price']},商品数量：{goods_info['num']}")
        case "5":
            print("退出购物车")
            break
        case _:
            print("输入错误，请重新选择")