# GUI Basic 1
from os import read
from tkinter import *
from tkinter import ttk,messagebox
import csv
import datetime
from typing import ForwardRef

# ttk is theme of Tk

GUI = Tk() # T upper case >> case sensitive
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย By Youngchin')
GUI .geometry('600x700+500+50')  # +50 (x)+0(y) Fix Positon Display on Screen

# Create Menu Bar
menubar = Menu(GUI)
GUI.config(menu=menubar)
# file menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu) #ทำทีละเมนู
filemenu.add_command(label='Save')
filemenu.add_command(label='Save AS')
filemenu.add_command(label='Exit')
# Help menu
def About():
    messagebox.showwarning('About','This Software Create BY Youngchin')

helpmenu = Menu(menubar,tearoff=0) #tearoff=0 ไม่ให้มีเส้น -- ใน list Menu
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
helpmenu.add_command(label='Version')


# Donate menu
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Donate')

#--------------------- End Create Menu Bar -------------

#--------------------- Create Tab -------------
Tab = ttk.Notebook(GUI)
#T1 = Frame(Tab,width=400,height=400) # fix Size
#T2 = Frame(Tab,width=400) # fix Size

T1 = Frame(Tab) # fix Size
T2 = Frame(Tab) # fix Size
Tab.pack(fill=BOTH, expand=1) #ขยายเต็มจอ

#Tab.add(T1, text='Add Expense')
#Tab.add(T2, text='List Expense')


#expenseicon = PhotoImage(file='icon-calendar.png').subsample(2) ย่อรูปลงกี่เท่า
expenseicon = PhotoImage(file='icon-calendar.png')
listicon = PhotoImage(file='icon-statistics.png')

Tab.add(T1, text=f'{"Add Expense": ^50s}', image=expenseicon,compound='top') #^ ทำให้ข้อความอยู่ตรงกลาง compound='top' กำหนดให้รูปอยู่บน
Tab.add(T2, text=f'{"List Expense": ^50s}', image=listicon,compound='top')

#---------------------End Create Tab -------------

# .pack() : แปะ ส่วนต่างๆ (Widget) เข้าไปใน GUI
#F1 = ttk.LabelFrame(GUI,text='test') : มีกรอบของ Frame
F1 = Frame(T1)
F1.place(x=100,y=50)

days = {'Mon' : 'จันทร์',
        'Tue' : 'อังคาร',
        'Wed' : 'พุธ',
        'Thu' : 'พฤหัสบดี.',
        'Fri' : 'ศุกร์',
        'Sat' : 'เสาร์',
        'Sun' : 'อาทิตย์'}

def Save(event = None):
    expense = v_expense.get()
    qty = v_qty.get()
    price = v_price.get()

    if expense == '':
        print('No Data')
        messagebox.showwarning('ERROR','กรุณากรอกข้อมูล expense')
        return
    elif price == '':
        messagebox.showwarning('ERROR','กรุณากรอกข้อมูล price')
        return
    elif qty == '':
        messagebox.showwarning('ERROR','กรุณากรอกข้อมูล qty')
        return
    try:          
        today = datetime.datetime.now().strftime('%a')
        dateinsert = datetime.datetime.now().strftime('%m/%d/%Y-{}, %H:%M:%S'.format(days[today]))
        totalprice = int(qty)*int(price)
        print(' Save Item : {}  ,Price :  {} ,Qty : {} ,Totalprice : {} ,Date : {} Completed'.format(expense,price,qty,totalprice,dateinsert))
        text = ' Save Item : {}  Completed \n'.format(expense)
        text = text + 'Price :  {} ,Qty : {} ,Totalprice : {} \n'.format(price,qty,totalprice)
        text = text + 'Date : {} '.format(dateinsert)
        v_result.set(text)
        # Clear Data
        v_expense.set('')
        v_price.set('')
        v_qty.set('')
        #v_totalprice.set('')
        #Save data to csv ** import csv
        #with คือ สั่งเปิดไฟล์ แล้วปิดอัติโนมัติ ,
        #a คือการ append data , w คือ การเขียนใหม่หมดทุกครั้ง
        #newline = '' >> ทำให้ข้อมูลไม่มีบันทัดว่าง
        
        with open('savedata.csv','a',encoding='utf-8',newline = '') as f :
            fw = csv.writer(f) #สร้างฟังก์ชั่นสำหรับเขียนข้อมูล
            data = [expense,price,qty,totalprice,dateinsert]
            fw.writerow(data)
            
    # ทำให้ cursor กลับไปที่ตำแหน่งช่องกรอก
        E1.focus()
        #resulttable.delete(*resulttable.get_children())
        update_table()
		#update_record()
    except:
        print('ERROR')
        #messagebox.showerror('ERROR','กรุณาข้อมูลให้ถูกต้อง')
        messagebox.showwarning('ERROR','กรุณาข้อมูลให้ถูกต้อง')
        #messagebox.showinfo('ERROR','กรุณาข้อมูลให้ถูกต้อง')
        # Clear Data


# ทำให้สามารถกด Enter ได้
GUI.bind('<Return>',Save) # ต้องเพิ่มใน def Save ว่า Save(event = None)
FONT1 = ('Angsana New',20)
FONT2 = ('Angsana New',14)

mainicon = PhotoImage(file='icon-project.png')
MainIcon = Label(F1,image=mainicon)
MainIcon.pack()
#--------------- text 1 --------------------------
L = ttk.Label(F1,text = 'รายการค่าใช้จ่าย',font=FONT1).pack()
 # StringVar() ตัวแปรสำหรับเก็บข้อมูลใน GUI
v_expense = StringVar() #ตัวแปรสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable = v_expense,font = FONT2)
E1.pack()
#---------------End text 1 --------------------------

#---------------text 2 --------------------------
 # StringVar() ตัวแปรสำหรับเก็บข้อมูลใน GUI
L = ttk.Label(F1,text = 'ราคา (บาท)',font=FONT1).pack()
v_price= StringVar() #ตัวแปรสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable = v_price,font = FONT2)
E2.pack()
#---------------End text 2 --------------------------
#---------------text 3 --------------------------
 # StringVar() ตัวแปรสำหรับเก็บข้อมูลใน GUI
L = ttk.Label(F1,text = 'จำนวน (ชิ้น)',font=FONT1).pack()
v_qty = StringVar() #ตัวแปรสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable = v_qty,font = FONT2)
E3.pack()
#---------------End text 3 --------------------------
#---------------text 4 --------------------------
 # StringVar() ตัวแปรสำหรับเก็บข้อมูลใน GUI
'''
L = ttk.Label(F1,text = 'ราคารวมทั้งหมด (บาท)',font=FONT1).pack()
v_totalprice= StringVar() #ตัวแปรสำหรับเก็บข้อมูลใน GUI
E4 = ttk.Entry(F1,textvariable = v_totalprice,font = FONT2)
E4.pack()
'''
iconsave = PhotoImage(file='icon-save.png')
#---------------End text 4 --------------------------
#---------------Button Save --------------------------
B2 = ttk.Button(F1,text=f'{"Save" : >{10}}',image=iconsave,compound='left',command = Save) # command คือ event เมื่อกดปุ่ม
B2.pack(ipadx=30,ipady=6,pady=10)
#---------------End Button Save --------------------------


v_result = StringVar()
v_result.set('===========Result=============')
result = ttk.Label(F1, textvariable=v_result,font =FONT2,foreground='blue')
result.pack(pady = 10)

#------------------------End Tab1 ----------------------------
#------------------------Tab2 ----------------------------
F2= Frame(T2)
F2.place(x=100,y=50)
mainicon2 = PhotoImage(file='icon-list-small.png')
L = ttk.Label(T2,text = f'{"List ALL Expense" : >{10}}',image=mainicon2,compound='left',font=FONT1)
L.pack()

#mainicon2 = PhotoImage(file='icon-calc.png')
#MainIcon2 = Label(F2,image=mainicon2)
#MainIcon2.pack()

def read_csv():
    with open('savedata.csv',newline='',encoding='utf-8') as f: # open csv and auto close 
        fr = csv.reader(f) # fr = filereader
        data = list(fr) #แปลง data ให้เป็น List
        # print(data)
        # print('------------------')
        # print(data[0][0]) = for d in data:
        # for d in data:
        #     print(d[0]) # ต้องการแสดงข้อมูล Column ที่ 1
    return data 

# rs = read_csv() test to print data
# print(rs)


# def update_record():
#     getdata = read_csv()
#     v_allrecord.set('')
#     text =''
#     for d in getdata:
#         txt = '{}-----{}------{}-----{}------{}\n'.format(d[0],d[1],d[2],d[3],d[4])
#         text = text + txt
        
#     v_allrecord.set(text)

# v_allrecord = StringVar()
# v_allrecord.set('===========ALL List=============')
# allrecord = ttk.Label(F2, textvariable=v_allrecord,font =FONT2,foreground='green')
# allrecord.pack(pady =5)

# สร้าง table ด้วย Treeview
header  = ['Item','Price','Qty','Total','Dateadd']
resulttb = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttb.pack()

#resulttb.heading(header[0],text=header[0]) #กำหนดเองที column
for hd in header: # วนเพื่อแสดง Header จะได้ไม่ต้องกำหนดหลายบรรทัด
	resulttb.heading(hd,text=hd) 

#resulttb.column('Item',width=10) กำหนดเองทีละ column

headerwidth = [170,80,80,80,150] #กำหนด size ของ Header
for hd,W in zip(header,headerwidth): #วนเพื่อกำหนด size ของ Header จะได้ไม่ต้องกำหนดหลายบรรทัด
	resulttb.column(hd,width=W)

def update_table():
    resulttb.delete(*resulttb.get_children()) # คำสั่งลบข้อมูล * โดยไม่ต้องรัน Loop
	# for c in resulttb.get_children():
    #     resulttb.delete(c)
    data = read_csv()
    for dt in data:
        resulttb.insert('','end',value=dt)

update_table()

#update_record()
GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop() # ทำให้ UI รันตลอดเวลา
