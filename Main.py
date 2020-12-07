#!usr/bin/env python3
# -*- coding:UTF-8 -*-

import turtle as t
import sys

t.hideturtle()#X隐藏海龟
t.speed(10)#海龟速度

def qml(h,l):#边界
    t.goto(int(-l/2)-1,int(h/2)+1)#位置初始化
    t.color('black')
    t.pendown()
    for i in range(0,4):
        if (i%2)==0:
            t.forward(l+2)
        else:
            t.forward(h+2)
        t.right(90)
    t.penup()
    
def qm(h,l):#旗面绘制函数:h高,l宽
    t.pendown()
    t.begin_fill()
    for i in range(0,4):
        if (i%2)==0:
            t.forward(l)
        else:
            t.forward(h)
        t.right(90)
    t.end_fill()
    t.penup()

def star5(f):#五角星绘制函数:f五角星直径
    t.left(18)
    t.pendown()
    t.begin_fill()
    for a in range(0,5):
        t.forward(f*0.951)
        t.right(144)
    t.end_fill()
    t.penup()
    
def PRC():#中华人民共和国国旗
    t.setheading(0)#角度初始化
    t.clear()
    h=1000#长宽关系
    l=h*1.5
    t.penup()

    qml(h,l)#边界
    
    t.color("red")
    t.goto(int(-l/2),int(h/2))#位置初始化
    qm(h,l)#旗面绘制

    t.color("yellow")

    #大五角星
    t.goto(int(-l/6*2),int(h/2*4/5))
    t.setheading(0)
    t.right(90)
    star5(286)

    x,y=int(-l/2*2/3),int(h/4)
    
    def Xiaowujaioxing(left,forward):
        nonlocal x
        nonlocal y
        t.goto(x,y)
        t.setheading(0)
        t.left(left)
        t.forward(forward)
        star5(100)
    
    Xiaowujaioxing(31,242)
    Xiaowujaioxing(8,304)
    Xiaowujaioxing(-16,314)
    Xiaowujaioxing(-39,270)

def DPRK():#朝鲜民主主义人民共和国国旗
    t.setheading(0)#角度初始化
    t.clear()
    h=720
    l=h*2
    t.penup()

    qml(h,l)#边界
    
    t.color("red")
    
    t.goto(int(-l/2),int(h/2))#位置初始化
    qm(h,l)

    x,y=-l/2/3,0

    t.goto(x,y-h*16/36/2)

    #五星外环圆
    t.color("white")
    t.pendown()
    t.begin_fill()
    cr=int(h*32/72/2)
    t.circle(cr,360)
    t.end_fill()
    t.penup()

    t.color("red")
    star_cr=cr//100

    x,y=x,y+h*16/36/2-star_cr*3
    #五星
    t.goto(x,y)
    t.setheading(0)
    t.right(90)
    star5(310)

    #蓝色
    t.color("blue")
    t.setheading(0)
    t.goto(int(-l/2),int(h/2))#位置
    qm(h/2*0.3,l)
    t.goto(int(-l/2),int(-h/2+h/2*0.3))#位置
    qm(h/2*0.3,l)

    #白色
    t.color("white")
    t.setheading(0)
    t.goto(int(-l/2),int(h/2-h/2*0.3))#位置
    qm(h/2*1/18,l)
    t.goto(int(-l/2),int(-h/2+h/2*0.3+h/2*1/18))#位置
    qm(h/2*1/18,l)

def USA():#美利坚合众国国旗
    t.setheading(0)#角度初始化
    t.clear()
    h=1000
    l=h*1.9
    t.penup()

    qml(h,l)#边界

    #红色旗面
    t.color("red")
    t.goto(int(-l/2),int(h/2))#位置初始化
    qm(h,l)

    #白色条纹
    t.color("white")
    t.setheading(0)
    t.goto(int(-l/2),int(h/2))#位置初始化
    th=int(h*1/13)#条宽度
    a=-1
    while True:
        a=a+2
        if a==13:
            break
        t.goto(int(-l/2),int(h/2-th*a))
        t.setheading(0)
        qm(th,l)

    #蓝色方框
    t.color("darkblue")
    t.setheading(0)
    t.goto(int(-l/2),int(h/2))#位置初始化
    c=th*7
    d=l*2/5
    qm(c,d)

    sd=th*0.616#星直径
    f=c/10#星纵间距
    g=d/12#星横间距
    
    #50星
    t.color("white")
    for n in range(1,12):
        if (n%2)==1:
            for m in range(0,5):
                t.goto(int(-l/2+n*g),int(h/2-f*2*m+sd/2-f))
                t.setheading(0)
                t.right(90)
                star5(sd)
        else:
            for m in range(0,4):
                t.goto(int(-l/2+n*g),int(h/2-f*2*m+sd/2-f*2))
                t.setheading(0)
                t.right(90)
                star5(sd)
                t.goto(int(-l/2+n*g),int(h/2-f*2*m+sd/2))

def ROK():#大韩民国第六共和国国旗
    t.setheading(0)#角度初始化
    t.clear()
    h=800#长宽关系
    l=h*3/2
    t.penup()

    qml(h,l)#边界
    
    t.color('white')
    t.goto(int(-l/2),int(h/2))#位置初始化
    qm(h,l)#旗面绘制

    t.goto(0,0-h/2)
    ap=34
    r=h/4
    
    def taiji(x,y,r,c1,c2):#太极
        nonlocal h
        nonlocal ap

        t.goto(x,y)#复位
        t.setheading(180-34)
        t.color(c1)
        t.forward(r)
        t.setheading(180-34+90)
        t.pendown()
        t.begin_fill()
        t.circle(r,180)
        t.end_fill()
        t.color(c2)
        t.begin_fill()
        t.circle(r,180)
        t.circle(r/2,180)
        t.end_fill()
        t.setheading(-34)
        t.pendown()
        t.forward(r)
        t.color(c1)
        t.begin_fill()
        t.setheading(-34+90)
        t.circle(r/2,180)
        t.end_fill()
        t.penup()
        
    taiji(0,0,r,'darkblue','red')

    def bagua():#八卦
        nonlocal r
        nonlocal ap

        d=r*2
        h=d/12
        l=r

        t.color('black')

        def weizhi():#到达八卦的起始位置
            t.forward(d/4+d/24*2+d/12*3+d/2)
            t.left(90)
            t.forward(l/2)
            t.right(180)

        def chang():#长
            nonlocal d
            nonlocal l
            qm(h,l)

        def duan():#短
            nonlocal d
            nonlocal l
            qm(h,l/2-d/2/24)
            t.forward(l/2-d/2/24+d/24)
            qm(h,l/2-d/2/48)
            #t.right(180)
            t.forward(-l/2-d/2/24)
            
        def baguaq(a,b,c):
            weizhi()
            e=[a,b,c]
            for f in e:
                if f==True:
                    chang()
                else:
                    duan()
                t.right(90)
                t.forward(h+d/24)
                t.left(90)
            t.goto(0,0)
        t.setheading(180-ap)
        baguaq(1,1,1)#乾
        t.setheading(ap)
        baguaq(0,1,0)#坎
        t.setheading(-ap)
        baguaq(0,0,0)#坤
        t.setheading(180+ap)
        baguaq(1,0,1)#离

    bagua()

def JP():#日本国国旗
    t.setheading(0)#角度初始化
    t.clear()
    h=1000#长宽关系
    l=h*1.5
    t.penup()

    qml(h,l)#边界
    
    t.color('white')
    t.goto(int(-l/2),int(h/2))#位置初始化
    qm(h,l)#旗面绘制

    r=h*3/5/2
    
    t.pendown()
    t.goto(0,0-r)
    t.color('red')
    t.begin_fill()
    t.circle(r,360)
    t.penup()
    t.end_fill()

def RUF():#俄罗斯联邦国旗
    t.setheading(0)#角度初始化
    t.clear()
    h=1000#长宽关系
    l=h*1.5
    t.penup()

    qml(h,l)#边界
    
    t.color('white')
    t.goto(int(-l/2),int(h/2))#位置初始化
    qm(h,l)#旗面绘制

    t.goto(int(-l/2),int(h/6))
    t.color("darkblue")
    qm(h/3,l)

    t.goto(int(-l/2),int(-h/6))
    t.color("red")
    qm(h/3,l)

def FRR():#法兰西第五共和国国旗
    t.setheading(0)#角度初始化
    t.clear()
    h=1000#长宽关系
    l=h*1.5
    t.penup()

    qml(h,l)#边界

    t.color('red')
    t.goto(int(-l/2),int(h/2))#位置初始化
    qm(h,l)#旗面绘制

    t.color('blue')
    t.goto(int(-l/2),int(h/2))
    qm(h,l/3)

    t.color('white')
    t.goto(int(-l/2+l/3),int(h/2))
    qm(h,l/3)

def ROT():#土耳其共和国国旗
    t.setheading(0)#角度初始化
    t.clear()
    h=1000#长宽关系
    l=h*1.5
    t.penup()

    qml(h,l)#边界
    
    t.color('red')
    t.goto(int(-l/2),int(h/2))#位置初始化
    qm(h,l)#旗面绘制

    #星月
    t.color('white')#月球
    t.goto(int(-l/2+h/2),int(-h/4))
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.circle(h/4,360)
    t.end_fill()
    t.penup()
    t.color('red')#阴影
    t.goto(int(-l/2+h/2+h/16),int(-h*2/5/2))
    t.pendown()
    t.setheading(0)
    t.begin_fill()
    t.circle(h*2/5/2,360)
    t.end_fill()
    t.penup()
    t.color('white')#星
    t.goto(int(-l/2+h/2+h/16-h/3/2+h/3),0)
    t.setheading(0)
    star5(h/4)
    
def main():
    
    c=int(input())
    d={0:'sys.exit()',1:'PRC()',2:'DPRK()',
       3:'USA()',4:'ROK()',5:'JP()',6:'RUF()',
       7:'FRR()',8:'ROT()'}
    eval(d[c])
    main()

main()
