"""
定义敌人类
    ——数据：姓名，血量，基础攻击力，防御力
    ———行为：打印个人信息

    创建敌人列表（至少4个元素），并画出内存图。
    查找姓名是“灭霸”的敌人对象
    查找所有死亡的敌人
    计算所有敌人的平均攻击力
    删除防御力小于10的敌人
    将所有敌人攻击力增加50
"""
class Enemy:
    enemy_list = []
    def __init__(self,name,volume,ATK,defense):
        self.name = name
        self.volume = volume
        self.ATK = ATK
        self.defense = defense

    def print_info(self):
        print(self.name,self.volume,self.ATK,self.defense)

    @classmethod
    def Append(cls):
        while True:
            name = input("输入姓名：")
            if name == "":
                break
            volume = int(input("输入血量："))
            ATK = int(input("输入攻击力："))
            defense = int(input("输入防御力："))
            enemy = Enemy(name, volume, ATK, defense)
            Enemy.enemy_list.append(enemy)

    @classmethod
    def seek_name(cls,name):
        for item in Enemy.enemy_list:
            if item.name == name:
                print(item.name,item.volume,item.ATK,item.defense)

    @classmethod
    def seek_died(cls):
        for item in Enemy.enemy_list:
            if item.volume == 0:
                print(item.name,item.volume,item.ATK,item.defense)

Enemy.Append()
Enemy.seek_died()













