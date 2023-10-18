from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk
#from tkinter import Button, simpledialog
from tkinter import simpledialog, messagebox
from tkinter import Tk, Listbox, Scrollbar
import tkinter as tk
import sys # คำสั่งปิดโปรแกรม
import sqlite3
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime

login = None
mainWindows = None

def closemenu():
    Closemenu1 = messagebox.askquestion("ยืนยัน", "คุณต้องการปิดโปรแกรมหรือไม่?")
    if  Closemenu1 == 'yes':
        mainWindows.destroy()
    sys.exit() 

def showprice():
    mainWindows = Tk()
    mainWindows.resizable(FALSE, FALSE)
    mainWindows.title("เลือกโปรแกรม")
    mainWindows.geometry("650x700+500+50")
    bg = tk.Canvas(mainWindows, width=1250, height=700, bg="#FFEFD5")
    bg.place(relx=0, rely=0)
    def fetch_coffee():

        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM coffee")
        data = cursor.fetchall()# เพื่อดึงข้อมูลทั้งหมดที่ได้มาจากการ execute SQL statement ไปเก็บไว้ในตัวแปร data

        # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
        listbox.delete(0, tk.END)
        listbox.configure(font=("consolas", 20))
        
        
        for row in data:
            listbox.insert(tk.END, f"id: {row[0]}, list: {row[1]}, price: {row[2]}")

        conn.close()

    def fetch_shot():
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM shot")
        data = cursor.fetchall()

        # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
        listbox.delete(0, tk.END)
        #listbox.configure(font=("consolas", 16))

        for row in data:
            listbox.insert(tk.END, f"id: {row[0]}, lish: {row[1]}, price: {row[2]}")
        conn.close() 

    def fetch_size():
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM size")
        data = cursor.fetchall()

        # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
        listbox.delete(0, tk.END)

        for row in data:
            listbox.insert(tk.END, f"id: {row[0]}, list: {row[1]},price: {row[2]}")
        
        conn.close()

    def fetch_type():
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM type")
        data = cursor.fetchall()

        # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
        listbox.delete(0, tk.END)

        for row in data:
            listbox.insert(tk.END, f"id: {row[0]}, list: {row[1]},price: {row[2]}")
        
        conn.close()      

 

    # สร้างเฟรมให้ listbox อยู่
    frame = tk.Frame(mainWindows)
    frame.place(x=0, y=140)

    # สร้าง listbox ในเฟรม0
    listbox = tk.Listbox(frame, width=220, height=43)
    listbox.configure(bg="#FFEFD5")
    listbox.option_add("*Font", "consolas 15")
    listbox.pack()

    buttonaliimenu = Button(mainWindows, width=10, height=3, text="ข้อมูลกาแฟ", command=fetch_coffee, bg="#DCAD67", font="Fc 12 bold", fg='black')
    buttonaliimenu.place(relx=0.133, rely=0.877)

    buttonname = Button(mainWindows, width=10, height=3, text="ข้อมูลช็อต", command=fetch_shot, bg="#DCAD67", font="Fc 12 bold", fg='black')
    buttonname.place(relx=0.333, rely=0.877)

    buttonname_menu = Button(mainWindows, width=10, height=3, text="ข้อมูลไซต์", command=fetch_size, bg="#DCAD67", font="Fc 12 bold", fg='black')
    buttonname_menu.place(relx=0.533, rely=0.877)

    deletebutton = Button(mainWindows, width=15, height=3, text="ข้อมูลขนาดแก้วกาแฟ", compound=tk.TOP, command=fetch_type, bg="#DCAD67", font="Fc 12 bold", fg='black')
    deletebutton.place(relx=0.733, rely=0.877)
    
    #back

    backlogin = Button(mainWindows, width=10, text="กลับ", height=1, command=lambda: (showfun(), mainWindows.destroy()), font="Fc 12 bold", bg="#FFEFD5")
    backlogin.place(relx=0.02, rely=0.03)


    mainWindows.mainloop()
        
def showallorder():
            mainWindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
            mainWindows.resizable(FALSE, FALSE)
            mainWindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
            mainWindows.geometry("1000x700+500+50")#กำหนดขนาดของหน้าจอ
            databest_canvas1 = tk.Canvas(mainWindows, width=1250, height=700, bg="#FFEFD5")
            databest_canvas1.place(relx=0, rely=0)
            def delete_data():

                # แสดง dialog เพื่อรับ ID ที่ต้องการลบ
                try:
                    user_input = int(simpledialog.askstring("Delete Data", "กรุณาเลือก id ที่จะลบข้อมูล:"))# เพื่อแสดงหน้าต่างของ dialog สำหรับการป้อนข้อมูลที่ถามผู้ใช้ "กรุณาเลือก id ที่จะลบข้อมูล
                except ValueError:#จัดการกับข้อผิดพลาดที่เกิดขึ้นเมื่อมีการแปลงข้อมูลไม่สำเร็จ
                    return  # ป้อนข้อมูลไม่ถูกต้อง (ไม่ใช่ตัวเลข) ไม่ต้องทำอะไร

                # แสดง messagebox ยืนยันการลบข้อมูล
                confirmation = messagebox.askquestion("Confirm Deletion", "คุณแน่ใจนะครับว่าจะลบข้อมูล")
                if confirmation == "yes":
                    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                    cursor = conn.cursor()

                    # ใช้คำสั่ง SQL DELETE เพื่อลบข้อมูลที่มี ID ตรงกับที่รับมา
                    cursor.execute("DELETE FROM allOrder WHERE id=?", (user_input,))
                    conn.commit()
                    conn.close()
                

            def listbox():
                frame = tk.Frame(databest_canvas1)
                frame.place(x=0, y=120)

                        # สร้าง listbox ในเฟรม
                listbox = tk.Listbox(frame, width=120, height=20, cursor="hand2")
                listbox.configure(bg="#FFEFD5")
                listbox.grid(row=1, column=3)

                        # เชื่อมต่อกับฐานข้อมูล
                conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                cursor = conn.cursor()

                        # ดึงข้อมูลจากตาราง 'allOrder' โดยใช้พารามิเตอร์ ? ในคำสั่ง SQL
                cursor.execute("SELECT * FROM 'allOrder'")
                data = cursor.fetchall()

                        # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
                listbox.delete(0, tk.END)
                listbox.configure(font=("consolas", 14))

                        # เพิ่มข้อมูลจากฐานข้อมูลลงใน Listbox
                for row in data:
                            listbox.insert(tk.END, f"id: {row[0]}\n, userid: {row[1]}\n, coffee: {row[2]}, shot: {row[3]}\n, type:{row[4]}\n, size:{row[5]}\n, price:{row[6]}\n")

                        # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
                conn.commit()

                        # ปิดการเชื่อมต่อฐานข้อมูล
                conn.close()
            listbox()
            
            backlogin = Button(mainWindows, width=10, text="กลับ", height=1, command=lambda: (showfun(), mainWindows.destroy()), font="Fc 12 bold", bg="#FFEFD5")
            backlogin.place(relx=0.02, rely=0.03)
            confrim = Button(mainWindows, width=10, text="ลบข้อมูล", height=1,command=lambda: (delete_data(),showfun(), mainWindows.destroy()),font="Fc 12 bold", bg="#E1B771")
            confrim.place(relx=0.875, rely=0.855)

def allshowuser():
            mainWindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
            mainWindows.resizable(FALSE, FALSE)
            mainWindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
            mainWindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
            databest_canvas1 = tk.Canvas(mainWindows, width=1250, height=700, bg="#FFEFD5")
            databest_canvas1.place(relx=0, rely=0)


            frame = tk.Frame(databest_canvas1)
            frame.place(x=0, y=120)

                    # สร้าง listbox ในเฟรม
            listbox = tk.Listbox(frame, width=120, height=20, cursor="hand2")
            listbox.configure(bg="#FFEFD5")
            listbox.grid(row=1, column=3)

                    # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

                    # ดึงข้อมูลจากตาราง 'allOrder' โดยใช้พารามิเตอร์ ? ในคำสั่ง SQL
            cursor.execute("SELECT * FROM 'user_id'")
            data = cursor.fetchall()

                    # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
            listbox.delete(0, tk.END)
            listbox.configure(font=("consolas", 16))

                    # เพิ่มข้อมูลจากฐานข้อมูลลงใน Listbox
            for row in data:
                        listbox.insert(tk.END, f"userid: {row[0]}\n,name: {row[1]}\n, number: {row[2]}")

                    # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
            conn.commit()

                    # ปิดการเชื่อมต่อฐานข้อมูล
            conn.close()


            backlogin = Button(mainWindows, width=10, text="กลับ", height=1, command=lambda: (showfun(), mainWindows.destroy()), font="Fc 12 bold", bg="#FFEFD5")
            backlogin.place(relx=0.02, rely=0.03)

def allshoworderinuser():
            mainWindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
            mainWindows.resizable(FALSE, FALSE)
            mainWindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
            mainWindows.geometry("1000x700+500+50")#กำหนดขนาดของหน้าจอ
            databest_canvas1 = tk.Canvas(mainWindows, width=1000, height=300, bg="#FFEFD5")
            databest_canvas1.place(relx=0, rely=0)
            databest_canvas2 = tk.Canvas(mainWindows, width=1000, height=400, bg="#FFEFD5")
            databest_canvas2.place(relx=0, rely=0.666)
            def listbox():
                iduser = int(editid1.get())
                frame = tk.Frame(databest_canvas1)
                frame.place(x=0, y=120)

                # สร้าง listbox ในเฟรม
                listbox = tk.Listbox(frame, width=180, height=20, cursor="hand2")
                listbox.configure(bg="#FFEFD5")
                listbox.grid(row=1, column=3)

                # เชื่อมต่อกับฐานข้อมูล
                conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                cursor = conn.cursor()

                # ดึงข้อมูลจากตาราง 'allOrder' โดยใช้พารามิเตอร์ ? ในคำสั่ง SQL
                cursor.execute("SELECT * FROM allOrder WHERE userid=?", (iduser,))
                data = cursor.fetchall()

                # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
                listbox.delete(0, tk.END)
                listbox.configure(font=("consolas", 15))

                # เพิ่มข้อมูลจากฐานข้อมูลลงใน Listbox
                for row in data:
                    listbox.insert(tk.END, f"id: {row[0]}\n, userid: {row[1]}\n, coffee: {row[2]}, shot: {row[3]}\n, type:{row[4]}\n, size:{row[5]}\n, price:{row[6]}\n")

                # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
                conn.commit()

                # ปิดการเชื่อมต่อฐานข้อมูล
                conn.close()

                frame2 = tk.Frame(databest_canvas2)
                frame2.place(x=0, y=120)

                # สร้าง listbox ในเฟรม
                listbox = tk.Listbox(frame2, width=120, height=20, cursor="hand2")
                listbox.configure(bg="#FFEFD5")
                listbox.grid(row=1, column=3)

                # เชื่อมต่อกับฐานข้อมูล
                conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                cursor = conn.cursor()

                # ดึงข้อมูลจากตาราง 'allOrder' โดยใช้พารามิเตอร์ ? ในคำสั่ง SQL
                cursor.execute("SELECT * FROM 'user_id' WHERE id=?", (iduser,))
                data = cursor.fetchall()

                # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
                listbox.delete(0, tk.END)
                listbox.configure(font=("consolas", 17))

                # เพิ่มข้อมูลจากฐานข้อมูลลงใน Listbox
                for row in data:
                    listbox.insert(tk.END, f"id: {row[0]}\n, name: {row[1]}\n, number: {row[2]}")

                # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
                conn.commit()

                # ปิดการเชื่อมต่อฐานข้อมูล
                conn.close()

            editid1 = Entry(mainWindows,width=19,font=("Helvetica", 14))
            editid1.place(relx=0.367, rely=0.623)

            #ปุ่มกลับ
            backlogin = Button(mainWindows, width=10, text="กลับ", height=1, command=lambda: (showfun(), mainWindows.destroy()), font="Fc 12 bold", bg="#FFEFD5")
            backlogin.place(relx=0.02, rely=0.03)

            editdatabestbest = Button(mainWindows, width=10, height=1, text="ยืนยัน", command=listbox, bg="#D7873C", font="Fc 12 bold", fg='black')
            editdatabestbest.place(relx=0.9, rely=0.82)

def showfun():
    #mainwindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
    #mainwindows.resizable(FALSE, FALSE)
    #mainwindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
    #mainwindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
    databest_canvas1 = tk.Canvas(mainWindows, width=1250, height=700, bg="#FFEFD5")
    databest_canvas1.place(relx=0, rely=0)
    doglib_image = Image.open("BGllll.png")  # ใช้ชื่อไฟล์ภาพโดยตรง (ไม่ต้องระบุ path ถ้าอยู่ในโฟลเดอร์เดียวกับโค้ด)
    doglib_image = doglib_image.resize((700, 700))
    doglib_photo = ImageTk.PhotoImage(doglib_image)
    background_label = tk.Label(mainWindows, image=doglib_photo)
    background_label.photo = doglib_photo
    background_label.place(relx=0, rely=0)
    choosecoffee = Button(mainWindows,width=15,height=4,text="ข้อมูลราคากาแฟ",command=lambda:(showprice(),mainWindows.destroy),bg="#EBC680",font="Fc 12 bold",fg='black')
    choosecoffee.place(relx=0.4, rely=0.25)
    datebest = Button(mainWindows,width=15,height=4,text="ข้อมูลรายการทั้งหมด ",command=lambda:(showallorder(),mainWindows.destroy),bg="#EBC680",font="Fc 12 bold",fg='black')
    datebest.place(relx=0.4, rely=0.40)
    editdatabestbest = Button(mainWindows,width=15,height=4,text="ข้อมูลลูกค้าทั้งหมด ",command=lambda:(allshowuser(),mainWindows.destroy),bg="#EBC680",font="Fc 12 bold",fg='black')
    editdatabestbest.place(relx=0.4, rely=0.55)
    editdatabestbest = Button(mainWindows,width=15,height=4,text="เลือกดูข้อมูลลูกค้า ",command=lambda:(allshoworderinuser(),mainWindows.destroy),bg="#EBC680",font="Fc 12 bold",fg='black')
    editdatabestbest.place(relx=0.4, rely=0.70)
    back = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    back = back.resize((55, int(55 * back.height / back.width)))
    back1 = ImageTk.PhotoImage(back)
    backlogin = Button(mainWindows,width=45,height=35,image=back1, command=home,bg="#FFEFD5")
    backlogin.place(relx=0.02, rely=0.03)
    backlogin.image = back1

def showdatabest():
    def fetch_allmenu():

        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\testdata.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM allmenu")
        data = cursor.fetchall()# เพื่อดึงข้อมูลทั้งหมดที่ได้มาจากการ execute SQL statement ไปเก็บไว้ในตัวแปร data

        # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
        listbox.delete(0, tk.END)
        listbox.configure(font=("consolas", 13))
        
        
        for row in data:
            listbox.insert(tk.END, f"allid: {row[0]}, menucoffee: {row[1]}, shot: {row[2]}, type: {row[3]}\n sweetness: {row[4]}\n size: {row[5]}\n price: {row[6]}")

        conn.close()

    def fetch_name():
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\testdata.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM name")
        data = cursor.fetchall()

        # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
        listbox.delete(0, tk.END)
        listbox.configure(font=("consolas", 16))

        for row in data:
            listbox.insert(tk.END, f"userid: {row[0]}, name: {row[1]}")
        conn.close() 

    def fetch_namemenu():
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\testdata.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM name_menu")
        data = cursor.fetchall()

        # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
        listbox.delete(0, tk.END)

        for row in data:
            listbox.insert(tk.END, f"usermenuid: {row[0]}, name: {row[1]},menucoffee: {row[2]}")
        
        conn.close()   

    def delete_data():
        selected_item = listbox.curselection()  # รับข้อมูลที่ถูกเลือกใน Listbox
        if not selected_item:
            return

        # แสดง dialog เพื่อรับ ID ที่ต้องการลบ
        try:
            user_input = int(simpledialog.askstring("Delete Data", "กรุณาเลือก id ที่จะลบข้อมูล:"))# เพื่อแสดงหน้าต่างของ dialog สำหรับการป้อนข้อมูลที่ถามผู้ใช้ "กรุณาเลือก id ที่จะลบข้อมูล
        except ValueError:#จัดการกับข้อผิดพลาดที่เกิดขึ้นเมื่อมีการแปลงข้อมูลไม่สำเร็จ
            return  # ป้อนข้อมูลไม่ถูกต้อง (ไม่ใช่ตัวเลข) ไม่ต้องทำอะไร

        # แสดง messagebox ยืนยันการลบข้อมูล
        confirmation = messagebox.askquestion("Confirm Deletion", "คุณแน่ใจนะครับว่าจะลบข้อมูล")
        if confirmation == "yes":
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\testdata.db")
            cursor = conn.cursor()

            # ใช้คำสั่ง SQL DELETE เพื่อลบข้อมูลที่มี ID ตรงกับที่รับมา
            cursor.execute("DELETE FROM allmenu WHERE allid=?", (user_input,))
              # ใช้คำสั่ง SQL DELETE เพื่อลบข้อมูลที่มี ID ตรงกับที่รับมา จากตาราง allmenu
               
                
            # ลบข้อมูลจากตาราง name ที่มี userid ตรงกับ user_input
            cursor.execute("DELETE FROM name WHERE userid=?", (user_input,))
           
                
            # ลบข้อมูลจากตาราง name_menu ที่มี usermenuid ตรงกับ user_input
            cursor.execute("DELETE FROM name_menu WHERE usermenuid=?", (user_input,))
           
                
            # ลบข้อมูลจากตาราง rammenu ที่มี romid ตรงกับ user_input
            cursor.execute("DELETE FROM rammenu WHERE romid=?", (user_input,))
            conn.commit()
            conn.close()
           

            # ลบข้อมูลออกจาก Listbox
            listbox.delete(selected_item)

    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("ข้อมูลการสั่ง")
    mainWindows.geometry("900x700+250+50")
    mainWindows = tk.Canvas(mainWindows, width=700, height=700, bg="#FFEFD5")
    mainWindows.place(relx=0, rely=0)

    # สร้างเฟรมให้ listbox อยู่
    frame = tk.Frame(mainWindows)
    frame.pack()

    # สร้าง listbox ในเฟรม
    listbox = tk.Listbox(frame, width=220, height=43)
    listbox.configure(bg="#FFEFD5")
    listbox.option_add("*Font", "consolas 15")
    listbox.pack()

    buttonaliimenu = Button(mainWindows, width=17, height=3, text="ข้อมูลการสั่งทั้งหมด", command=fetch_allmenu, bg="#DCAD67", font="Fc 12 bold", fg='black')
    buttonaliimenu.place(relx=0.155, rely=0.877)

    buttonname = Button(mainWindows, width=12, height=3, text="ข้อมูลชื่อลูกค้า", command=fetch_name, bg="#DCAD67", font="Fc 12 bold", fg='black')
    buttonname.place(relx=0.299, rely=0.877)

    buttonname_menu = Button(mainWindows, width=15, height=3, text="ข้อมูลชื่อและเมนู", command=fetch_namemenu, bg="#DCAD67", font="Fc 12 bold", fg='black')
    buttonname_menu.place(relx=0.405, rely=0.877)

    deletebutton = Button(mainWindows, width=15, height=3, text="ลบข้อมูลการสั่งทั้งหมด", compound=tk.TOP, command=delete_data, bg="#DCAD67", font="Fc 12 bold", fg='black')
    deletebutton.place(relx=0.534, rely=0.877)

    mainWindows.mainloop()

def pdf():
    result = calculate_sum_of_numbers()
    pdfmetrics.registerFont(TTFont('TH SarabunNew', r"C:\\Users\\ASUS\\Desktop\\THSarabunNew\\THSarabunNew.ttf"))

    doc = SimpleDocTemplate("invoice%s.pdf" , pagesize=letter)

    elements = []

    styles = getSampleStyleSheet()
    normal_style_head = styles['Normal']
    normal_style_head.fontName = 'TH SarabunNew'
    normal_style_head.fontSize = 20

    styles = getSampleStyleSheet()
    normal_style1 = styles['Normal']
    normal_style1.fontName = 'TH SarabunNew'
    normal_style1.fontSize = 30

    styles = getSampleStyleSheet()
    normal_style2 = styles['Normal']
    normal_style2.fontName = 'TH SarabunNew'
    normal_style2.fontSize = 25




    # สร้างคำในใบเสร็จ
    head = Paragraph("ใบเสร็จรับเงิน", normal_style1)
    head1 = Paragraph("Doglib slowbar cafe", normal_style_head)
    #head2 = Paragraph("999/9 หมู่ที่ 9 ต.ทุ่มเท อ.ทุ่มทิ้ง จ.ทุ่มครึ่ง 999999", normal_style_head)
    #datepdf = Paragraph(f"ชื่อลูกค้า : {nameuser}", normal_style_head)
    #time1 = Paragraph(f"เบอร์โทรศัพท์ : {phone}", normal_style_head)
    line = Paragraph("______________________________________________________________", normal_style_head)
    postid = Paragraph(f"POST ID {iduser}", normal_style2)
    hu1 = Paragraph(f"ชื่อลูกค้า : {nameuser}", normal_style2)
    un1 = Paragraph(f"เบอร์โทรศัพท์ : {phone}", normal_style_head)
    telun1 = Paragraph(f"Coffee : {coffeen} ", normal_style_head)
    telun2 = Paragraph(f"shot :  {shotn} ", normal_style_head)
    telun3 = Paragraph(f"type :  {typen} ", normal_style_head)
    telun4 = Paragraph(f"size :  {sizen} ", normal_style_head)
    desun1 = Paragraph(f"วันที่ {day} ", normal_style_head)
    desun3 = Paragraph(f"เวลา {time} ", normal_style_head)
    #hu2 = Paragraph("ผู้รับ : ")
    un2 = Paragraph("พนักงาน : ธนากร โยงไธสง สหรัฐ ภูสถาน", normal_style_head)
    telun2 = Paragraph("เบอร์โทร : 0917076809", normal_style_head)
    desun2 = Paragraph("------------ขอบคุณที่ใช้บริการ------------  ", normal_style_head)
    #wun2 = Paragraph("น้ำหนักพัสดุ :", normal_style_head)
    sumun2 = Paragraph(f"Total {result}   บาท", normal_style1)



    spacer = Spacer(1, 10)
    spacer1 = Spacer(1, 50)
    spacer2 = Spacer(1, 20)

    elements.append(head)
    elements.append(spacer1)
    elements.append(head1)
    elements.append(spacer)
    #elements.append(head2)
    elements.append(spacer1)
    #elements.append(datepdf)
    elements.append(spacer)
    #elements.append(time1)
    elements.append(line)
    elements.append(spacer1)
    elements.append(postid)
    elements.append(spacer1)
    elements.append(hu1)##
    elements.append(spacer2)
    elements.append(un1)
    elements.append(spacer)
    elements.append(telun1)
    elements.append(spacer)
    elements.append(telun2)
    elements.append(spacer)
    elements.append(telun3)
    elements.append(spacer)
    elements.append(telun4)
    elements.append(spacer)
    elements.append(desun1)
    elements.append(spacer)
    elements.append(desun3)
    elements.append(spacer)
    #elements.append(hu2)
    elements.append(spacer2)
    elements.append(un2)
    elements.append(spacer)
    elements.append(telun2)
    elements.append(spacer)
    elements.append(desun2)
    elements.append(spacer)
    #elements.append(wun2)
    elements.append(spacer)
    elements.append(sumun2)
    elements.append(spacer)
    elements.append(line)


    doc.build(elements)

    # เปิดสลิปpdf
    subprocess.Popen(["start", "invoice%s.pdf" ], shell=True)

def logincoffee():
    global mainWindows
    if mainWindows:
        mainWindows.destroy()
    mainWindows = Tk()
    mainWindows.resizable(FALSE, FALSE)
    mainWindows.title("เลือกโปรแกรม")
    mainWindows.geometry("650x700+500+50")



    logincolor = Canvas(mainWindows, width=650, height=700, bg="#FFEFD5")
    logincolor.place(relx=0, rely=0)

    bglogin = Image.open(r"C:\Users\ASUS\Desktop\project python\BGLOGIN (2).png") 
    bglogin = bglogin.resize((650, 700))
    bglogin1 = ImageTk.PhotoImage(bglogin)
    background_label = tk.Label(mainWindows, image=bglogin1)
    background_label.image = bglogin1
    background_label.place(relx=0, rely=0)

    
    def check1():
        try:
            tel = int(namelogin2.get())  # แปลงค่าจาก StringVar namelogin2 เป็น int
            if len(str(tel)) == 9:  # ตรวจสอบว่ามี 10 หลักหรือไม่
                confirm()
            else:
                messagebox.showerror("ข้อมูลไม่ถูกต้อง", "กรุณากรอกเบอร์โทรศัพท์ 10 ตัวเลขเท่านั้น")
        except ValueError:
            messagebox.showerror("ข้อมูลไม่ถูกต้อง", "กรุณากรอกเบอร์โทรศัพท์เป็นตัวเลขเท่านั้น")
           
    def confirm():
        idinput()
        choostcoffee()
        mainWindows.deiconify()


    def input_order(id,name,phone):
                    
                    try:
                        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                        c = conn.cursor()
                        sql = '''INSERT INTO "user_id" (id,name,number) VALUES (?,?, ?)'''
                        data = (id,name,phone)
                        c.execute(sql, data)
                        conn.commit()
                        conn.close()
                    except sqlite3.Error as e:
                        print("Error inserting data into Orders:", e)


    def idinput():
        global iduser,nameuser,phone,day,time
        now = datetime.now()
        day = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M")

        nameuser = namelogin.get()
        phone1 = int(namelogin2.get())
        phone2="0"
        phone=f'{phone2}{phone1}'
        print(phone)
        iduser= int(namelogin3.get())
        input_order( id=iduser ,name=nameuser, phone=phone)

    namelogin = Entry(mainWindows, width=13,borderwidth=0, font=("Helvetica", 17))
    namelogin.place(relx=0.410, rely=0.382)#ชื่อ

    namelogin2 = Entry(mainWindows, width=10,borderwidth=0, font=("Helvetica", 20),bg="#E38052")
    namelogin2.place(relx=0.473, rely=0.55)#เบอร์โทรศัพท์

    namelogin3 = Entry(mainWindows, width=10,borderwidth=0, font=("Helvetica", 20),bg="#FFFFFF")
    namelogin3.place(relx=0.452, rely=0.701)#ID


    back = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    back = back.resize((55, int(55 * back.height / back.width)))
    back1 = ImageTk.PhotoImage(back)
    backlogin = Button(mainWindows,width=45,height=35,image=back1, command=home,bg="#FFEFD5")
    backlogin.place(relx=0.02, rely=0.03)
    backlogin.image = back1

    Confrimlogin = Button(mainWindows, text="ยืนยัน",command=check1, bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimlogin.place(relx=0.865, rely=0.9, height=40, width=80)

    mainWindows.mainloop()

def fetch_coffee_price():
    global coffee_price,selected_item
    selected_item = listresult
    if selected_item:
        # เชื่อมต่อกับฐานข้อมูล
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        cursor = conn.cursor()

        # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
        query = "SELECT id FROM coffee WHERE list = ?"
        cursor.execute(query, (selected_item[0],))
        result = cursor.fetchone()

        # ปิดการเชื่อมต่อฐานข้อมูล
        conn.commit()
        if result:
            selected_id = int(result[0])
            print(f"Selected ID: {selected_id}")
        else:
            print("ไม่พบ ID สำหรับข้อมูลที่เลือกใน Combobox")
    def get(selected_id):
        try :
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

                # คิวรี SQL เพื่อดึงค่าจากตารางและแปลงเป็น integer
            query = '''SELECT price FROM coffee WHERE id = ?'''
            cursor.execute(query, (selected_id,))
            result = cursor.fetchone()
            if result:
                value_as_int = int(result[0])
                return value_as_int
            else:
                  return None
        except :
            conn.commit()

    coffee_price = get(selected_id)
    print(coffee_price)

def fetch_shot_price():
    global shot_price
    selected_item = shotresult
    print(selected_item)
    print(shotresult)
    if selected_item:
        # เชื่อมต่อกับฐานข้อมูล
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        cursor = conn.cursor()

        # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
        query = "SELECT id FROM shot WHERE list = ?"
        cursor.execute(query, (selected_item[0],))
        result = cursor.fetchone()

        # ปิดการเชื่อมต่อฐานข้อมูล
        conn.commit()
        if result:
            selected_id = int(result[0])
            print(f"Selected ID: {selected_id}")
        else:
            print("ไม่พบ ID ")
    def get(selected_id):
        try :
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

                # คิวรี SQL เพื่อดึงค่าจากตารางและแปลงเป็น integer
            query = '''SELECT price FROM shot WHERE id = ?'''
            cursor.execute(query, (selected_id,))
            result = cursor.fetchone()
            if result:
                value_as_int = int(result[0])
                return value_as_int
            else:
                  return None
        except :
            conn.commit()

    shot_price = get(selected_id)
    print(shot_price)

def fetch_type_price():
    global type_price
    selected_item = typeresult
    if selected_item:
        # เชื่อมต่อกับฐานข้อมูล
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        cursor = conn.cursor()

        # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
        query = "SELECT id FROM type WHERE list = ?"
        cursor.execute(query, (selected_item[0],))
        result = cursor.fetchone()

        # ปิดการเชื่อมต่อฐานข้อมูล
        conn.commit()
        if result:
            selected_id = int(result[0])
            print(f"Selected ID: {selected_id}")
        else:
            print("ไม่พบ ID ")
    def get(selected_id):
        try :
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

                # คิวรี SQL เพื่อดึงค่าจากตารางและแปลงเป็น integer
            query = '''SELECT price FROM type WHERE id = ?'''
            cursor.execute(query, (selected_id,))
            result = cursor.fetchone()
            if result:
                value_as_int = int(result[0])
                return value_as_int
            else:
                  return None
        except :
            conn.commit()

    type_price = get(selected_id)
    print(type_price)

def fetch_size_price():
    global size_price
    selected_item = sizeresult
    if selected_item:
        # เชื่อมต่อกับฐานข้อมูล
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        cursor = conn.cursor()

        # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
        query = "SELECT id FROM size WHERE list = ?"
        cursor.execute(query, (selected_item[0],))
        result = cursor.fetchone()

        # ปิดการเชื่อมต่อฐานข้อมูล
        conn.commit()
        if result:
            selected_id = int(result[0])
            print(f"Selected ID: {selected_id}")
        else:
            print("ไม่พบ ID ")
    def get(selected_id):
        try :
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

                # คิวรี SQL เพื่อดึงค่าจากตารางและแปลงเป็น integer
            query = '''SELECT price FROM size WHERE id = ?'''
            cursor.execute(query, (selected_id,))
            result = cursor.fetchone()
            if result:
                value_as_int = int(result[0])
                return value_as_int
            else:
                  return None
        except :
            conn.commit()

    size_price = get(selected_id)
    print(size_price)

def input_order(coffee, shot, size, type,price):
    try:
        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
        c = conn.cursor()
        sql = '''INSERT INTO "Order" (coffee, shot, size, type,price) VALUES (?, ?, ?, ?,?)'''
        data = (coffee, shot, size, type,price)
        c.execute(sql, data)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error inserting data into Orders:", e)

def update(coffee, shot, type, size,price, idpick):
    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
    cursor = conn.cursor()
    update_query = '''UPDATE "Order" SET coffee=?, shot=?, type=?, size=?, price=? WHERE "id"=?'''
    data = (coffee, shot, type, size,price, idpick)
    cursor.execute(update_query, data)
    conn.commit()

def delete():
    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `Order`")
    conn.commit()
    conn.close()

def insertall(userid,coffee,shot,type,size,price):
    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
    c = conn.cursor()
    sql = '''INSERT INTO "allOrder" (userid,coffee,shot,type,size,price) VALUES (?,?,?,?,?,?)'''
    data = (userid,coffee,shot,type,size,price)
    c.execute(sql, data)
    conn.commit()
    conn.close()

def updateall(userid,coffee,shot,type,size,price,pickid):
    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
    c = conn.cursor()
    sql ='''UPDATE "allOrder" SET userid=?,coffee=?,shot=?,type=?,size=?,price=? WHERE "id"=?'''
    data = (userid,coffee,shot,type,size,price,pickid)
    c.execute(sql, data)
    conn.commit()
    conn.close()

def updatecoffeeprice():
            mainwindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
            mainwindows.resizable(FALSE, FALSE)
            mainwindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
            mainwindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
            databest_canvas1 = tk.Canvas(mainwindows, width=1250, height=700, bg="#FFEFD5")
            databest_canvas1.place(relx=0, rely=0)
            def cap():  
                        id = int(editid1.get())
                        price = int(editid2.get())
                        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                        cursor = conn.cursor()
                        update_query = '''UPDATE "coffee" SET price=? WHERE "id"=?'''
                        data = (price, id)
                        cursor.execute(update_query, data)
                        conn.commit()
            editid1 = Entry(mainwindows,width=14,font=("Helvetica", 14))
            editid1.place(relx=0.367, rely=0.2)
            nameee = Label(mainwindows, text="แก้ไขเมนูที่",bg="#FFEFD5",font="Fc 15 bold",fg='black',)#แสดงผลเลขหน้าจอ
            nameee.place(relx=0.42, rely=0.14)
            editid2 = Entry(mainwindows,width=14,font=("Helvetica", 14))
            editid2.place(relx=0.367, rely=0.4)
            nameee1 = Label(mainwindows, text="ราคา",bg="#FFEFD5",font="Fc 15 bold",fg='black',)#แสดงผลเลขหน้าจอ
            nameee1.place(relx=0.42, rely=0.322)
            editdatabestbest = Button(mainwindows, width=12, height=4, text="ยืนยัน", command=cap,bg="#E1B771", font="Fc 12 bold", fg='black')
            editdatabestbest.place(relx=0.4, rely=0.60)
            backlogin = Button(mainwindows, width=10, text="กลับ", height=1, command=lambda: (updatefun(), mainwindows.destroy()), font="Fc 12 bold", bg="#FFEFD5")
            backlogin.place(relx=0.02, rely=0.03)
    
def updateshotprice():
            mainwindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
            mainwindows.resizable(FALSE, FALSE)
            mainwindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
            mainwindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
            databest_canvas1 = tk.Canvas(mainwindows, width=1250, height=700, bg="#FFEFD5")
            databest_canvas1.place(relx=0, rely=0)
            def cap():  
                        id = int(editid1.get())
                        price = int(editid2.get())
                        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                        cursor = conn.cursor()
                        update_query = '''UPDATE "shot" SET price=? WHERE "id"=?'''
                        data = (price, id)
                        cursor.execute(update_query, data)
                        conn.commit()
            editid1 = Entry(mainwindows,width=14,font=("Helvetica", 14))
            editid1.place(relx=0.367, rely=0.2)
            nameee3 = Label(mainwindows, text="แก้ไขช็อตที่",bg="#FFEFD5",font="Fc 15 bold",fg='black',)#แสดงผลเลขหน้าจอ
            nameee3.place(relx=0.42, rely=0.14)
            editid2 = Entry(mainwindows,width=14,font=("Helvetica", 14))
            editid2.place(relx=0.367, rely=0.4)
            nameee4 = Label(mainwindows, text="ราคา",bg="#FFEFD5",font="Fc 15 bold",fg='black',)#แสดงผลเลขหน้าจอ
            nameee4.place(relx=0.42, rely=0.322)
            editdatabestbest = Button(mainwindows, width=12, height=4, text="ยืนยัน", command=cap, bg="#E1B771", font="Fc 12 bold", fg='black')
            editdatabestbest.place(relx=0.4, rely=0.60)
            backlogin = Button(mainwindows, width=10, text="กลับ", height=1, command=lambda: (updatefun(), mainwindows.destroy()), font="Fc 12 bold", bg="#FFEFD5")
            backlogin.place(relx=0.02, rely=0.03)

def updatetypeprice():
            mainwindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
            mainwindows.resizable(FALSE, FALSE)
            mainwindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
            mainwindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
            databest_canvas1 = tk.Canvas(mainwindows, width=1250, height=700, bg="#FFEFD5")
            databest_canvas1.place(relx=0, rely=0)
            def cap():  
                        id = int(editid1.get())
                        price = int(editid2.get())
                        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                        cursor = conn.cursor()
                        update_query = '''UPDATE "type" SET price=? WHERE "id"=?'''
                        data = (price, id)
                        cursor.execute(update_query, data)
                        conn.commit()
            editid1 = Entry(mainwindows,width=14,font=("Helvetica", 14))
            editid1.place(relx=0.367, rely=0.2)
            nameee5 = Label(mainwindows, text="แก้ไขขนาดที่",bg="#FFEFD5",font="Fc 15 bold",fg='black',)#แสดงผลเลขหน้าจอ
            nameee5.place(relx=0.42, rely=0.14)
            editid2 = Entry(mainwindows,width=14,font=("Helvetica", 14))
            editid2.place(relx=0.367, rely=0.4)
            nameee6 = Label(mainwindows, text="ราคา",bg="#FFEFD5",font="Fc 15 bold",fg='black',)#แสดงผลเลขหน้าจอ
            nameee6.place(relx=0.42, rely=0.322)
            editdatabestbest = Button(mainwindows, width=12, height=4, text="ยืนยัน", command=cap, bg="#E1B771", font="Fc 12 bold", fg='black')
            editdatabestbest.place(relx=0.4, rely=0.60)
            backlogin = Button(mainwindows, width=10, text="กลับ", height=1, command=lambda: (updatefun(), mainwindows.destroy()), font="Fc 12 bold", bg="#FFEFD5")
            backlogin.place(relx=0.02, rely=0.03)

def updatesizeprice():
            mainwindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
            mainwindows.resizable(FALSE, FALSE)
            mainwindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
            mainwindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
            databest_canvas1 = tk.Canvas(mainwindows, width=1250, height=700, bg="#FFEFD5")
            databest_canvas1.place(relx=0, rely=0)
            def cap():  
                        id = int(editid1.get())
                        price = int(editid2.get())
                        conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
                        cursor = conn.cursor()
                        update_query = '''UPDATE "size" SET price=? WHERE "id"=?'''
                        data = (price, id)
                        cursor.execute(update_query, data)
                        conn.commit()
            editid1 = Entry(mainwindows,width=14,font=("Helvetica", 14))
            editid1.place(relx=0.367, rely=0.2)
            nameee7 = Label(mainwindows, text="แก้ไขไซต์ที่",bg="#FFEFD5",font="Fc 15 bold",fg='black')#แสดงผลเลขหน้าจอ
            nameee7.place(relx=0.42, rely=0.14)
            editid2 = Entry(mainwindows,width=14,font=("Helvetica", 14))
            editid2.place(relx=0.367, rely=0.4)
            nameee8 = Label(mainwindows, text="ราคา",bg="#FFEFD5",font="Fc 15 bold",fg='black',)#แสดงผลเลขหน้าจอ
            nameee8.place(relx=0.42, rely=0.322)
            editdatabestbest = Button(mainwindows, width=12, height=4, text="ยืนยัน", command=cap, bg="#E1B771", font="Fc 12 bold", fg='black')
            editdatabestbest.place(relx=0.4, rely=0.60)
            backlogin = Button(mainwindows, width=10, text="กลับ", height=1, command=lambda: (updatefun(), mainwindows.destroy()), font="Fc 12 bold", bg="#FFEFD5")
            backlogin.place(relx=0.02, rely=0.03)

def updatefun():
    #mainwindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
    #mainwindows.resizable(FALSE, FALSE)
    #mainwindows.title("Doglib slowbar cafe ☕") #สร้างชื่อของหน้าต่าง
    #mainwindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
    databest_canvas1 = tk.Canvas(mainWindows, width=1250, height=700, bg="#FFEFD5")
    databest_canvas1.place(relx=0, rely=0)
    doglib_image = Image.open("BGllll.png")  # ใช้ชื่อไฟล์ภาพโดยตรง (ไม่ต้องระบุ path ถ้าอยู่ในโฟลเดอร์เดียวกับโค้ด)
    doglib_image = doglib_image.resize((700, 700))
    doglib_photo = ImageTk.PhotoImage(doglib_image)
    background_label = tk.Label(mainWindows, image=doglib_photo)
    background_label.photo = doglib_photo
    background_label.place(relx=0, rely=0)


    choosecoffee = Button(mainWindows,width=12,height=4,text="ราคากาแฟ",command=updatecoffeeprice,bg="#EBC680",font="Fc 12 bold",fg='black')
    choosecoffee.place(relx=0.4, rely=0.25)
    datebest = Button(mainWindows,width=12,height=4,text="ราคาช็อตกาแฟ ",command=updateshotprice,bg="#EBC680",font="Fc 12 bold",fg='black')
    datebest.place(relx=0.4, rely=0.40)
    editdatabestbest = Button(mainWindows,width=12,height=4,text="ประเภทกาแฟ ",command=updatetypeprice,bg="#EBC680",font="Fc 12 bold",fg='black')
    editdatabestbest.place(relx=0.4, rely=0.55)
    editdatabestbest = Button(mainWindows,width=12,height=4,text="ขนาดแก้ว ",command=updatesizeprice,bg="#EBC680",font="Fc 12 bold",fg='black')
    editdatabestbest.place(relx=0.4, rely=0.70)
    backlogin14 = Button(mainWindows, width=10, text="กลับ", height=1, command=lambda: (home(),mainWindows.destroy), font="Fc 12 bold", bg="#FFEFD5")
    backlogin14.place(relx=0.02, rely=0.03)

def choostcoffee():
    global mainWindows,listbuttonchoostcoffee
    if mainWindows:
        mainWindows.destroy()
    mainWindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
    mainWindows.resizable(FALSE, FALSE)
    mainWindows.title("เลือกโปรแกรม") #สร้างชื่อของหน้าต่าง
    mainWindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
    
    choostcoffeecolor = Canvas(mainWindows,width=650,height=700,bg="#FFEFD5")
    choostcoffeecolor.place(relx=0, rely=0)
    
    choostcoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\bgchoose.png") 
    choostcoffee = choostcoffee.resize((650, 700))
    choostcoffee1 = ImageTk.PhotoImage(choostcoffee)
    choostcoffee_label = tk.Label(mainWindows, image=choostcoffee1)
    choostcoffee_label.image = choostcoffee1
    choostcoffee_label.place(relx=0, rely=0)

    def ChangechoostButtonColor():
        global listbuttonchoostcoffee
        for z in range(len(listbuttonchoostcoffee)):
            listbuttonchoostcoffee[z].config(bg="#DCAD67")
            
    def Coffee_func(index):
        global listresult
        ChangechoostButtonColor()
        listbuttonchoostcoffee[index].config(bg="#AE5E1A")
        if index==0:
            selected_item=1
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()
        elif index==1:
            selected_item=2
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()
        elif index==2:
            selected_item=3
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = (cursor.fetchone())
        elif index==3:
            selected_item=4
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()
        elif index==4:
            selected_item=5
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()
        elif index==5:
            selected_item=6
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()

    Cappuccino = Image.open("Capuccinobutton.png")
    Cappuccino = Cappuccino.resize((120, int(120 * Cappuccino.height / Cappuccino.width)))
    Cappuccino1 = ImageTk.PhotoImage(Cappuccino)

    choostcoffeeCappuccinobutton = Button(mainWindows,width=130,height=135,image=Cappuccino1,text="Capuccino",compound=TOP,command=lambda:Coffee_func(0),font="Fc 12 bold", bg="#DCAD67")
    choostcoffeeCappuccinobutton.image = Cappuccino1
    choostcoffeeCappuccinobutton.place(relx=0.25, rely=0.17)

    Latte = Image.open(r"C:\Users\ASUS\Desktop\project python\Latte.png")
    Latte = Latte.resize((120, int(120 * Latte.height / Latte.width)))
    Latte1 = ImageTk.PhotoImage(Latte)

    choostcoffeeLattebutton = Button(mainWindows,width=130,height=135,image=Latte1,text="Latte",compound=TOP,command=lambda:Coffee_func(1),bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeLattebutton.image = Latte1
    choostcoffeeLattebutton.place(relx=0.55, rely=0.17)#ปุ่มลาเต้

    Mocha = Image.open(r"C:\Users\ASUS\Desktop\project python\Mocha.png")
    Mocha = Mocha.resize((130, int(130 * Mocha.height / Mocha.width)))
    Mocha1 = ImageTk.PhotoImage(Mocha)
    choostcoffeeMochabutton = Button(mainWindows,width=130,height=135,image=Mocha1,text="Mocha",compound=TOP,command=lambda:Coffee_func(2),bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeMochabutton.image = Mocha1
    choostcoffeeMochabutton.place(relx=0.25, rely=0.4)#ปุ่มมอคค่า

    Macchiato = Image.open(r"C:\Users\ASUS\Desktop\project python\Macchiato.png")
    Macchiato = Macchiato.resize((120, int(120 * Macchiato.height / Macchiato.width)))
    Macchiato1 = ImageTk.PhotoImage(Macchiato)
    choostcoffeeMacchiatobutton = Button(mainWindows,width=130,height=135,image=Macchiato1,compound=TOP,command=lambda:Coffee_func(3),text="Macchiato",bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeMacchiatobutton.image = Macchiato1
    choostcoffeeMacchiatobutton.place(relx=0.55, rely=0.4)#ปุ่มอเมริกาโน่

    Americano = Image.open(r"C:\Users\ASUS\Desktop\project python\Americano.png")
    Americano = Americano.resize((120, int(120 * Americano.height / Americano.width)))
    Americano1 = ImageTk.PhotoImage(Americano)
    choostcoffeeAmericanobutton = Button(mainWindows,width=130,height=135,image=Americano1,text="Americano",compound=TOP,command=lambda:Coffee_func(4),bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeAmericanobutton.image = Americano1
    choostcoffeeAmericanobutton.place(relx=0.25, rely=0.65)#ปุ่มEspresso

    Espresso = Image.open(r"C:\Users\ASUS\Desktop\project python\Espresso.png")
    Espresso = Espresso.resize((130, int(130 * Espresso.height / Espresso.width)))
    Espresso1 = ImageTk.PhotoImage(Espresso)
    choostcoffeeEspressobutton = Button(mainWindows,width=130,height=135,image=Espresso1,text="Espresso",compound=TOP,command=lambda:Coffee_func(5),bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeEspressobutton.image = Espresso1

    choostcoffeeEspressobutton.place(relx=0.55, rely=0.65)#ปุ่มEspresso
    listbuttonchoostcoffee = [choostcoffeeCappuccinobutton,choostcoffeeLattebutton,choostcoffeeMochabutton,choostcoffeeMacchiatobutton,choostcoffeeAmericanobutton,choostcoffeeEspressobutton]

    #ปุ่มกลับ
    back = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    back = back.resize((55, int(55 * back.height / back.width)))
    back1 = ImageTk.PhotoImage(back)
    choostcoffeebacklogin = Button(mainWindows,width=45,height=35,image=back1, command=logincoffee,bg="#FFEFD5")
    choostcoffeebacklogin.place(relx=0.02, rely=0.03)
    choostcoffeeLattebutton.image = back1
    #ปุ่มยืนยัน
    Confrimchoostcoffee = Button(mainWindows, text="ยืนยัน",command=lambda:(fetch_coffee_price(),shotcoffee()), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimchoostcoffee.place(relx=0.865, rely=0.9,height=40, width=80)

    mainWindows.mainloop()

def shotcoffee():
    global mainWindows,shotbuttonlist
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("เลือกโปรแกรม")
    mainWindows.geometry("650x700+500+50")


    mainCanvas = tk.Canvas(mainWindows, width=650, height=700, bg="#FFEFD5")
    mainCanvas.place(relx=0, rely=0)

    choostcoffee1 = Image.open(r"C:\Users\ASUS\Desktop\project python\bgshot.png") 
    choostcoffee1 = choostcoffee1.resize((650, 700))
    choostcoffee2 = ImageTk.PhotoImage(choostcoffee1)
    shotcoffee_label = tk.Label(mainWindows, image=choostcoffee2)
    shotcoffee_label.image = choostcoffee2
    shotcoffee_label.place(relx=0, rely=0)

    def ChangeshotButtonColor():
        global shotbuttonlist
        for z in range(len(shotbuttonlist)):
            shotbuttonlist[z].config(bg="#DCAD67")

    def shot_func(index):
        global shotresult
        ChangeshotButtonColor()
        shotbuttonlist[index].config(bg="#AE5E1A")
        selected_item = index
        print(selected_item)
        if index==0:
            selected_item=1
            print(selected_item)
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM shot WHERE id = ?"
            cursor.execute(query, (selected_item,))
            shotresult = cursor.fetchone()
            print(shotresult)
        elif index==1:
            selected_item=2
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM shot WHERE id = ?"
            cursor.execute(query, (selected_item,))
            shotresult = cursor.fetchone()
        elif index==2:
            selected_item=3
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM shot WHERE id = ?"
            cursor.execute(query, (selected_item,))
            shotresult = cursor.fetchone()

    oneshotcoffee = tk.Button(mainWindows, width=15,height=5, text="One shot",command=lambda:shot_func(0), bg="#DCAD67", font="Fc 12 bold", fg='black')
    oneshotcoffee.place(relx=0.4, rely=0.20)

    twoshotcoffee = tk.Button(mainWindows, width=15, height=5, text="Two shot",command=lambda:shot_func(1), bg="#DCAD67", font="Fc 12 bold", fg='black')
    twoshotcoffee.place(relx=0.4, rely=0.40)

    Treeshotcoffee = tk.Button(mainWindows, width=15, height=5, text="Tree shot",command=lambda:shot_func(2), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Treeshotcoffee.place(relx=0.4, rely=0.60)
    
    shotbuttonlist = [oneshotcoffee,twoshotcoffee,Treeshotcoffee]

    backshotcoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    backshotcoffee = backshotcoffee.resize((55, int(55 * backshotcoffee.height / backshotcoffee.width)))
    backshotcoffee1 = ImageTk.PhotoImage(backshotcoffee)
    backshotcoffee = Button(mainWindows,width=45,height=35,image=backshotcoffee1, command=choostcoffee,bg="#FFEFD5")
    backshotcoffee.place(relx=0.02, rely=0.03)
    backshotcoffee.image = backshotcoffee1

    Confrimshot = tk.Button(mainWindows, text="ยืนยัน",command=lambda:(fetch_shot_price(),typecoffee()), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimshot.place(relx=0.865, rely=0.9, height=30, width=80)

def typecoffee():
    global mainWindows,typebuttonlist
    if mainWindows:
        mainWindows.destroy()
    mainWindows = Tk()  # สร้างหน้าต่างย่อยด้วย Toplevel
    mainWindows.resizable(False, False)
    mainWindows.title("เลือกโปรแกรม")
    mainWindows.geometry("650x700+500+50")

    mainCanvas = Canvas(mainWindows, width=650, height=700, bg="#FFEFD5")
    mainCanvas.place(relx=0, rely=0)

    typecoffee1 = Image.open(r"C:\Users\ASUS\Desktop\project python\bgtype.png") 
    typecoffee1 = typecoffee1.resize((650, 700))
    choostcoffee2 = ImageTk.PhotoImage(typecoffee1)
    typecoffee_label = tk.Label(mainWindows, image=choostcoffee2)
    typecoffee_label.image = choostcoffee2
    typecoffee_label.place(relx=0, rely=0)

    def ChangetypeButtonColor():
        global typebuttonlist
        for z in range(len(typebuttonlist)):
            typebuttonlist[z].config(bg="#DCAD67")

    def type_func(index):
        global typeresult
        ChangetypeButtonColor()
        typebuttonlist[index].config(bg="#AE5E1A")
        selected_item = index
        if index==0:
            selected_item=1
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM type WHERE id = ?"
            cursor.execute(query, (selected_item,))
            typeresult = cursor.fetchone()
        elif index==1:
            selected_item=2
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM type WHERE id = ?"
            cursor.execute(query, (selected_item,))
            typeresult = cursor.fetchone()
        elif index==2:
            selected_item=3
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM type WHERE id = ?"
            cursor.execute(query, (selected_item,))
            typeresult = cursor.fetchone()

    typehotcoffee = Button(mainWindows, width=15, height=5, text="Hot",command=lambda:type_func(0), bg="#DCAD67", font="Fc 12 bold", fg='black')
    typehotcoffee.place(relx=0.4, rely=0.20)

    typecoldcoffee = Button(mainWindows, width=15, height=5, text="Cold",command=lambda:type_func(1), bg="#DCAD67", font="Fc 12 bold", fg='black')
    typecoldcoffee.place(relx=0.4, rely=0.40)

    typefrappecoffee = Button(mainWindows, width=15, height=5, text="frappe",command=lambda:type_func(2), bg="#DCAD67", font="Fc 12 bold", fg='black')
    typefrappecoffee.place(relx=0.4, rely=0.60)

    typebuttonlist = [typehotcoffee,typecoldcoffee,typefrappecoffee]

    backtypecoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    backtypecoffee = backtypecoffee.resize((55, int(55 * backtypecoffee.height / backtypecoffee.width)))
    back3 = ImageTk.PhotoImage(backtypecoffee)
    choostcoffeebacklogin = Button(mainWindows, width=45, height=35, image=back3, command=shotcoffee, bg="#FFEFD5")
    choostcoffeebacklogin.image = back3
    choostcoffeebacklogin.place(relx=0.02, rely=0.03)
     

    Confrimtype = Button(mainWindows, text="ยืนยัน",command=lambda:(fetch_type_price(),sizecoffee()), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimtype.place(relx=0.865, rely=0.9, height=40, width=80)

    mainWindows.mainloop()

def sizecoffee():
    global mainWindows,sizebuttonlist
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("เลือกโปรแกรม")
    mainWindows.geometry("650x700+500+50")

    mainCanvas = tk.Canvas(mainWindows, width=650, height=700, bg="#FFEFD5")
    mainCanvas.place(relx=0, rely=0)

    sizecoffee1 = Image.open(r"C:\Users\ASUS\Desktop\project python\bgsize.png") 
    sizecoffee1 = sizecoffee1.resize((650, 700))
    choostcoffee2 = ImageTk.PhotoImage(sizecoffee1)
    shotcoffee_label = tk.Label(mainWindows, image=choostcoffee2)
    shotcoffee_label.image = choostcoffee2
    shotcoffee_label.place(relx=0, rely=0)

    def ChangesizeButtonColor():
        global sizebuttonlist
        for z in range(len(sizebuttonlist)):
            sizebuttonlist[z].config(bg="#DCAD67")

    def size_func(index):
        global sizeresult ,idchooesl
        ChangesizeButtonColor()
        sizebuttonlist[index].config(bg="#AE5E1A")
        selected_item = index
        idchooesl=0
        if index==0:
            selected_item=1
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM size WHERE id = ?"
            cursor.execute(query, (selected_item,))
            sizeresult = cursor.fetchone()

        elif index==1:
            selected_item=2
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM size WHERE id = ?"
            cursor.execute(query, (selected_item,))
            sizeresult = cursor.fetchone()
        elif index==2:
            selected_item=3
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM size WHERE id = ?"
            cursor.execute(query, (selected_item,))
            sizeresult = cursor.fetchone()

    sizecoffees = tk.Button(mainWindows, width=15, height=5, text="Size S",command=lambda:size_func(0), bg="#DCAD67", font="Fc 12 bold", fg='black')
    sizecoffees.place(relx=0.4, rely=0.20)

    sizecoffeem = tk.Button(mainWindows, width=15, height=5, text="Size M",command=lambda:size_func(1), bg="#DCAD67", font="Fc 12 bold", fg='black')
    sizecoffeem.place(relx=0.4, rely=0.40)

    sizecoffeel = tk.Button(mainWindows, width=15, height=5, text="Size L",command=lambda:size_func(2), bg="#DCAD67", font="Fc 12 bold", fg='black')
    sizecoffeel.place(relx=0.4, rely=0.60)

    sizebuttonlist = [sizecoffees,sizecoffeem,sizecoffeel]

    backsizecoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    backsizecoffee = backsizecoffee.resize((55, int(55 * backsizecoffee.height / backsizecoffee.width)))
    back4 = ImageTk.PhotoImage(backsizecoffee)
    backlogin = Button(mainWindows, width=45, height=35, image=back4, command=typecoffee, bg="#FFEFD5")
    backlogin.image = back4
    backlogin.place(relx=0.02, rely=0.03)

    Confrimsize = tk.Button(mainWindows, text="ยืนยัน",command=lambda:(fetch_size_price(),showorder()), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimsize.place(relx=0.865, rely=0.9, height=40, width=80)
    mainWindows.mainloop()

def qr():
   # global mainWindows
    #if mainWindows:
    #    mainWindows.destroy()
    qr_image1 = Image.open(r"C:\Users\ASUS\Desktop\project python\Qrr.png")
    qr_image1 = qr_image1.resize((650, 700))
    qr_photo2 = ImageTk.PhotoImage(qr_image1)
    qrbackground_label = tk.Label(mainWindows, image=qr_photo2)
    qrbackground_label.photo = qr_photo2
    qrbackground_label.place(relx=0, rely=0)


    #Confrimchoostcoffee = Button(mainWindows, text="ปริ้นใบเสร็จ", command=pdf, bg="#DCAD67", font="Fc 12 bold", fg='black')
    #Confrimchoostcoffee.place(relx=0.865, rely=0.9, height=40, width=80)
    mainWindows.mainloop()

def showorder():
    global mainWindows,pricecoffee,coffeep,shotp,typep,sizep
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("ออเดอร์")
    mainWindows.geometry("1000x700+500+50")

    databest_canvas = tk.Canvas(mainWindows, width=1000, height=700, bg="#FFEFD5")
    databest_canvas.place(relx=0, rely=0)
    
    pricecoffee = int(coffee_price + shot_price + type_price + size_price)
    coffeep=str("%s"%listresult)
    shotp=str("%s"%shotresult)
    typep=str("%s"%typeresult)
    sizep=str("%s"%sizeresult)
    insertall(userid=iduser,coffee=coffeep,shot=shotp,type=typep,size=sizep,price=pricecoffee)
    input_order(coffee=coffeep,shot=shotp,type=typep,size=sizep,price=pricecoffee)
    # สร้าง listbox ในเฟรม
    frame = tk.Frame(databest_canvas)
    frame.place(x=0, y=120)
    # สร้าง listbox ในเฟรม
    listbox = tk.Listbox(frame, width=120, height=20, cursor="hand2")
    listbox.configure(bg="#FFEFD5")
    listbox.grid(row=1,column=3)

    # เชื่อมต่อกับฐานข้อมูล
    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
    cursor = conn.cursor()

    # ดึงข้อมูลจากตาราง 'Order'
    cursor.execute("SELECT * FROM `Order`")
    data = cursor.fetchall()

    # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
    listbox.delete(0, tk.END)
    listbox.configure(font=("consolas", 17))

    # เพิ่มข้อมูลจากฐานข้อมูลลงใน Listbox
    for row in data:
        listbox.insert(tk.END, f"id: {row[0]}\n, coffee: {row[1]}\n, shot: {row[2]}, type: {row[3]}\n, size:{row[4]}\n, price:{row[5]}\n")

    # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
    conn.commit()

    # ปิดการเชื่อมต่อฐานข้อมูล
    conn.close()

    

    addoder = Button(mainWindows,width=12,height=3,text="สั่งเพิ่ม",command=choostcoffee,bg="#DCAD67",font="Fc 12 bold",fg='black')
    addoder.place(relx=0.2,rely=0.845)

    editorder = Button(mainWindows,width=12,height=3,text="แก้ไขเมนู",command=editmenuchoostcoffee,bg="#DCAD67",font="Fc 12 bold",fg='black')
    editorder.place(relx=0.43,rely=0.845)

    confrimorder = Button(mainWindows,width=12,height=3,text="ยืนยัน",command=lambda:(pdf(),qr()),bg="#DCAD67",font="Fc 12 bold",fg='black')
    confrimorder.place(relx=0.67,rely=0.845)

    backsizecoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    backsizecoffee = backsizecoffee.resize((55, int(55 * backsizecoffee.height / backsizecoffee.width)))
    back4 = ImageTk.PhotoImage(backsizecoffee)
    backlogin = Button(mainWindows, width=45, height=35, image=back4, command=sizecoffee, bg="#FFEFD5")
    backlogin.image = back4
    backlogin.place(relx=0.02, rely=0.03)
    mainWindows.mainloop()

def calculate_sum_of_numbers():
    global coffeen,shotn,typen,sizen
    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM 'Order'")
    rows = cursor.fetchall()
    cursor.execute("SELECT coffee FROM 'Order'")
    coffeent = cursor.fetchall()
    cursor.execute("SELECT shot FROM 'Order'")
    shotnt = cursor.fetchall()
    cursor.execute("SELECT type FROM 'Order'")
    typent = cursor.fetchall()
    cursor.execute("SELECT size FROM 'Order'")
    sizent = cursor.fetchall()
    conn.close()
    coffeen=str("%s"%coffeent)
    shotn=str("%s"%shotnt)
    typen=str("%s"%typent)
    sizen=str("%s"%sizent)
    # แปลงค่าจากข้อความ (string) เป็นตัวเลข (integer) และกำหนดค่าเริ่มต้นเป็น 0 ถ้าไม่สามารถแปลง
    total = sum(int(row[0]) if row[0].isdigit() else 0 for row in rows)
    return total

def total1():
    global mainWindows
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("ออเดอร์")
    mainWindows.geometry("650x700+500+50")

    delete()

    mainWindows.mainloop()

def editmenu():
    global mainWindows
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("ออเดอร์")
    mainWindows.geometry("1000x700+500+50")

    databest_canvas = tk.Canvas(mainWindows, width=1000, height=700, bg="#FFEFD5")
    databest_canvas.place(relx=0, rely=0)
    def idpick():
            global Menuid
            pricecoffee = int(coffee_price + shot_price + type_price + shot_price)
            Menuid = int(editid.get())
            coffeep=str("%s"%listresult)
            shotp=str("%s"%shotresult)
            typep=str("%s"%typeresult)
            sizep=str("%s"%sizeresult)
            updateall(userid=iduser,coffee=coffeep,shot=shotp,type=typep,size=sizep,price=pricecoffee,pickid=Menuid)
            update(coffee=coffeep,shot=shotp,type=typep,size=sizep,price=pricecoffee,idpick=Menuid)
    # สร้าง listbox ในเฟรม
    frame = tk.Frame(databest_canvas)
    frame.place(x=0, y=120)
    # สร้าง listbox ในเฟรม
    listbox = tk.Listbox(frame, width=120, height=20, cursor="hand2")
    listbox.configure(bg="#FFEFD5")
    listbox.grid(row=1,column=3)

    # เชื่อมต่อกับฐานข้อมูล
    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
    cursor = conn.cursor()

    # ดึงข้อมูลจากตาราง 'Order'
    cursor.execute("SELECT * FROM `Order`")
    data = cursor.fetchall()

    # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
    listbox.delete(0, tk.END)
    listbox.configure(font=("consolas", 17))

    # เพิ่มข้อมูลจากฐานข้อมูลลงใน Listbox
    for row in data:
        listbox.insert(tk.END, f"id: {row[0]}\n, coffee: {row[1]}\n, shot: {row[2]}, type: {row[3]}\n, size:{row[4]}\n, price:{row[5]}\n")

    # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
    conn.commit()

    # ปิดการเชื่อมต่อฐานข้อมูล
    conn.close()
 

    editid = Entry(mainWindows,width=14,font=("Helvetica", 14))
    editid.place(relx=0.367, rely=0.4)

    editidbutton = Button(mainWindows,width=10,height=2,text="อัพเดต",command=lambda:(idpick(),editshoworder()),bg="#DCAD67",font="Fc 12 bold",fg='black')
    editidbutton.place(relx=0.375, rely=0.6)#ปุ่มคาปู

def editmenuchoostcoffee():
    global mainWindows,listbuttonchoostcoffee
    if mainWindows:
        mainWindows.destroy()
    mainWindows = Tk() #wimdows คือตัวแปรที่คิดขึ้น
    mainWindows.resizable(FALSE, FALSE)
    mainWindows.title("เลือกโปรแกรม") #สร้างชื่อของหน้าต่าง
    mainWindows.geometry("650x700+500+50")#กำหนดขนาดของหน้าจอ
    
    choostcoffeecolor = Canvas(mainWindows,width=650,height=700,bg="#FFEFD5")
    choostcoffeecolor.place(relx=0, rely=0)
    
    choostcoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\bgchoose.png") 
    choostcoffee = choostcoffee.resize((650, 700))
    choostcoffee1 = ImageTk.PhotoImage(choostcoffee)
    choostcoffee_label = tk.Label(mainWindows, image=choostcoffee1)
    choostcoffee_label.image = choostcoffee1
    choostcoffee_label.place(relx=0, rely=0)

    def ChangechoostButtonColor():
        global listbuttonchoostcoffee
        for z in range(len(listbuttonchoostcoffee)):
            listbuttonchoostcoffee[z].config(bg="#DCAD67")
            
    def Coffee_func(index):
        global listresult
        ChangechoostButtonColor()
        listbuttonchoostcoffee[index].config(bg="#AE5E1A")
        selected_item = index
        if index==0:
            selected_item=1
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()
        elif index==1:
            selected_item=2
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()
        elif index==2:
            selected_item=3
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = (cursor.fetchone())
        elif index==3:
            selected_item=4
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()
        elif index==4:
            selected_item=5
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()
        elif index==5:
            selected_item=6
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM coffee WHERE id = ?"
            cursor.execute(query, (selected_item,))
            listresult = cursor.fetchone()

    Cappuccino = Image.open("Capuccinobutton.png")
    Cappuccino = Cappuccino.resize((120, int(120 * Cappuccino.height / Cappuccino.width)))
    Cappuccino1 = ImageTk.PhotoImage(Cappuccino)

    choostcoffeeCappuccinobutton = Button(mainWindows,width=130,height=135,image=Cappuccino1,text="Capuccino",compound=TOP,command=lambda:Coffee_func(0),font="Fc 12 bold", bg="#DCAD67")
    choostcoffeeCappuccinobutton.image = Cappuccino1
    choostcoffeeCappuccinobutton.place(relx=0.25, rely=0.17)

    Latte = Image.open(r"C:\Users\ASUS\Desktop\project python\Latte.png")
    Latte = Latte.resize((120, int(120 * Latte.height / Latte.width)))
    Latte1 = ImageTk.PhotoImage(Latte)

    choostcoffeeLattebutton = Button(mainWindows,width=130,height=135,image=Latte1,text="Latte",compound=TOP,command=lambda:Coffee_func(1),bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeLattebutton.image = Latte1
    choostcoffeeLattebutton.place(relx=0.55, rely=0.17)#ปุ่มลาเต้

    Mocha = Image.open(r"C:\Users\ASUS\Desktop\project python\Mocha.png")
    Mocha = Mocha.resize((130, int(130 * Mocha.height / Mocha.width)))
    Mocha1 = ImageTk.PhotoImage(Mocha)
    choostcoffeeMochabutton = Button(mainWindows,width=130,height=135,image=Mocha1,text="Mocha",compound=TOP,command=lambda:Coffee_func(2),bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeMochabutton.image = Mocha1
    choostcoffeeMochabutton.place(relx=0.25, rely=0.4)#ปุ่มมอคค่า

    Macchiato = Image.open(r"C:\Users\ASUS\Desktop\project python\Macchiato.png")
    Macchiato = Macchiato.resize((120, int(120 * Macchiato.height / Macchiato.width)))
    Macchiato1 = ImageTk.PhotoImage(Macchiato)
    choostcoffeeMacchiatobutton = Button(mainWindows,width=130,height=135,image=Macchiato1,compound=TOP,command=lambda:Coffee_func(3),text="Macchiato",bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeMacchiatobutton.image = Macchiato1
    choostcoffeeMacchiatobutton.place(relx=0.55, rely=0.4)#ปุ่มอเมริกาโน่

    Americano = Image.open(r"C:\Users\ASUS\Desktop\project python\Americano.png")
    Americano = Americano.resize((120, int(120 * Americano.height / Americano.width)))
    Americano1 = ImageTk.PhotoImage(Americano)
    choostcoffeeAmericanobutton = Button(mainWindows,width=130,height=135,image=Americano1,text="Americano",compound=TOP,command=lambda:Coffee_func(4),bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeAmericanobutton.image = Americano1
    choostcoffeeAmericanobutton.place(relx=0.25, rely=0.65)#ปุ่มEspresso

    Espresso = Image.open(r"C:\Users\ASUS\Desktop\project python\Espresso.png")
    Espresso = Espresso.resize((130, int(130 * Espresso.height / Espresso.width)))
    Espresso1 = ImageTk.PhotoImage(Espresso)
    choostcoffeeEspressobutton = Button(mainWindows,width=130,height=135,image=Espresso1,text="Espresso",compound=TOP,command=lambda:Coffee_func(5),bg="#DCAD67",font="Fc 12 bold",fg='black')
    choostcoffeeEspressobutton.image = Espresso1

    choostcoffeeEspressobutton.place(relx=0.55, rely=0.65)#ปุ่มEspresso
    listbuttonchoostcoffee = [choostcoffeeCappuccinobutton,choostcoffeeLattebutton,choostcoffeeMochabutton,choostcoffeeMacchiatobutton,choostcoffeeAmericanobutton,choostcoffeeEspressobutton]

    #ปุ่มกลับ
    back = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    back = back.resize((55, int(55 * back.height / back.width)))
    back1 = ImageTk.PhotoImage(back)
    choostcoffeebacklogin = Button(mainWindows,width=45,height=35,image=back1, command=showorder,bg="#FFEFD5")
    choostcoffeebacklogin.place(relx=0.02, rely=0.03)
    choostcoffeeLattebutton.image = back1
    #ปุ่มยืนยัน

    Confrimchoostcoffee = Button(mainWindows, text="ยืนยัน",command=lambda:(fetch_coffee_price(),editmenushotcoffee()), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimchoostcoffee.place(relx=0.865, rely=0.9,height=40, width=80)

    mainWindows.mainloop()

def editmenushotcoffee():
    global mainWindows,shotbuttonlist
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("เลือกโปรแกรม")
    mainWindows.geometry("650x700+500+50")


    mainCanvas = tk.Canvas(mainWindows, width=650, height=700, bg="#FFEFD5")
    mainCanvas.place(relx=0, rely=0)

    choostcoffee1 = Image.open(r"C:\Users\ASUS\Desktop\project python\bgshot.png") 
    choostcoffee1 = choostcoffee1.resize((650, 700))
    choostcoffee2 = ImageTk.PhotoImage(choostcoffee1)
    shotcoffee_label = tk.Label(mainWindows, image=choostcoffee2)
    shotcoffee_label.image = choostcoffee2
    shotcoffee_label.place(relx=0, rely=0)

    def ChangeshotButtonColor():
        global shotbuttonlist
        for z in range(len(shotbuttonlist)):
            shotbuttonlist[z].config(bg="#DCAD67")

    def shot_func(index):
        global shotresult
        ChangeshotButtonColor()
        shotbuttonlist[index].config(bg="#AE5E1A")
        selected_item = index
        if index==0:
            selected_item=1
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM shot WHERE id = ?"
            cursor.execute(query, (selected_item,))
            shotresult = cursor.fetchone()
        elif index==1:
            selected_item=2
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM shot WHERE id = ?"
            cursor.execute(query, (selected_item,))
            shotresult = cursor.fetchone()
        elif index==2:
            selected_item=3
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM shot WHERE id = ?"
            cursor.execute(query, (selected_item,))
            shotresult = cursor.fetchone()

    oneshotcoffee = tk.Button(mainWindows, width=15,height=5, text="One shot",command=lambda:shot_func(0), bg="#DCAD67", font="Fc 12 bold", fg='black')
    oneshotcoffee.place(relx=0.4, rely=0.20)

    twoshotcoffee = tk.Button(mainWindows, width=15, height=5, text="Two shot",command=lambda:shot_func(1), bg="#DCAD67", font="Fc 12 bold", fg='black')
    twoshotcoffee.place(relx=0.4, rely=0.40)

    Treeshotcoffee = tk.Button(mainWindows, width=15, height=5, text="Tree shot",command=lambda:shot_func(2), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Treeshotcoffee.place(relx=0.4, rely=0.60)
    
    shotbuttonlist = [oneshotcoffee,twoshotcoffee,Treeshotcoffee]

    backshotcoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    backshotcoffee = backshotcoffee.resize((55, int(55 * backshotcoffee.height / backshotcoffee.width)))
    backshotcoffee1 = ImageTk.PhotoImage(backshotcoffee)
    backshotcoffee = Button(mainWindows,width=45,height=35,image=backshotcoffee1, command=editmenuchoostcoffee,bg="#FFEFD5")
    backshotcoffee.place(relx=0.02, rely=0.03)
    backshotcoffee.image = backshotcoffee1

    Confrimshot = tk.Button(mainWindows, text="ยืนยัน",command=lambda:(fetch_shot_price(),editmenutypecoffee()), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimshot.place(relx=0.865, rely=0.9, height=40, width=80)

def editmenutypecoffee():
    global mainWindows,typebuttonlist
    if mainWindows:
        mainWindows.destroy()
    mainWindows = Tk()  # สร้างหน้าต่างย่อยด้วย Toplevel
    mainWindows.resizable(False, False)
    mainWindows.title("เลือกโปรแกรม")
    mainWindows.geometry("650x700+500+50")

    mainCanvas = Canvas(mainWindows, width=650, height=700, bg="#FFEFD5")
    mainCanvas.place(relx=0, rely=0)

    typecoffee1 = Image.open(r"C:\Users\ASUS\Desktop\project python\bgtype.png") 
    typecoffee1 = typecoffee1.resize((650, 700))
    choostcoffee2 = ImageTk.PhotoImage(typecoffee1)
    typecoffee_label = tk.Label(mainWindows, image=choostcoffee2)
    typecoffee_label.image = choostcoffee2
    typecoffee_label.place(relx=0, rely=0)

    def ChangetypeButtonColor():
        global typebuttonlist
        for z in range(len(typebuttonlist)):
            typebuttonlist[z].config(bg="#DCAD67")

    def type_func(index):
        global typeresult
        ChangetypeButtonColor()
        typebuttonlist[index].config(bg="#AE5E1A")
        selected_item = index
        if index==0:
            selected_item=1
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM type WHERE id = ?"
            cursor.execute(query, (selected_item,))
            typeresult = cursor.fetchone()
        elif index==1:
            selected_item=2
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM type WHERE id = ?"
            cursor.execute(query, (selected_item,))
            typeresult = cursor.fetchone()
        elif index==2:
            selected_item=3
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM type WHERE id = ?"
            cursor.execute(query, (selected_item,))
            typeresult = cursor.fetchone()

    typehotcoffee = Button(mainWindows, width=15, height=5, text="Hot",command=lambda:type_func(0), bg="#DCAD67", font="Fc 12 bold", fg='black')
    typehotcoffee.place(relx=0.4, rely=0.20)

    typecoldcoffee = Button(mainWindows, width=15, height=5, text="Cold",command=lambda:type_func(1), bg="#DCAD67", font="Fc 12 bold", fg='black')
    typecoldcoffee.place(relx=0.4, rely=0.40)

    typefrappecoffee = Button(mainWindows, width=15, height=5, text="frappe",command=lambda:type_func(2), bg="#DCAD67", font="Fc 12 bold", fg='black')
    typefrappecoffee.place(relx=0.4, rely=0.60)

    typebuttonlist = [typehotcoffee,typecoldcoffee,typefrappecoffee]

    backtypecoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    backtypecoffee = backtypecoffee.resize((55, int(55 * backtypecoffee.height / backtypecoffee.width)))
    back3 = ImageTk.PhotoImage(backtypecoffee)
    choostcoffeebacklogin = Button(mainWindows, width=45, height=35, image=back3, command=editmenushotcoffee, bg="#FFEFD5")
    choostcoffeebacklogin.image = back3
    choostcoffeebacklogin.place(relx=0.02, rely=0.03)
     

    Confrimtype = Button(mainWindows, text="ยืนยัน",command=lambda:(fetch_type_price(),editmenusizecoffee()), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimtype.place(relx=0.865, rely=0.9, height=40, width=80)

    mainWindows.mainloop()

def editmenusizecoffee():
    global mainWindows,sizebuttonlist
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("เลือกโปรแกรม")
    mainWindows.geometry("650x700+500+50")

    mainCanvas = tk.Canvas(mainWindows, width=650, height=700, bg="#FFEFD5")
    mainCanvas.place(relx=0, rely=0)

    sizecoffee1 = Image.open(r"C:\Users\ASUS\Desktop\project python\bgsize.png") 
    sizecoffee1 = sizecoffee1.resize((650, 700))
    choostcoffee2 = ImageTk.PhotoImage(sizecoffee1)
    shotcoffee_label = tk.Label(mainWindows, image=choostcoffee2)
    shotcoffee_label.image = choostcoffee2
    shotcoffee_label.place(relx=0, rely=0)

    def ChangesizeButtonColor():
        global sizebuttonlist
        for z in range(len(sizebuttonlist)):
            sizebuttonlist[z].config(bg="#DCAD67")

    def size_func(index):
        global sizeresult ,idchooesl
        ChangesizeButtonColor()
        sizebuttonlist[index].config(bg="#AE5E1A")
        selected_item = index
        idchooesl=0
        if index==0:
            selected_item=1
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM size WHERE id = ?"
            cursor.execute(query, (selected_item,))
            sizeresult = cursor.fetchone()

        elif index==1:
            selected_item=2
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM size WHERE id = ?"
            cursor.execute(query, (selected_item,))
            sizeresult = cursor.fetchone()
        elif index==2:
            selected_item=3
            # เชื่อมต่อกับฐานข้อมูล
            conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
            cursor = conn.cursor()

            # คิวรี SQL เพื่อค้นหา id จากข้อมูลที่เลือกใน Combobox
            query = "SELECT list FROM size WHERE id = ?"
            cursor.execute(query, (selected_item,))
            sizeresult = cursor.fetchone()

    sizecoffees = tk.Button(mainWindows, width=15, height=5, text="Size S",command=lambda:size_func(0), bg="#DCAD67", font="Fc 12 bold", fg='black')
    sizecoffees.place(relx=0.4, rely=0.20)

    sizecoffeem = tk.Button(mainWindows, width=15, height=5, text="Size M",command=lambda:size_func(1), bg="#DCAD67", font="Fc 12 bold", fg='black')
    sizecoffeem.place(relx=0.4, rely=0.40)

    sizecoffeel = tk.Button(mainWindows, width=15, height=5, text="Size L",command=lambda:size_func(2), bg="#DCAD67", font="Fc 12 bold", fg='black')
    sizecoffeel.place(relx=0.4, rely=0.60)

    sizebuttonlist = [sizecoffees,sizecoffeem,sizecoffeel]

    backsizecoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    backsizecoffee = backsizecoffee.resize((55, int(55 * backsizecoffee.height / backsizecoffee.width)))
    back4 = ImageTk.PhotoImage(backsizecoffee)
    backlogin = Button(mainWindows, width=45, height=35, image=back4, command=editmenutypecoffee, bg="#FFEFD5")
    backlogin.image = back4
    backlogin.place(relx=0.02, rely=0.03)

    Confrimsize = tk.Button(mainWindows, text="ยืนยัน",command=lambda:(fetch_size_price(),editmenu()), bg="#DCAD67", font="Fc 12 bold", fg='black')
    Confrimsize.place(relx=0.865, rely=0.9, height=40, width=80)
    mainWindows.mainloop()

def editshoworder():
    global mainWindows
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(False, False)
    mainWindows.title("ออเดอร์")
    mainWindows.geometry("1000x700+500+50")

    databest_canvas = tk.Canvas(mainWindows, width=1000, height=700, bg="#FFEFD5")
    databest_canvas.place(relx=0, rely=0)
    

    frame = tk.Frame(databest_canvas)
    frame.place(x=0, y=120)
    # สร้าง listbox ในเฟรม
    listbox = tk.Listbox(frame, width=120, height=20, cursor="hand2")
    listbox.configure(bg="#FFEFD5")
    listbox.grid(row=1,column=3)

    # เชื่อมต่อกับฐานข้อมูล
    conn = sqlite3.connect(r"C:\Users\ASUS\Desktop\project python\dbproject.db")
    cursor = conn.cursor()

    # ดึงข้อมูลจากตาราง 'Order'
    cursor.execute("SELECT * FROM `Order`")
    data = cursor.fetchall()

    # ลบข้อมูลที่มีอยู่ใน Listbox ก่อนเพิ่มข้อมูลใหม่
    listbox.delete(0, tk.END)
    listbox.configure(font=("consolas", 17))

    # เพิ่มข้อมูลจากฐานข้อมูลลงใน Listbox
    for row in data:
        listbox.insert(tk.END, f"id: {row[0]}\n, coffee: {row[1]}\n, shot: {row[2]}, type: {row[3]}\n, size:{row[4]}\n, price:{row[5]}\n")

    # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล
    conn.commit()

    # ปิดการเชื่อมต่อฐานข้อมูล
    conn.close()

    addoder = Button(mainWindows,width=12,height=3,text="สั่งเพิ่ม",command=choostcoffee,bg="#DCAD67",font="Fc 12 bold",fg='black')
    addoder.place(relx=0.2,rely=0.845)

    editorder = Button(mainWindows,width=12,height=3,text="แก้ไขเมนู",command=editmenu,bg="#DCAD67",font="Fc 12 bold",fg='black')
    editorder.place(relx=0.43,rely=0.845)

    confrimorder = Button(mainWindows,width=12,height=3,text="ยืนยัน",command=lambda:(pdf(),qr()),bg="#DCAD67",font="Fc 12 bold",fg='black')
    confrimorder.place(relx=0.67,rely=0.845)

    backsizecoffee = Image.open(r"C:\Users\ASUS\Desktop\project python\backbutton.png")
    backsizecoffee = backsizecoffee.resize((55, int(55 * backsizecoffee.height / backsizecoffee.width)))
    back4 = ImageTk.PhotoImage(backsizecoffee)
    backlogin = Button(mainWindows, width=45, height=35, image=back4, command=sizecoffee, bg="#FFEFD5")
    backlogin.image = back4
    backlogin.place(relx=0.02, rely=0.03)
    
    mainWindows.mainloop()

def chooesmenu():
   
    logincoffee()

def home():
    global mainWindows
    if mainWindows:
        mainWindows.destroy()
    mainWindows = tk.Tk()
    mainWindows.resizable(FALSE, FALSE)
    mainWindows.title("Doglib slowbar cafe ☕")
    mainWindows.geometry("650x700+500+50")
    databest_canvas1 = tk.Canvas(mainWindows, width=1250, height=700, bg="#FFEFD5")
    databest_canvas1.place(relx=0, rely=0)

    doglib_image = Image.open("BG1.png")  # ใช้ชื่อไฟล์ภาพโดยตรง (ไม่ต้องระบุ path ถ้าอยู่ในโฟลเดอร์เดียวกับโค้ด)
    doglib_image = doglib_image.resize((700, 700))
    doglib_photo = ImageTk.PhotoImage(doglib_image)
    background_label = tk.Label(mainWindows, image=doglib_photo)
    background_label.photo = doglib_photo
    background_label.place(relx=0, rely=0)

    choosecoffee = Button(mainWindows, width=15, height=5, text="เลือกเมนูกาแฟ", command=logincoffee, bg="#FADCA5", font="Fc 12 bold", fg='black')
    choosecoffee.place(relx=0.4, rely=0.21)
    datebest = Button(mainWindows, width=15, height=5, text="เปิดข้อมูล", command=showfun, bg="#FADCA5", font="Fc 12 bold", fg='black')
    datebest.place(relx=0.4, rely=0.41)
    editdatabestbest = Button(mainWindows, width=15, height=5, text="แก้ไขข้อมูล", command=updatefun, bg="#FADCA5", font="Fc 12 bold", fg='black')
    editdatabestbest.place(relx=0.4, rely=0.61)
    editdatabestbest = Button(mainWindows, width=15, height=5, text="ปิดโปรแกรม", command=closemenu, bg="#FADCA5", font="Fc 12 bold", fg='black')
    editdatabestbest.place(relx=0.4, rely=0.81)

    mainWindows.mainloop()

delete()

home()
