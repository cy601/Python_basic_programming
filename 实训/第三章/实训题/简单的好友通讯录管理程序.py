# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新增名片  ")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    name = input("请输入姓名：")
    phone = input("请输入电话:")

    address = input("请输入地址：")

    card_dict = {"name": name,
                 "phone": phone,
                 "address": address}
    card_list.append(card_dict)

    print(card_list)
    print("添加%s的名片成功" % name)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用新增功能添加名片！")

        # return
        return
        # 打印表头
    for name in ["姓名", "电话", "地址"]:
        print(name, end="\t\t")
    # 遍历名片列表，显示所有名片信息
    print("")
    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t" % (card_dict["name"],
                                    card_dict["phone"],
                                    card_dict["address"],
                                    ))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 提示用户输入要搜索的姓名

    find_name = input("请输入要搜索的姓名")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了")
            for name in ["姓名", "电话", "地址"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t1" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["address"],
                                        ))
            #  针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)

            break
    else:
        print("抱歉，没有找到%s" % find_name)


def deal_card(find_dict):
    """

    :param find_dict:
    :return:
    """
    print(find_dict)
    action_str = input("请选择要执行的操作 "
                       "【1】 修改 "
                       "【2】 删除 "
                       "【0】 返回上级")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "名字：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["address"] = input_card_info(find_dict["address"], "地址:")
        print("修改名片")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片")
    elif action_str == "0":
        return


def input_card_info(dict_value, tip_message):
    """

    :param dict_value:字典中原有的值
    :param tip_message:提示输入的信息
    :return:返回处理后的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value


# 无限循环
while True:
    # TODO（XX/邮件） 显示功能菜单
    show_menu()
    inputString = input("请输入你希望选择的操作：")
    print("你输入的操作是:%s" % inputString)
    # 1，2，3针对名片的操作
    if inputString in ["1", "2", "3"]:
        # 新增名片
        if inputString == "1":
            new_card()
        # 显示全部
        elif inputString == "2":
            show_all()
        # 查询名片
        elif inputString == "3":
            search_card()

        pass
    # 退出当前程序
    elif inputString == "0":
        break
        pass
    # 非法输入，重新选择
    else:
        print("非法输入，请重新输入")
