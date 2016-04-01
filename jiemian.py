# -*- coding: UTF-8 -*-
from dataAccess import *
from Tkinter import *


root=Tk()
root.geometry('600x400+200+200')
root.title('银行ATM系统')

info=" "
gid=0
number=''
card_number=''
password=''
card_password=''

welcome=0
enter=1
menu=2
qukuan=3
zhuanzhang=4
chayue=5
info_to_menu=6
info_to_qukuan=7
info_to_gaimiam=8
info_to_enter=9
qukuan2=10
gaimima=11
cunk=12


list=[]

frame_welcome=Frame(height = 400,width = 600)
frame_enter=Frame(height = 400,width = 600  )
frame_menu=Frame(height = 400,width = 600  )
frame_qukuan=Frame(height = 400,width = 600)
frame_zhuanzhang=Frame(height = 400,width = 600)
frame_chayue=Frame(height = 400,width = 600)
frame_info1=Frame(height = 400,width = 600)
frame_info2=Frame(height = 400,width = 600)
frame_info3=Frame(height = 400,width = 600)
frame_info4=Frame(height = 400,width = 600)
frame_qukuan2=Frame(height = 400,width = 600)
frame_gaimima=Frame(height = 400 ,width =600)
frame_cunkuang=Frame(height = 400 ,width =600)


list.append(frame_welcome)
list.append(frame_enter)
list.append(frame_menu)
list.append(frame_qukuan)
list.append(frame_zhuanzhang)
list.append(frame_chayue)
list.append(frame_info1)
list.append(frame_info2)
list.append(frame_info3)
list.append(frame_info4)
list.append(frame_qukuan2)
list.append(frame_gaimima)
list.append(frame_cunkuang)


def Welcome():
    list[welcome].forget()
    list[enter].pack()

def Enter(number,password):
    tq.delete(0.0,END)
    print number,type(number)
    print password,type(password)
    global card_number
    global card_password
    zhang_state=check_zhanghu(number)
    mima_state=0
    if zhang_state==1:
        mima_state=check_mima(number,password)
        if mima_state==1:
             card_number=number
             card_password=password
             list[enter].forget()
             list[menu].pack()
        else:
             info="密码错误！"
             tq.insert(INSERT,info)
             list[enter].forget()
             list[info_to_enter].pack()
    else:
        info="账号不存在！"
        tq.insert(INSERT,info)
        list[enter].forget()
        list[info_to_enter].pack()
    print zhang_state


def Quit():
    root.quit()

def Zhuan():
    list[menu].forget()
    list[zhuanzhang].pack()

def Qukuan():
    list[menu].forget()
    list[qukuan].pack()

def Gai():
    list[menu].forget()
    list[gaimima].pack()

def Zhuanzhang(duifan,number):
    td.delete(0.0,END)
    zhang_state=check_zhanghu(duifan)
    mima_state=0
    if zhang_state==1:
        now=getmoney(card_number)
        if now<int(number):
             info='账户余额不足！'
             td.insert(INSERT,info)
             list[zhuanzhang].forget()
             list[info_to_menu].pack()
        else:
             reduce_money(card_number,float(number))
             add_money(duifan,float(number))
             after=getmoney(card_number)
             info="转入账号 :"+str(duifan)+"\n操作类型 :转账  \n操作金额 ：RMB "+str(number)+"\n账号余额 ：RMB "+str(after)
             td.insert(INSERT,info)
             list[zhuanzhang].forget()
             list[info_to_menu].pack()
    else:
        info="账号不存在！"
        td.insert(INSERT,info)
        list[zhuanzhang].forget()
        list[info_to_menu].pack()
    tf.delete(0,END)
    tg.delete(0,END)

def Gaimima(original_pwd,new_pwd1,new_pwd2):
    tp.delete(0.0,END)
    if original_pwd!=card_password:
        info="原密码输入错误！"
        tp.insert(INSERT,info)
        list[gaimima].forget()
        list[info_to_gaimiam].pack()
    else:
        if new_pwd1!=new_pwd2:
            info="两次输入的新密码不同！"
            tp.insert(INSERT,info)
            list[gaimima].forget()
            list[info_to_gaimiam].pack()
        else:
            changepwd(card_number,new_pwd2)
            info="密码修改成功！"
            tp.insert(INSERT,info)
            list[gaimima].forget()
            list[info_to_gaimiam].pack()

    tj.delete(0,END)
    tm.delete(0,END)
    tn.delete(0,END)

def cunkuang():
    list[menu].forget()
    list[cunk].pack()

def  cun(count):
    td.delete(0.0,END)
    s=str(count).isdigit()
    if s:
             add_money(card_number,float(count))
             after=getmoney(card_number)
             info="操作类型 :存款  \n操作金额 ：RMB "+str(count)+"\n账号余额 ：RMB "+str(after)
             td.insert(INSERT,info)
             list[cunk].forget()
             list[info_to_menu].pack()
    else:
             info="输入金额错误！"
             td.insert(INSERT,info)
             list[cunk].forget()
             list[info_to_menu].pack()

    tw.delete(0,END)

def Expand():
    pass

def Qukuan_to_Menu():
    list[qukuan].forget()
    list[menu].pack()

def Info_to_Enter():
    list[info_to_enter].forget()
    list[enter].pack()

def Info_to_Menu():
    list[info_to_menu].forget()
    list[menu].pack()

def Info_to_Qukuan():
    list[info_to_qukuan].forget()
    list[qukuan].pack()

def Info_to_Gaimima():
    list[info_to_gaimiam].forget()
    list[gaimima].pack()

def qukuan2_to_qukaun():
    list[qukuan2].forget()
    list[qukuan].pack()

def Qukuan_to_Menu():
    list[qukuan].forget()
    list[menu].pack()



def  zhuanzhuang_to_menu():
    list[zhuanzhang].forget()
    list[menu].pack()

def gaimima_to_menu():
    list[gaimima].forget()
    list[menu].pack()

def cunkuan_to_menu():
    list[cunk].forget()
    list[menu].pack()

def Chayue():
    print card_number,type(card_number)
    td.delete(0.0,END)
    m=getmoney(card_number)
    info="当前账户余额是 ：RMB"+str(m)
    td.insert(INSERT,info)
    list[menu].forget()
    list[info_to_menu].pack()



def qu_one(number):
    te.delete(0.0,END)
    now=getmoney(card_number)
    if(now<number):
        info = "账户余额不足！"
        te.insert(INSERT,info)
        list[qukuan].forget()
        list[info_to_qukuan].pack()
    else:
        reduce_money(card_number,number)
        after=getmoney(card_number)
        info="操作账号 :"+str(card_number)+"\n操作类型 :取款  \n操作金额 ：RMB "+str(number)+"\n账号余额 ：RMB "+str(after)
        te.insert(INSERT,info)
        list[qukuan].forget()
        list[info_to_qukuan].pack()



def qu_two():
    list[qukuan].forget()
    list[qukuan2].pack()

def qu_three(number):
    te.delete(0.0,END)
    now=getmoney(card_number)
    if(now<number):
        info = "账户余额不足！"
        te.insert(INSERT,info)
        list[qukuan2].forget()
        list[info_to_qukuan].pack()
    else:
        reduce_money(card_number,number)
        after=getmoney(card_number)
        info="操作账号 :"+str(card_number)+"\n操作类型 :取款  \n操作金额 ：RMB "+str(number)+"\n账号余额 ：RMB "+str(after)
        te.insert(INSERT,info)
        list[qukuan2].forget()
        list[info_to_qukuan].pack()


#欢迎界面
button_1 = Button(frame_welcome, text='进入系统',command = Welcome)
button_1.place(x = 180,y =200,anchor = NW)

button_2 = Button(frame_welcome, text='退出系统',command = Quit)
button_2.place(x = 380,y =200,anchor = NW)

la=Label(frame_welcome,text="欢迎进入银行管理系统" )#,width=300, height=20)
la.place(x = 250,y = 150,anchor = NW)

#  输入界面


lb= Label(frame_enter,text="请输入你的卡号" )
lb.place(x = 150, y= 80 , anchor = NW)

tb=Entry(frame_enter ,bd = 4 ,width =40)
tb.place(x=150 , y= 110)
#card_number =tb.get()
#print card_number,type(card_number)

lc= Label(frame_enter,text="请输入你的密码" )
lc.place(x = 150, y= 140 , anchor = NW)

tc=Entry(frame_enter ,show='*', bd  = 4 ,width =40)
tc.place(x=150 , y= 170)
#card_password = tc.get()
#print card_number,type(card_password)

button_3 = Button(frame_enter, text='确定',width =15 ,command = lambda : Enter(  number = tb.get() , password = tc.get()))
button_3.place(x = 150,y =210,anchor = NW)

button_4 = Button(frame_enter, text='退出',width =15 ,command = Quit)
button_4.place(x = 300,y =210,anchor = NW)


#菜单界面
ld=Label(frame_menu,text="请选择业务" )#,width=300, height=20)
ld.place(x = 270,y = 40,anchor = NW)

button_5 = Button(frame_menu, text='取款',height = 3 ,width =15,command = Qukuan)
button_5.place(x = 150,y =80,anchor = NW)

button_6 = Button(frame_menu, text='查询余额',height = 3 ,width =15,command = Chayue)
button_6.place(x = 350,y =80,anchor = NW)

button_7 = Button(frame_menu, text='转账',height = 3 ,width =15 ,command = Zhuan)
button_7.place(x=150,y=240,anchor = NW)

button_8 = Button(frame_menu, text='修改密码',height = 3 ,width =15 ,command = Gai)
button_8.place(x=350,y=160,anchor = NW)

button_9 = Button(frame_menu, text='存款',height = 3 ,width =15 ,command = cunkuang)
button_9.place(x=150,y=160,anchor = NW)

button_10 = Button(frame_menu, text='退出',height = 3 ,width =15 ,command = Quit)
button_10.place(x=350,y=240,anchor = NW)


# 取款界面
le=Label(frame_qukuan,text="请选择取款金额" )#,width=300, height=20)
le.place(x = 270,y = 40,anchor = NW)

button_11 = Button(frame_qukuan, text='100',height = 3 ,width =15,command = lambda : qu_one(number = 100))
button_11.place(x = 150,y =80,anchor = NW)

button_12 = Button(frame_qukuan, text='800',height = 3 ,width =15,command = lambda : qu_one(number = 800))
button_12.place(x = 350,y =80,anchor = NW)

button_13 = Button(frame_qukuan, text='300',height = 3 ,width =15 ,command = lambda : qu_one(number = 300))
button_13.place(x=150,y=160,anchor = NW)

button_14= Button(frame_qukuan, text='1000',height = 3 ,width =15 ,command = lambda : qu_one(number = 1000))
button_14.place(x=350,y=160,anchor = NW)

button_15 = Button(frame_qukuan, text='500',height = 3 ,width =15 ,command = lambda : qu_one(number = 500))
button_15.place(x=150,y=240,anchor = NW)

button_16 = Button(frame_qukuan, text='其他',height = 3 ,width =15 ,command = qu_two)
button_16.place(x=350,y=240,anchor = NW)

button_17 = Button(frame_qukuan, text='返回',height = 1 ,width =15 ,command = Qukuan_to_Menu)
button_17.place(x=100,y=330,anchor = NW)

button_18 = Button(frame_qukuan, text='退出',height = 1 ,width =15 ,command = Quit)
button_18.place(x=400,y=330,anchor = NW)

# 其他  取款界面
lr= Label(frame_qukuan2,text="请输入金额" )
lr.place(x = 150, y= 110 , anchor = NW)

tr=Entry(frame_qukuan2 ,bd = 4 ,width =40)
tr.place(x=150 , y= 140)

button_33 = Button(frame_qukuan2, text='确定',width =10 ,command =lambda : qu_three(int(tr.get())))
button_33.place(x = 100,y =230,anchor = NW)

button_34 = Button(frame_qukuan2, text='返回',width =10,command = qukuan2_to_qukaun)
button_34.place(x = 250,y =230,anchor = NW)

button_35 = Button(frame_qukuan2, text='退出',width =10 ,command = Quit)
button_35.place(x = 400,y =230,anchor = NW)



#  操作信息显示界面  info_to_menu
ld= Label(frame_info1,text="操作信息显示" )
ld.place(x = 270, y= 35 , anchor = NW)

td=Text(frame_info1 ,height = 10,width =45)
td.insert(INSERT,"ffwfgwgwgwgwgwef  你也好方便为方便和查附件跟srbgbbbtrbrtb")
td.place(x=150 , y= 70,anchor = NW)

button_19 = Button(frame_info1, text='返回',width =15 ,command = Info_to_Menu)
button_19.place(x = 150,y =270,anchor = NW)

button_20 = Button(frame_info1, text='退出',width =15 ,command = Quit)
button_20.place(x = 350,y =270,anchor = NW)

#信息操作显示界面  info_to_qukuan
le= Label(frame_info2,text="操作信息显示" )
le.place(x = 270, y= 35 , anchor = NW)

te=Text(frame_info2 ,height = 10,width =45)
te.insert(INSERT,"ffwfgwgwgwgwgwef  你也好方便为方便和查附件跟srbgbbbtrbrtb")
te.place(x=150 , y= 70,anchor = NW)

button_21 = Button(frame_info2, text='返回',width =15 ,command = Info_to_Qukuan)
button_21.place(x = 150,y =270,anchor = NW)

button_22 = Button(frame_info2, text='退出',width =15 ,command = Quit)
button_22.place(x = 350,y =270,anchor = NW)


#信息操作显示界面  info_to_gaimima
lp= Label(frame_info3,text="操作信息显示" )
lp.place(x = 270, y= 35 , anchor = NW)

tp=Text(frame_info3 ,height = 10,width =45)
tp.insert(INSERT,"ffwfgwgwgwgwgwef  你也好方便为方便和查附件跟srbgbbbtrbrtb")
tp.place(x=150 , y= 70,anchor = NW)

button_29 = Button(frame_info3, text='返回',width =15 ,command = Info_to_Gaimima)
button_29.place(x = 150,y =270,anchor = NW)

button_30 = Button(frame_info3, text='退出',width =15 ,command = Quit)
button_30.place(x = 350,y =270,anchor = NW)


#信息操作显示界面  info_to_enter
lq= Label(frame_info4,text="操作信息显示" )
lq.place(x = 270, y= 35 , anchor = NW)

tq=Text(frame_info4 ,height = 10,width =45)
#tq.insert(INSERT,info)
tq.place(x=150 , y= 70,anchor = NW)

button_31 = Button(frame_info4, text='返回',width =15 ,command = Info_to_Enter)
button_31.place(x = 150,y =270,anchor = NW)

button_32 = Button(frame_info4, text='退出',width =15 ,command = Quit)
button_32.place(x = 350,y =270,anchor = NW)

# 转账界面
lf= Label(frame_zhuanzhang,text="请输入对方账户" )
lf.place(x = 150, y= 80 , anchor = NW)

tf=Entry(frame_zhuanzhang ,bd = 4 ,width =40)
tf.place(x=150 , y= 110)

lg= Label(frame_zhuanzhang,text="请输入金额" )
lg.place(x = 150, y= 140 , anchor = NW)

tg=Entry(frame_zhuanzhang ,bd = 4 ,width =40)
tg.place(x=150 , y= 170)

button_23 = Button(frame_zhuanzhang, text='确定',width =12 ,command = lambda :Zhuanzhang(duifan=tf.get(),number=tg.get()))
button_23.place(x = 100,y =270,anchor = NW)

button_24 = Button(frame_zhuanzhang, text='返回',width =12 ,command = zhuanzhuang_to_menu)
button_24.place(x = 250,y =270,anchor = NW)

button_25 = Button(frame_zhuanzhang, text='退出',width =12 ,command = Quit)
button_25.place(x = 400,y =270,anchor = NW)

# 修改密码
lj= Label(frame_gaimima,text="修改密码" )
lj.place(x = 270, y= 35 , anchor = NW)


tj=Entry(frame_gaimima ,show='*',bd = 4 ,width =40)
tj.place(x=150 , y= 100)

lm= Label(frame_gaimima,text="请输入新密码" )
lm.place(x = 150, y= 140 , anchor = NW)

tm=Entry(frame_gaimima  ,show='*',bd = 4 ,width =40)
tm.place(x=150 , y= 160)

ln= Label(frame_gaimima,text="请确认新密码" )
ln.place(x = 150, y= 200 , anchor = NW)

tn=Entry(frame_gaimima ,show='*',bd = 4 ,width =40)
tn.place(x=150 , y= 220)

button_26 = Button(frame_gaimima, text='确定',width =12 ,command = lambda :Gaimima(original_pwd=tj.get(),new_pwd1=tm.get(),new_pwd2=tn.get()))
button_26.place(x = 100,y =300,anchor = NW)

button_27 = Button(frame_gaimima, text='返回',width =12 ,command = gaimima_to_menu)
button_27.place(x = 250,y =300,anchor = NW)

button_28 = Button(frame_gaimima, text='退出',width =12 ,command = Quit)
button_28.place(x = 400,y =300,anchor = NW)


#存款

lw= Label(frame_cunkuang,text="请输入存款金额" )
lw.place(x = 150, y= 80 , anchor = NW)

tw=Entry(frame_cunkuang ,bd = 4 ,width =40)
tw.place(x=150 , y= 120)
'''
ly= Label(frame_cunkuang,text="存款金额只能是100的倍数" )
ly.place(x = 180, y= 140 , anchor = NW)
'''

button_38 = Button(frame_cunkuang, text='确定',width =12 ,command = lambda :cun(count=tw.get()))
button_38.place(x = 100,y =300,anchor = NW)

button_39 = Button(frame_cunkuang, text='返回',width =12 ,command = cunkuan_to_menu)
button_39.place(x = 250,y =300,anchor = NW)

button_40 = Button(frame_cunkuang, text='退出',width =12 ,command = Quit)
button_40.place(x = 400,y =300,anchor = NW)


list[welcome].pack()
root.mainloop()



