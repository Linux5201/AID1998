"""
继承
    财产：钱不用孩子挣，但是可以花
    皇位：江山不用孩子打，但是可以做。
    代码：子类不用写，但是可以用。
"""
"""
class Person:
    def say(self):
        print("说话")

# 多个子类在概念上是一致的，所以就抽象出一个父类
# 多个子类的共性，可以提取到父类中
# 在实际开发过程中：
# 从设计角度讲：先有子，再有父
# 从编码角度讲：先有父，再有子
class Student(Person):
    def study(self):
        print("学习")



class Teacher(Person):
    def teach(self):
        print("讲课")

# 子类对象可以调用子类，也可以调用父类成员
# 父类对象只可以调用父类成员，不能调用子类成员
s01 = Student()
s01.study()
s01.say()

t01 = Teacher()
# python 内置函数
# 判断对象是否属于一个类型
# "老师对象“ 是 一个老师类型
print(isinstance(t01,Teacher)) #True
# "老师对象“ 不是 一个学生类型
print(isinstance(t01,Student)) #Flase
# "老师对象“ 是 一个人类型
print(isinstance(t01,Person)) #True

# 判断一个类型是否属于类一个类型
# ”老师类型“不是一个”学生类型“
print(issubclass(Teacher,Student)) #Flase
print(issubclass(Teacher,Person)) #True
print(issubclass(Person,Teacher)) #Flase

"""

"""

class Person:
    def __init__(self,name):
        self.name = name
        
class Student(Person):
    #子类若没有构造函数，使用父类的
    pass

s02 = Student()
s02.name

class Student(Person):
    def __init__(self,score):
        self.score = score

s01 = Student(100)
print(s01.score)

"""
"""

%初始化
clear all;                           %清除所有变量
close all;                           %清图
clc;                                 %清屏
D=4;                                %单染色体上的基因数（即4个变量）（每个基因采用10进制）    
NP=100;                              %染色体数目（初始化种群的数目）
Xs=5;                               %变量上限          
Xx=-5;                              %变量下限
G=500;                              %最大遗传代数
f=zeros(D,NP);                       %初始种群赋空间 创建一个4*100的0矩阵
nf=zeros(D,NP);                      %子种群赋空间   创建一个4*100的0矩阵
Pc=0.8;                              %交叉概率
Pm=0.1;                              %变异概率
f=rand(D,NP)*(Xs-Xx)+Xx;             %随机获得初始种群（10进制的种群），维数4*100

%按适应度升序排列
for np=1:NP
    MSLL(np)=func2(f(:,np));         %计算个染色体的适应度
end
[SortMSLL,Index]=sort(MSLL);         %sort对数组元素按升序排列 SortMSLL放排序后的数 Index放排序后的位置                          
Sortf=f(:,Index);                    %将适应度按升序排列

%遗传算法循环
for gen=1:G
    %选择最佳个体进行选择交叉操作
    Emper=Sortf(:,1);                      %最佳染色体（即最好的一个）
    NoPoint=round(D*Pc);                   %每次交叉点的个数   round取整函数
    PoPoint=randi([1 D],NoPoint,NP/2);     %交叉基因的位置   1-10 8*50矩阵
    nf=Sortf;
    %%%50个个体交叉
    for i=1:NP/2
        nf(:,2*i-1)=Emper;                 %将所有的奇数项换为君主染色体
        nf(:,2*i)=Sortf(:,2*i);            %偶数项不变
        for k=1:NoPoint
            nf(PoPoint(k,i),2*i-1)=nf(PoPoint(k,i),2*i);
            nf(PoPoint(k,i),2*i)=Emper(PoPoint(k,i));
        end
    end
   
    %变异操作
    for m=1:NP                             %对所有个体进行变异
        for n=1:D                          %每个基因都可能变异
            r=rand(1,1);
            if r<Pm
                nf(n,m)=rand(1,1)*(Xs-Xx)+Xx; %变异操作
            end
        end
    end
 
    %子种群按适应度升序排列
    for np=1:NP 
          NMSLL(np)=func2(nf(:,np));   
    end
    [NSortMSLL,Index]=sort(NMSLL);           
    NSortf=nf(:,Index);
  
    %产生新种群
    f1=[Sortf,NSortf];                %子代和父代合并
    MSLL1=[SortMSLL,NSortMSLL];       %子代和父代的适应度值合并
    [SortMSLL1,Index]=sort(MSLL

"""
import numpy as np

def func2(x):
    result = x * x
    return result.sum()


D=4                                #单染色体上的基因数（即4个变量）（每个基因采用10进制）
NP=150                             #染色体数目（初始化种群的数目）
Xs=5                               #最大遗传代数变量上限
Xx=-5                              #变量下限
G=500

f=np.zeros((D,NP))                                      #初始种群赋空间 创建一个4*100的0矩阵
nf=np.zeros((D,NP))                                     #子种群赋空间   创建一个4*100的0矩阵
Pc=0.8                                                  #交叉概率
Pm=0.1                                                  #变异概率
f=np.random.randint(-5,5,(D,NP))*(Xs-Xx)+Xx             #随机获得初始种群（10进制的种群），维数4*100

MSLL = []
#按适应度升序排列
for n_p in range(0,NP):
    MSLL.append(func2(f[:,n_p]))        #计算个染色体的适应度
MSLL.sort()
MSLL = np.array(MSLL)



#遗传算法循环
for gen in range(G):
    # 选择最佳个体进行选择交叉操作
    Emper = MSLL  # 最佳染色体（即最好的一个）
    NoPoint=round(D*Pc)                   #每次交叉点的个数   round取整函数
    PoPoint=np.random.randint(1, D, (NoPoint, NP/2))     #交叉基因的位置   1-10 8*50矩阵
    nf = MSLL
    #50个个体交叉
    for i in range(NP/2):
        MSLL[2*i+1] = Emper   # 将所有的奇数项换为君主染色体
        nf[2*i]= MSLL[2 * i]  # 偶数项不变
        for k in range(NoPoint):
            nf[2*i+1] = nf[2*i]
            nf[2 * i] = Emper[PoPoint[k,i]]
    

#     % 变异操作
#     for m=1:NP % 对所有个体进行变异
#     for n=1:D % 每个基因都可能变异
#     r = rand(1, 1);
#     if r < Pm
#         nf(n, m) = rand(1, 1) * (Xs - Xx) + Xx; % 变异操作
#     end
# end
# end









