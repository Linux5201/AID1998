"""
超市例子
"""
class cosmetics:
    def __init__(self,grade):
        self.grad = grade

    def recommend(self,skin):
        if skin == "干燥" and self.grad == "高档":
            print("推荐您使用妮维雅")
            return 100
        elif skin == "干燥" and self.grad == "低档":
            print("推荐您使用曼秀雷敦")
            return 50
        elif skin == "油性" and self.grad == "高档":
            print("推荐您使用高夫")
            return 100
        elif skin == "油性" and self.grad == "低档":
            print("推荐您使用大宝")
            return 50

class toy:
    def __init__(self,name):
        self.name = name

    def calculate(self):
        if self.name == "飞机":
            return 100
        elif self.name == "大炮":
            return 84

class clothes:
    def __init__(self,sex,style):
        self.sex = sex
        self.style = style

    def recommend(self):
        if self.sex == "男" and self.style == "上衣":
            return 100
        elif self.sex == "男" and self.style == "裤子":
            return 90
        elif self.sex == "女" and self.style == "上衣":
            return 100
        elif self.sex == "女" and self.style == "裤子":
            return 90

class food:
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def calculate(self):
        if self.name == "方便面":
            return 10*self.number
        elif self.name == "火腿肠":
            return 5*self.number
        elif self.name == "矿泉水":
            return 3*self.number
        else:
            print("对不起，没有这个商品")

c1 = cosmetics("高档")
sum = c1.recommend("油性")
c2 = toy("飞机")
sum += c2.calculate()
c3 = clothes("男","裤子")
sum += c3.recommend()
c4 = food("方便面",5)
sum += c4.calculate()
print(sum)









