"""
学生评价系统
"""
class sc:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def evaluate(self):
        if self.score > 90:
            print(self.name + "同学成绩非常好")
        elif self.score > 80 and self.score <= 90:
            print(self.name + "同学成绩还行")
        elif self.score > 60 and self.score < 80:
            print(self.name + "同学成绩一般")
        else:
            print(self.name + "同学成绩不太好")

st01 = sc("小明",54)
st01.evaluate()