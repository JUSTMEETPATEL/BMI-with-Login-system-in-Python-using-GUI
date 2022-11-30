from tkinter import * #type:ignore
from tkinter import messagebox
import mysql.connector as c
import random
import smtplib
from email.message import EmailMessage
import tkinter as tk 
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk

#FUNCTIONS
def home_screen():
    def send_email(subject,body,to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
        user = "valetudommv@gmail.com"
        password = "eyckveuubhpeyhgu"
        msg['from'] = user



        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user,password)
        server.send_message(msg)

        server.quit()

    #STARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTSIGNIN

    def signup_cc():
        new=Toplevel(root)
        def sign():
            new.destroy()

        def on_enter(e):
            user.delete(0,'end')

        def on_leave(e):
            name=user.get()
            if name =='':
                user.insert(0,'Username')

        def onenter(e):
            code.delete(0,'end')

        def onleave(e):
            name=code.get()
            if name =='':
                code.insert(0,'Password')

        def on__enter(e):
            gmail.delete(0,'end')

        def on__leave(e):
            name=gmail.get()
            if name =='':
                gmail.insert(0,'Email')

        def signup():
            username = user.get()
            password = code.get()
            mail = gmail.get()
            a = c.connect(host = "localhost", user = "root",passwd = "admin123",database = "12project")
            mycursor = a.cursor()
            query = "insert into login(Username ,Password,gmail) values(%s,%s,%s)"
            val = (username,password,mail)
            mycursor.execute(query,val)
            a.commit()
            messagebox.showinfo("Signup","Your account has been created successfully")
            new.destroy()




        new.title('Signin')
        new.geometry('450x644')

        new.configure(bg='#fff')
        new.resizable(False,False)



        frame = Frame(new,width= 450,height =450,bg="white")
        frame.place(x=50,y=50)

        heading=Label(frame,text='Signup',fg = "red",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x= 100,y=5)



        user=Entry(frame,width=25,fg='black',border =0,bg='white',font=('Microsoft YaHei UI Light',11))
        user.place(x=30,y=80)
        user.insert(0,'Username')
        user.bind('<FocusIn>', on_enter )
        user.bind('<FocusOut>', on_leave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

        code=Entry(frame,width=25,fg='black',border =0,bg='white',font=('Microsoft YaHei UI Light',11))
        code.place(x=30,y=150)
        code.insert(0,'Password')
        code.bind('<FocusIn>', onenter )
        code.bind('<FocusOut>', onleave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

        gmail=Entry(frame,width=25,fg='black',border =0,bg='white',font=('Microsoft YaHei UI Light',11))
        gmail.place(x=30,y=220)
        gmail.insert(0,'Email')
        gmail.bind('<FocusIn>', on__enter )
        gmail.bind('<FocusOut>', on__leave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

        Button(frame,width=39,pady=7,text='Sign up',command=signup,bg='red',fg='white',border=0).place(x=35,y=274)
        label=Label(frame,text="Already have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        label.place(x=75,y=344)

        signin=Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='red',command = sign)
        signin.place(x=215,y=344) 

        new.mainloop() 

    #STOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPSIGNIN

    def on_enter(e):
        user.delete(0,'end')  # type: ignore

    def on_leave(e):
        name=user.get()  # type: ignore
        if name =='':
            user.insert(0,'Username')

    def onenter(e):
        code.delete(0,'end')

    def onleave(e):
        name=code.get()
        if name =='':
            code.insert(0,'Password')

    def signin():
        username = user.get()  # type: ignore
        password = code.get()

        a = c.connect(host = "localhost", user = "root",passwd = "admin123",database = "12project")
        mycursor = a.cursor()
        query = "select * from login where Username = %s and Password = %s"
        mycursor.execute(query,[(username),(password)])
        result = mycursor.fetchall()



        if result:

            bmi_wd=Toplevel(root)  
            bmi_wd.geometry("470x580+300+200")
            bmi_wd.resizable(False,False)
            bmi_wd.configure(bg="#f0f1f5")
            bmi_wd.title("BMI Calculator")
            def redirect():
                if bmi < 18.5:
                    underweight = Toplevel(bmi_wd)
                    underweight.title('UNDERWEIGHT')
                    underweight.config(bg = '#243E24')

                    underweight.geometry('465x644')
                    underweight.resizable(False, False)

                    def yoga():
                        yog = Tk()
                        yog.title('Yoga Underweight')
                        yog.geometry('465x644')
                        yog.config(bg = '#243E24')
                        yog.resizable(False, False)

                        def callback(url):
                            webbrowser.open_new_tab(url)

                        def eam():
                            messagebox.showinfo('Early Morning', 'Milk + dry fruits')
                        def brf():
                            messagebox.showinfo('Breakfast', 'Salad with fruits and vegetables + curd \n Or \n Oatmeal with fruit and flaxseeds \n Or \n Greek yogurt with chia seeds and berries')
                        def mdm():
                            messagebox.showinfo('Mid Morning', 'Lots of water and fruit if required ')
                        def lch():
                            messagebox.showinfo('Lunch', 'Marinated tofu pita pocket with Greek salad \n Or \n Red lentil veggie burger with avocado salad')
                        def evs():
                            messagebox.showinfo('Evening Snack','Dry fruits and milk')
                        def din():
                            messagebox.showinfo('Dinner', 'Chickpea curry with basmati rice \n Or \n Black bean tacos with cauliflower rice')

                        l = Label(yog, text = ' ', bg = '#243E24', width = 23)
                        l.grid(column = 0, row = 0, pady = 10)

                        lx = Label(yog, text = 'Let\'s get you fit', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                        lx.grid(column = 1, row = 0, pady = 5)

                        l1 = Label(yog, text = 'DIET PLAN', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24', width = 11)
                        l1.grid(column = 1, row = 1, pady = 10)

                        btn1 = Button(yog, text = 'Early Morning', bg='#ECBD00', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn1.grid(column = 1, row = 2, padx = 2)
                        btn2 = Button(yog, text = 'Breakfast', bg='#ECBD00', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn2.grid(column = 1, row = 3, padx = 2)
                        btn3 = Button(yog, text = 'Mid Morning', bg='#ECBD00', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn3.grid(column = 1, row = 4, padx = 2)
                        btn4 = Button(yog, text = 'Lunch', bg='#ECBD00', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn4.grid(column = 1, row = 5, padx = 2)
                        btn5 = Button(yog, text = 'Evening Snack', bg='#ECBD00', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn5.grid(column = 1, row = 6, padx = 2)
                        btn6 = Button(yog, text = 'Dinner', bg='#ECBD00', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn6.grid(column = 1, row = 7, padx = 2)


                        l3 = Label(yog, text = 'YOGA POSES', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24')
                        l3.grid(column = 1, row = 9, pady = 30)
                        link1 = Label(yog, text="Reference",font=('rockwell', 14), fg='#663A82', cursor="hand2", bg = '#243E24')
                        link1.grid(column = 1, row = 10, padx = 5)
                        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=BFHsX5mWff8"))

                        def des():
                            yog.destroy()

                        yogbtn = Button(yog, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                        yogbtn.grid(column = 2, row = 11, pady=5)

                        yog.mainloop()


                    def fit():
                        muscle = Tk()
                        muscle.title('Muscle Underweight')
                        muscle.config(bg = '#243E24')
                        muscle.geometry('465x644')
                        muscle.resizable(False, False)

                        def des():
                            muscle.destroy()

                        def callback(url):
                            webbrowser.open_new_tab(url)

                        def eam():
                            messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                        def brf():
                            messagebox.showinfo('Breakfast', 'A bowl of oats/wheat flakes/ quinoa with skimmed milk and some nuts \n OR \n Whole wheat toast with peanut butter + milk')
                        def mdm():
                            messagebox.showinfo('Mid Morning', 'Buttermilk made from low-fat yogurt \n OR \n 1 big bowl of watermelon/pineapple/grapefruit + 2 cheese slices')
                        def lch():
                            messagebox.showinfo('Lunch', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')
                        def evs():
                            messagebox.showinfo('Evening Snack', 'Sprouts or boiled legumes (chickpea/ black chana) with onion, tomato, cucumber, and lime juice + whey with water + eggs/cottage cheese/ low fat cheese slice \n Or \n Paneer and spinach roll/ 2 slices of brown bread + fresh juice')
                        def din():
                            messagebox.showinfo('Dinner', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')

                        lx = Label(muscle, text = 'Let\'s get you fit!!', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                        lx.grid(column = 1, row = 0, pady = 5)

                        l1 = Label(muscle, text = 'DIET PLAN', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24', width = 11)
                        l1.grid(column = 1, row = 1, pady = 10)

                        l2 = Label(muscle, text = 'VEG', font = ('hattenschweiler', 16), fg = '#4C9A2A', bg = '#243E24', width = 13)
                        l2.grid(column = 0, row = 2, pady = 5)

                        l3 = Label(muscle, text = 'NON-VEG', font = ('hattenschweiler', 16), fg = 'red', bg = '#243E24', width = 13)
                        l3.grid(column = 2, row = 2, pady = 5)

                        btn1 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn1.grid(column = 0, row = 3, padx = 2)
                        btn2 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn2.grid(column = 0, row = 4, padx = 2)
                        btn3 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn3.grid(column = 0, row = 5, padx = 2)
                        btn4 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn4.grid(column = 0, row = 6, padx = 2)
                        btn5 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn5.grid(column = 0, row = 7, padx = 2)
                        btn6 = Button(muscle, text = 'Dinner', bg='#CC9900', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn6.grid(column = 0, row = 8, padx = 2)


                        def eamn():
                            messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                        def brfn():
                            messagebox.showinfo('Breakfast', '3 to 4 slices of whole wheat bread toast with peanut butter + 3 egg whites + 1 full egg omelette \n OR \n 1 cup of low fat milk + 1 scoop of whey protein+ 150 gms of oatmeal + 1 banana+ a few almonds+ walnuts')
                        def mdmn():
                            messagebox.showinfo('Mid Morning', '1 orange or apple or 1 cup of green tea + 2 to 3 multigrain biscuits')
                        def lchn():
                            messagebox.showinfo('Lunch', '150 gms of brown rice or whole wheat chapattis + 150 gms of skinless chicken breast / fish + 1 bowl of mixed vegetables+ green chutney+ salad')
                        def evsn():
                            messagebox.showinfo('Evening Snack', '1 fruit or green tea or sprouts salad + few nuts')
                        def dinn():
                            messagebox.showinfo('Dinner', '1 small fish or 100 gms of skinless/ lean chicken + stir fried veggies with baked potato + 1 cup of brown rice/ whole wheat chappati')

                        btn7 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eamn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn7.grid(column = 2, row = 3, padx = 2)
                        btn8 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brfn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn8.grid(column = 2, row = 4, padx = 2)
                        btn9 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdmn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn9.grid(column = 2, row = 5, padx = 2)
                        btn10 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lchn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn10.grid(column = 2, row = 6, padx = 2)
                        btn11 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evsn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn11.grid(column = 2, row = 7, padx = 2)
                        btn12 = Button(muscle, text = 'Dinner', bg='#CC9900', command = dinn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn12.grid(column = 2, row = 8, padx = 2)



                        l3 = Label(muscle, text = 'VIDEOS', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24')
                        l3.grid(column = 1, row = 9, pady = 30)
                        link1 = Label(muscle, text="Leg Day",font=('rockwell', 14), fg='#CC8899', cursor="hand2", bg = '#243E24')
                        link1.grid(column = 1, row = 10, padx = 5)
                        link1.bind("<Button-1>", lambda e: callback(" https://www.youtube.com/watch?v=8HkhW_N1jFg"))
                        link2 = Label(muscle, text="Arm Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                        link2.grid(column = 1, row = 11, padx = 5)
                        link2.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=eytWFViVIvE"))
                        link3 = Label(muscle, text="Back Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                        link3.grid(column = 1, row = 12, padx = 5)
                        link3.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=pDns20FDhhw"))    

                        fitbtn = Button(muscle, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), activebackground = 'grey', width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                        fitbtn.grid(column = 2, row = 13, pady=5)

                        muscle.mainloop()


                    l1 = Label(underweight,text = 'Your BMI is...., you are underweight', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('impact', 20 ))
                    l1.pack(pady = 10)
                    l2 = Label(underweight,text = 'What\'s your goal?', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 16 ))
                    l2.pack(pady = 25)

                    image = Image.open('yog21.png')  # type: ignore
                    resim = image.resize((180, 180), Image.ANTIALIAS) # type: ignore
                    yog = ImageTk.PhotoImage(resim)
                    yogbtn = Button(underweight, image = yog, command = yoga, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                    yogbtn.pack()
                    l3 = Label(underweight,text = 'YOGA', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14 ))
                    l3.pack()

                    image = Image.open('bm2.png') # type: ignore
                    resim = image.resize((180, 180), Image.ANTIALIAS) # type: ignore
                    mus= ImageTk.PhotoImage(resim)
                    musbtn = Button(underweight, image = mus, command = fit, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                    musbtn.pack()
                    l1 = Label(underweight,text = 'BUILD MUSCLE', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14 ))
                    l1.pack()

                    underweight.mainloop()
                elif (bmi > 18.5) and (bmi < 24.9):
                    normal = Toplevel(bmi_wd)
                    normal.title('normal')
                    normal.config(bg = '#243E24')

                    normal.geometry('465x644')
                    normal.resizable(False, False)

                    def yoga():
                        yog = Tk()
                        yog.title('Yoga normal')
                        yog.geometry('465x644')
                        yog.config(bg = '#243E24')
                        yog.resizable(False, False)

                        def callback(url):
                            webbrowser.open_new_tab(url)

                        def eam():
                            messagebox.showinfo('Early Morning', 'Milk + dry fruits')
                        def brf():
                            messagebox.showinfo('Breakfast', 'Salad with fruits and vegetables + curd \n Or \n Oatmeal with fruit and flaxseeds \n Or \n Greek yogurt with chia seeds and berries')
                        def mdm():
                            messagebox.showinfo('Mid Morning', 'Lots of water and fruit if required ')
                        def lch():
                            messagebox.showinfo('Lunch', 'Marinated tofu pita pocket with Greek salad \n Or \n Red lentil veggie burger with avocado salad')
                        def evs():
                            messagebox.showinfo('Evening Snack','Dry fruits and milk')
                        def din():
                            messagebox.showinfo('Dinner', 'Chickpea curry with basmati rice \n Or \n Black bean tacos with cauliflower rice')

                        l = Label(yog, text = ' ', bg = '#243E24', width = 23)
                        l.grid(column = 0, row = 0, pady = 10)

                        lx = Label(yog, text = 'Let\'s get you fitter', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                        lx.grid(column = 1, row = 0, pady = 5)

                        l1 = Label(yog, text = 'DIET PLAN', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24', width = 11)
                        l1.grid(column = 1, row = 1, pady = 10)

                        btn1 = Button(yog, text = 'Early Morning', bg='#ECBD00', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn1.grid(column = 1, row = 2, padx = 2)
                        btn2 = Button(yog, text = 'Breakfast', bg='#ECBD00', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn2.grid(column = 1, row = 3, padx = 2)
                        btn3 = Button(yog, text = 'Mid Morning', bg='#ECBD00', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn3.grid(column = 1, row = 4, padx = 2)
                        btn4 = Button(yog, text = 'Lunch', bg='#ECBD00', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn4.grid(column = 1, row = 5, padx = 2)
                        btn5 = Button(yog, text = 'Evening Snack', bg='#ECBD00', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn5.grid(column = 1, row = 6, padx = 2)
                        btn6 = Button(yog, text = 'Dinner', bg='#ECBD00', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn6.grid(column = 1, row = 7, padx = 2)


                        l3 = Label(yog, text = 'YOGA POSES', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24')
                        l3.grid(column = 1, row = 9, pady = 30)
                        link1 = Label(yog, text="Reference",font=('rockwell', 14), fg='#663A82', cursor="hand2", bg = '#243E24')
                        link1.grid(column = 1, row = 10, padx = 5)
                        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=4A0-aTZpR8M"))

                        def des():
                            yog.destroy()

                        yogbtn = Button(yog, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                        yogbtn.grid(column = 2, row = 11, pady=5)

                        yog.mainloop()


                    def fit():
                        muscle = Tk()
                        muscle.title('Muscle normal')
                        muscle.config(bg = '#243E24')
                        muscle.geometry('465x644')
                        muscle.resizable(False, False)

                        def des():
                            muscle.destroy()

                        def callback(url):
                            webbrowser.open_new_tab(url)

                        def eam():
                            messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                        def brf():
                            messagebox.showinfo('Breakfast', 'A bowl of oats/wheat flakes/ quinoa with skimmed milk and some nuts \n OR \n Whole wheat toast with peanut butter + milk')
                        def mdm():
                            messagebox.showinfo('Mid Morning', 'Buttermilk made from low-fat yogurt \n OR \n 1 big bowl of watermelon/pineapple/grapefruit + 2 cheese slices')
                        def lch():
                            messagebox.showinfo('Lunch', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')
                        def evs():
                            messagebox.showinfo('Evening Snack', 'Sprouts or boiled legumes (chickpea/ black chana) with onion, tomato, cucumber, and lime juice + whey with water + eggs/cottage cheese/ low fat cheese slice \n Or \n Paneer and spinach roll/ 2 slices of brown bread + fresh juice')
                        def din():
                            messagebox.showinfo('Dinner', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')

                        lx = Label(muscle, text = 'Let\'s get you fitter!!', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                        lx.grid(column = 1, row = 0, pady = 5)

                        l1 = Label(muscle, text = 'DIET PLAN', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24', width = 11)
                        l1.grid(column = 1, row = 1, pady = 10)

                        l2 = Label(muscle, text = 'VEG', font = ('hattenschweiler', 16), fg = '#4C9A2A', bg = '#243E24', width = 13)
                        l2.grid(column = 0, row = 2, pady = 5)

                        l3 = Label(muscle, text = 'NON-VEG', font = ('hattenschweiler', 16), fg = 'red', bg = '#243E24', width = 13)
                        l3.grid(column = 2, row = 2, pady = 5)

                        btn1 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn1.grid(column = 0, row = 3, padx = 2)
                        btn2 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn2.grid(column = 0, row = 4, padx = 2)
                        btn3 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn3.grid(column = 0, row = 5, padx = 2)
                        btn4 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn4.grid(column = 0, row = 6, padx = 2)
                        btn5 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn5.grid(column = 0, row = 7, padx = 2)
                        btn6 = Button(muscle, text = 'Dinner', bg='#CC9900', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn6.grid(column = 0, row = 8, padx = 2)


                        def eamn():
                            messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                        def brfn():
                            messagebox.showinfo('Breakfast', '3 to 4 slices of whole wheat bread toast with peanut butter + 3 egg whites + 1 full egg omelette \n OR \n 1 cup of low fat milk + 1 scoop of whey protein+ 150 gms of oatmeal + 1 banana+ a few almonds+ walnuts')
                        def mdmn():
                            messagebox.showinfo('Mid Morning', '1 orange or apple or 1 cup of green tea + 2 to 3 multigrain biscuits')
                        def lchn():
                            messagebox.showinfo('Lunch', '150 gms of brown rice or whole wheat chapattis + 150 gms of skinless chicken breast / fish + 1 bowl of mixed vegetables+ green chutney+ salad')
                        def evsn():
                            messagebox.showinfo('Evening Snack', '1 fruit or green tea or sprouts salad + few nuts')
                        def dinn():
                            messagebox.showinfo('Dinner', '1 small fish or 100 gms of skinless/ lean chicken + stir fried veggies with baked potato + 1 cup of brown rice/ whole wheat chappati')

                        btn7 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eamn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn7.grid(column = 2, row = 3, padx = 2)
                        btn8 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brfn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn8.grid(column = 2, row = 4, padx = 2)
                        btn9 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdmn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn9.grid(column = 2, row = 5, padx = 2)
                        btn10 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lchn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn10.grid(column = 2, row = 6, padx = 2)
                        btn11 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evsn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn11.grid(column = 2, row = 7, padx = 2)
                        btn12 = Button(muscle, text = 'Dinner', bg='#CC9900', command = dinn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn12.grid(column = 2, row = 8, padx = 2)



                        l3 = Label(muscle, text = 'VIDEOS', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24')
                        l3.grid(column = 1, row = 9, pady = 30)
                        link1 = Label(muscle, text="Arm Day",font=('rockwell', 14), fg='#CC8899', cursor="hand2", bg = '#243E24')
                        link1.grid(column = 1, row = 10, padx = 5)
                        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=eytWFViVIvE"))
                        link2 = Label(muscle, text="Leg Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                        link2.grid(column = 1, row = 11, padx = 5)
                        link2.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=8HkhW_N1jFg"))
                        link3 = Label(muscle, text="Back Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                        link3.grid(column = 1, row = 12, padx = 5)
                        link3.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=pDns20FDhhw"))    

                        fitbtn = Button(muscle, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), activebackground = 'grey', width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                        fitbtn.grid(column = 2, row = 13, pady=5)

                        muscle.mainloop()


                    l1 = Label(normal,text = 'Your BMI is...., you are normal', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('impact', 20 ))
                    l1.pack(pady = 10)
                    l2 = Label(normal,text = 'What\'s your goal?', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 16 ))
                    l2.pack(pady = 25)

                    image = Image.open('yog21.png')  # type: ignore
                    resim = image.resize((180, 180), Image.ANTIALIAS)  # type: ignore
                    yog = ImageTk.PhotoImage(resim)
                    yogbtn = Button(normal, image = yog, command = yoga, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                    yogbtn.pack()
                    l3 = Label(normal,text = 'YOGA', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14 ))
                    l3.pack()

                    image = Image.open('bm1.png')  # type: ignore
                    resim = image.resize((180, 180), Image.ANTIALIAS)  # type: ignore
                    mus= ImageTk.PhotoImage(resim)
                    musbtn = Button(normal, image = mus, command = fit, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                    musbtn.pack()
                    l1 = Label(normal,text = 'BUILD MUSCLE', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14 ))
                    l1.pack()

                    normal.mainloop()
                elif (bmi > 24.9) and (bmi < 29.9):
                    overweight = Toplevel(bmi_wd)
                    overweight.title('overweight')
                    overweight.config(bg = '#243E24')

                    overweight.geometry('465x644')
                    overweight.resizable(False, False)

                    def yoga():
                        yog = Tk()
                        yog.title('Yoga overweight')
                        yog.geometry('465x644')
                        yog.config(bg = '#243E24')
                        yog.resizable(False, False)

                        def callback(url):
                            webbrowser.open_new_tab(url)

                        def eam():
                            messagebox.showinfo('Early Morning', 'Milk + dry fruits')
                        def brf():
                            messagebox.showinfo('Breakfast', 'Salad with fruits and vegetables + curd \n Or \n Oatmeal with fruit and flaxseeds \n Or \n Greek yogurt with chia seeds and berries')
                        def mdm():
                            messagebox.showinfo('Mid Morning', 'Lots of water and fruit if required ')
                        def lch():
                            messagebox.showinfo('Lunch', 'Marinated tofu pita pocket with Greek salad \n Or \n Red lentil veggie burger with avocado salad')
                        def evs():
                            messagebox.showinfo('Evening Snack','Dry fruits and milk')
                        def din():
                            messagebox.showinfo('Dinner', 'Chickpea curry with basmati rice \n Or \n Black bean tacos with cauliflower rice')

                        l = Label(yog, text = ' ', bg = '#243E24', width = 23)
                        l.grid(column = 0, row = 0, pady = 10)

                        lx = Label(yog, text = 'Let\'s get you fit', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                        lx.grid(column = 1, row = 0, pady = 5)

                        l1 = Label(yog, text = 'DIET PLAN', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24', width = 11)
                        l1.grid(column = 1, row = 1, pady = 10)

                        btn1 = Button(yog, text = 'Early Morning', bg='#ECBD00', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn1.grid(column = 1, row = 2, padx = 2)
                        btn2 = Button(yog, text = 'Breakfast', bg='#ECBD00', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn2.grid(column = 1, row = 3, padx = 2)
                        btn3 = Button(yog, text = 'Mid Morning', bg='#ECBD00', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn3.grid(column = 1, row = 4, padx = 2)
                        btn4 = Button(yog, text = 'Lunch', bg='#ECBD00', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn4.grid(column = 1, row = 5, padx = 2)
                        btn5 = Button(yog, text = 'Evening Snack', bg='#ECBD00', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn5.grid(column = 1, row = 6, padx = 2)
                        btn6 = Button(yog, text = 'Dinner', bg='#ECBD00', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn6.grid(column = 1, row = 7, padx = 2)


                        l3 = Label(yog, text = 'YOGA POSES', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24')
                        l3.grid(column = 1, row = 9, pady = 30)
                        link1 = Label(yog, text="Reference",font=('rockwell', 14), fg='#663A82', cursor="hand2", bg = '#243E24')
                        link1.grid(column = 1, row = 10, padx = 5)
                        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=i2zvV8-qsvU"))

                        def des():
                            yog.destroy()

                        yogbtn = Button(yog, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                        yogbtn.grid(column = 2, row = 11, pady=5)

                        yog.mainloop()

                    def weightloss():
                        lefa = Tk()
                        lefa.title('Weight Loss')
                        lefa.geometry('465x644')
                        lefa.resizable(False, False)
                        lefa.config(bg = '#243E24')     

                        def callback(url):
                            webbrowser.open_new_tab(url)

                        def eam():
                            messagebox.showinfo('Early Morning', 'Warm water (1 glass), Almonds(25 gm)')
                        def brf():
                            messagebox.showinfo('Breakfast', 'Oats porridge in skimmed milk')
                        def mdm():
                            messagebox.showinfo('Mid Morning', 'Fruits of any kind except mango and banana')
                        def lch():
                            messagebox.showinfo('Lunch', 'Salad including vegetables , fruits ,(paneer /chole/dal),spices \n Or \n 2 roti ,1 sabzi')
                        def evs():
                            messagebox.showinfo('Evening Snack', 'Fruit and milk/coffee(containg honey rather than sugar )')
                        def din():
                            messagebox.showinfo('Dinner', 'Sabzi , 2 chapatis , daal, steamed rice \n Or \n khichdi')

                        lx = Label(lefa, text = 'Let\'s get you fit!!', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                        lx.grid(column = 1, row = 0, pady = 5)

                        l1 = Label(lefa, text = 'DIET PLAN', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24', width = 11)
                        l1.grid(column = 1, row = 1, pady = 10)

                        l2 = Label(lefa, text = 'VEG', font = ('hattenschweiler', 16), fg = '#4C9A2A', bg = '#243E24', width = 13)
                        l2.grid(column = 0, row = 2)

                        l3 = Label(lefa, text = 'NON-VEG', font = ('hattenschweiler', 16), fg = 'red', bg = '#243E24', width = 13)
                        l3.grid(column = 2, row = 2)

                        btn1 = Button(lefa, text = 'Early Morning', bg='#CC9900', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn1.grid(column = 0, row = 3, padx = 2)
                        btn2 = Button(lefa, text = 'Breakfast', bg='#CC9900', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn2.grid(column = 0, row = 4, padx = 2)
                        btn3 = Button(lefa, text = 'Mid Morning', bg='#CC9900', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn3.grid(column = 0, row = 5, padx = 2)
                        btn4 = Button(lefa, text = 'Lunch', bg='#CC9900', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn4.grid(column = 0, row = 6, padx = 2)
                        btn5 = Button(lefa, text = 'Evening Snack', bg='#CC9900', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn5.grid(column = 0, row = 7, padx = 2)
                        btn6 = Button(lefa, text = 'Dinner', bg='#CC9900', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn6.grid(column = 0, row = 8, padx = 2)


                        def eamn():
                            messagebox.showinfo('Early Morning', 'Warm water (1 glass), Almonds(25 gm )')
                        def brfn():
                            messagebox.showinfo('Breakfast', 'Oats porridge in skimmed milk')
                        def mdmn():
                            messagebox.showinfo('Mid Morning', 'Fruits of any kind except mango and banana')
                        def lchn():
                            messagebox.showinfo('Lunch', '1 cup rice , chicken curry fresh salad \n Or \n 2 roti , 1 sabzi, 1 cup raw salad, 1 piece chicken or fish')
                        def evsn():
                            messagebox.showinfo('Evening Snack', 'Fruit and milk/coffee(containg honey rather than sugar )')
                        def dinn():
                            messagebox.showinfo('Dinner', '1 cup daal/egg curry, 1 cup raw salad \n Or \n khichdi')

                        btn7 = Button(lefa, text = 'Early Morning', bg='#CC9900', command = eamn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn7.grid(column = 2, row = 3, padx = 2)
                        btn8 = Button(lefa, text = 'Breakfast', bg='#CC9900', command = brfn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn8.grid(column = 2, row = 4, padx = 2)
                        btn9 = Button(lefa, text = 'Mid Morning', bg='#CC9900', command = mdmn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn9.grid(column = 2, row = 5, padx = 2)
                        btn10 = Button(lefa, text = 'Lunch', bg='#CC9900', command = lchn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn10.grid(column = 2, row = 6, padx = 2)
                        btn11 = Button(lefa, text = 'Evening Snack', bg='#CC9900', command = evsn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn11.grid(column = 2, row = 7, padx = 2)
                        btn12 = Button(lefa, text = 'Dinner', bg='#CC9900', command = dinn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn12.grid(column = 2, row = 8, padx = 2)



                        l3 = Label(lefa, text = 'VIDEO LINKS', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24')
                        l3.grid(column = 1, row = 9, pady = 30)
                        link1 = Label(lefa, text="Pro Advice",font=('rockwell', 14), fg='#CC8899', cursor="hand2", bg = '#243E24')
                        link1.grid(column = 1, row = 10, padx = 5)
                        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=G3J0XwUlEBo"))
                        link2 = Label(lefa, text="Exercises",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                        link2.grid(column = 1, row = 11, padx = 5)
                        link2.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=b7YoGQuXYRE"))
                        link3 = Label(lefa, text="Aerobics",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                        link3.grid(column = 1, row = 12, padx = 5)
                        link3.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=oR6jkKsORUI"))

                        def des():
                            lefa.destroy()

                        fitbtn = Button(lefa, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                        fitbtn.grid(column = 2, row = 13, pady=5)

                        lefa.mainloop()

                    def fit():
                        muscle = Tk()
                        muscle.title('Muscle overweight')
                        muscle.config(bg = '#243E24')
                        muscle.geometry('465x644')
                        muscle.resizable(False, False)

                        def callback(url):
                               webbrowser.open_new_tab(url)

                        def eam():
                            messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                        def brf():
                            messagebox.showinfo('Breakfast', 'A bowl of oats/wheat flakes/ quinoa with skimmed milk and some nuts \n OR \n Whole wheat toast with peanut butter + milk')
                        def mdm():
                            messagebox.showinfo('Mid Morning', 'Buttermilk made from low-fat yogurt \n OR \n 1 big bowl of watermelon/pineapple/grapefruit + 2 cheese slices')
                        def lch():
                            messagebox.showinfo('Lunch', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')
                        def evs():
                            messagebox.showinfo('Evening Snack', 'Sprouts or boiled legumes (chickpea/ black chana) with onion, tomato, cucumber, and lime juice + whey with water + eggs/cottage cheese/ low fat cheese slice \n Or \n Paneer and spinach roll/ 2 slices of brown bread + fresh juice')
                        def din():
                            messagebox.showinfo('Dinner', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')

                        lx = Label(muscle, text = 'Let\'s get you fit!!', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                        lx.grid(column = 1, row = 0, pady = 5)

                        l1 = Label(muscle, text = 'DIET PLAN', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24', width = 11)
                        l1.grid(column = 1, row = 1, pady = 10)

                        l2 = Label(muscle, text = 'VEG', font = ('hattenschweiler', 16), fg = '#4C9A2A', bg = '#243E24', width = 13)
                        l2.grid(column = 0, row = 2, pady = 5)

                        l3 = Label(muscle, text = 'NON-VEG', font = ('hattenschweiler', 16), fg = 'red', bg = '#243E24', width = 13)
                        l3.grid(column = 2, row = 2, pady = 5)

                        btn1 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn1.grid(column = 0, row = 3, padx = 2)
                        btn2 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn2.grid(column = 0, row = 4, padx = 2)
                        btn3 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn3.grid(column = 0, row = 5, padx = 2)
                        btn4 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn4.grid(column = 0, row = 6, padx = 2)
                        btn5 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn5.grid(column = 0, row = 7, padx = 2)
                        btn6 = Button(muscle, text = 'Dinner', bg='#CC9900', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn6.grid(column = 0, row = 8, padx = 2)


                        def eamn():
                            messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                        def brfn():
                            messagebox.showinfo('Breakfast', '3 to 4 slices of whole wheat bread toast with peanut butter + 3 egg whites + 1 full egg omelette \n OR \n 1 cup of low fat milk + 1 scoop of whey protein+ 150 gms of oatmeal + 1 banana+ a few almonds+ walnuts')
                        def mdmn():
                            messagebox.showinfo('Mid Morning', '1 orange or apple or 1 cup of green tea + 2 to 3 multigrain biscuits')
                        def lchn():
                            messagebox.showinfo('Lunch', '150 gms of brown rice or whole wheat chapattis + 150 gms of skinless chicken breast / fish + 1 bowl of mixed vegetables+ green chutney+ salad')
                        def evsn():
                            messagebox.showinfo('Evening Snack', '1 fruit or green tea or sprouts salad + few nuts')
                        def dinn():
                            messagebox.showinfo('Dinner', '1 small fish or 100 gms of skinless/ lean chicken + stir fried veggies with baked potato + 1 cup of brown rice/ whole wheat chappati')

                        btn7 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eamn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn7.grid(column = 2, row = 3, padx = 2)
                        btn8 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brfn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn8.grid(column = 2, row = 4, padx = 2)
                        btn9 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdmn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn9.grid(column = 2, row = 5, padx = 2)
                        btn10 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lchn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn10.grid(column = 2, row = 6, padx = 2)
                        btn11 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evsn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn11.grid(column = 2, row = 7, padx = 2)
                        btn12 = Button(muscle, text = 'Dinner', bg='#CC9900', command = dinn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                        btn12.grid(column = 2, row = 8, padx = 2)



                        l3 = Label(muscle, text = 'VIDEO LINKS', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24')
                        l3.grid(column = 1, row = 9, pady = 30)
                        link1 = Label(muscle, text="Arm Day",font=('rockwell', 14), fg='#CC8899', cursor="hand2", bg = '#243E24')
                        link1.grid(column = 1, row = 10, padx = 5)
                        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=eytWFViVIvE"))
                        link2 = Label(muscle, text="Leg Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                        link2.grid(column = 1, row = 11, padx = 5)
                        link2.bind("<Button-1>", lambda e: callback(" https://www.youtube.com/watch?v=8HkhW_N1jFg"))
                        link3 = Label(muscle, text="Back Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                        link3.grid(column = 1, row = 12, padx = 5)
                        link3.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=pDns20FDhhw"))

                        def des():
                            muscle.destroy()

                        fitbtn = Button(muscle, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), activebackground = 'grey', width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                        fitbtn.grid(column = 2, row = 13, pady=5)

                        muscle.mainloop()


                    l1 = Label(overweight,text = 'Your BMI is...., you are overweight', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('impact', 20 ))
                    l1.pack()
                    l2 = Label(overweight,text = 'What\'s your goal?', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 16 ))
                    l2.pack(pady = 25)

                    image = Image.open('yog21.png')  # type: ignore
                    resim = image.resize((125, 125), Image.ANTIALIAS)  # type: ignore
                    yog = ImageTk.PhotoImage(resim)
                    yogbtn = Button(overweight, image = yog, command = yoga, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                    yogbtn.pack()
                    l2 = Label(overweight,text = 'YOGA', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14))
                    l2.pack()

                    image = Image.open('lf1.png')  # type: ignore
                    resim = image.resize((125, 125), Image.ANTIALIAS)  # type: ignore
                    lf = ImageTk.PhotoImage(resim)
                    lfbtn = Button(overweight, image = lf, command = weightloss, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                    lfbtn.pack()
                    l2 = Label(overweight,text = 'WEIGHTLOSS', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14))
                    l2.pack()

                    image = Image.open('bm3.png')  # type: ignore
                    resim = image.resize((125, 125), Image.ANTIALIAS)   # type: ignore
                    mus= ImageTk.PhotoImage(resim)
                    musbtn = Button(overweight, image = mus, command = fit, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                    musbtn.pack()
                    l2 = Label(overweight,text = 'BUILD MUSCLE', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14))
                    l2.pack()

                    overweight.mainloop()
                else:
                   Label2.config(text="Obesity!")
                   Label3.config(text="Health may be at risk, if they do not \n lose weight !")
            def ds():
                bmi_wd.destroy()
            def BMI():
                h= float(Height.get())
                w=float(Weight.get())
                m=h/100
                global bmi 
                bmi = round(float(w/m**2))
                Label1.config(text=bmi)
                if bmi < 18.5:
                   Label2.config(text="Underweight!")
                   Label3.config(text="You have lower weight then normal body !")
                elif (bmi > 18.5) and (bmi < 24.9):
                    Label2.config(text="Normal!")
                    Label3.config(text="It indicates that you are healthy !")
                elif (bmi > 24.9) and (bmi < 29.9):
                    Label2.config(text="Overweight!")
                    Label3.config(text="it indicates that a person is \n slightly overweight ! \n  Adoctor may advice to lose some \n weight for health reasons !")
                else:
                   Label2.config(text="Obesity!")
                   Label3.config(text="Health may be at risk, if they do not \n lose weight !")
            #icon
            image_icon=PhotoImage(file="icon.png")
            bmi_wd.iconphoto(False,image_icon)
            #top
            top = PhotoImage(file="top.png")
            top_image=Label(bmi_wd,image=top,background="#f0f1f5")
            top_image.place(x=-10,y=-10)
            #bottom Box
            Label(bmi_wd,width=72,height=18,bg="lightblue").pack(side = BOTTOM)
            #two boxes
            box= PhotoImage(file="box.png")
            Label(bmi_wd,image=box).place(x=20,y=100)
            Label(bmi_wd,image=box).place(x=240,y=100)
            #scale 
            Scale=PhotoImage(file="scale.png")
            Label(bmi_wd,image=Scale,bg="Lightblue").place(x=20,y=310)
            ##################slider1##################################################
            current_value = tk.DoubleVar()
            def get_current_value():
                return '{: .2f}'.format(current_value.get())
            def slider_changed(event):
                Height.set(get_current_value())
                size = int(float(get_current_value()))
                img= (Image.open("man.png"))  # type: ignore
                resized_image = img.resize((50,10+size))
                photo2=ImageTk.PhotoImage(resized_image)
                secondimage.config(image=photo2)
                secondimage.place(x=70,y=550-size)
                secondimage.image=photo2  # type: ignore
            #Command o change background color of scale
            style = ttk.Style()
            style.configure("TScale",background="White")
            slider = ttk.Scale(bmi_wd,from_=0,to=220,orient="horizontal",style="TScale",
                                    command=slider_changed,variable=current_value)
            slider.place(x=80,y=250)
            ########################################################################
            ##################slider2##################################################
            current_value2 = tk.DoubleVar()
            def get_current_value2():
                return '{: .2f}'.format(current_value2.get()) 
            def slider_changed2(event):
                Weight.set(get_current_value2())
            #Command o change background color of scale
            style2= ttk.Style()
            style2.configure("TScale",background="White")
            slider2 = ttk.Scale(bmi_wd,from_=0,to=200,orient="horizontal",style="TScale",
                                    command=slider_changed2,variable=current_value2)
            slider2.place(x=300,y=250)
            #Entry box
            Height = StringVar()
            Weight = StringVar()
            height=Entry(bmi_wd,textvariable=Height,width=5,font="arial 50",bg="#fff",fg="#000",bd=0,justify = CENTER)
            height.place(x=35,y=160)
            Height.set(get_current_value())
            weight = Entry(bmi_wd,textvariable=Weight,width=5,font="arial 50",bg="#fff",fg="#000",bd=0,justify = CENTER)
            weight.place(x=255,y=160)
            Weight.set(get_current_value2())
            #MAN IMAGE
            secondimage=Label(bmi_wd,bg="lightblue")
            secondimage.place(x=70,y=530)
            Button(bmi_wd,text="View Report",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=280,y=340)
            Label1=Label(bmi_wd,font="Arial 60 bold",bg="lightblue",fg = "#fff")
            Label1.place(x=125,y=305)
            Label2=Label(bmi_wd,font="Arial 20 bold",bg="lightblue",fg = "#fff")
            Label2.place(x=280,y=430)
            Label3=Label(bmi_wd,font="Arial 10 bold",bg="lightblue",fg = "#fff")
            Label3.place(x=200,y=500)

            Button(bmi_wd,text="Get help",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=redirect).place(x=280,y=500)


            bmi_wd.mainloop()

            return True

        else:
            messagebox.showerror("Incorrect username or password")
            return False

        #BMIIIIIIII STOP   

    def signinwithootp():
        otpwd = Toplevel(root)
        otpwd.title('Login')
        otpwd.geometry('450x644')

        otpwd.configure(bg='#fff')
        otpwd.resizable(False,False)

        def send_email(subject,body,to):
            msg = EmailMessage()
            msg.set_content(body)
            msg['subject'] = subject
            msg['to'] = to
            user = "valetudommv@gmail.com"
            password = "eyckveuubhpeyhgu"
            msg['from'] = user



            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(user,password)
            server.send_message(msg)

            server.quit()

        def otpsender():
            user1 = mail.get()
            global otp 
            otp = random.randint(1000,9999) 
            Body = "Your verification code is  " + str(otp)
            send_email("OTP verification EmailMessage",Body,user1)



        def on_enter(e):
            mail.delete(0,'end')  # type: ignore

        def on_leave(e):
            name=mail.get()  # type: ignore
            if name =='':
                mail.insert(0,'Email Address')

        def onenter(e):
            otp2.delete(0,'end')

        def onleave(e):
            name=otp2.get()
            if name =='':
                otp2.insert(0,'OTP')


        def entry():
            email = mail.get()
            user_otp = otp2.get()

            a = c.connect(host = "localhost", user = "root",passwd = "admin123",database = "12project")
            mycursor = a.cursor()
            query = "select * from login where gmail = %s "
            mycursor.execute(query,[(email)])
            result = mycursor.fetchall()
            print(result)
            print(otp)


            if result[0][2] == email:# type: ignore 
                if str(otp)== user_otp:        
                    bmi_wd=Toplevel(root)  
                    bmi_wd.geometry("470x580+300+200")
                    bmi_wd.resizable(False,False)
                    bmi_wd.configure(bg="#f0f1f5")
                    bmi_wd.title("BMI Calculator")

                    def redirect():
                        if bmi < 18.5:
                            underweight = Toplevel(bmi_wd)
                            underweight.title('UNDERWEIGHT')
                            underweight.config(bg = '#243E24')

                            underweight.geometry('465x644')
                            underweight.resizable(False, False)

                            def yoga():
                                yog = Tk()
                                yog.title('Yoga Underweight')
                                yog.geometry('465x644')
                                yog.config(bg = '#243E24')
                                yog.resizable(False, False)

                                def callback(url):
                                    webbrowser.open_new_tab(url)

                                def eam():
                                    messagebox.showinfo('Early Morning', 'Milk + dry fruits')
                                def brf():
                                    messagebox.showinfo('Breakfast', 'Salad with fruits and vegetables + curd \n Or \n Oatmeal with fruit and flaxseeds \n Or \n Greek yogurt with chia seeds and berries')
                                def mdm():
                                    messagebox.showinfo('Mid Morning', 'Lots of water and fruit if required ')
                                def lch():
                                    messagebox.showinfo('Lunch', 'Marinated tofu pita pocket with Greek salad \n Or \n Red lentil veggie burger with avocado salad')
                                def evs():
                                    messagebox.showinfo('Evening Snack','Dry fruits and milk')
                                def din():
                                    messagebox.showinfo('Dinner', 'Chickpea curry with basmati rice \n Or \n Black bean tacos with cauliflower rice')

                                l = Label(yog, text = ' ', bg = '#243E24', width = 23)
                                l.grid(column = 0, row = 0, pady = 10)

                                lx = Label(yog, text = 'Let\'s get you fit', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                                lx.grid(column = 1, row = 0, pady = 5)

                                l1 = Label(yog, text = 'DIET PLAN', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24', width = 11)
                                l1.grid(column = 1, row = 1, pady = 10)

                                btn1 = Button(yog, text = 'Early Morning', bg='#ECBD00', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn1.grid(column = 1, row = 2, padx = 2)
                                btn2 = Button(yog, text = 'Breakfast', bg='#ECBD00', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn2.grid(column = 1, row = 3, padx = 2)
                                btn3 = Button(yog, text = 'Mid Morning', bg='#ECBD00', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn3.grid(column = 1, row = 4, padx = 2)
                                btn4 = Button(yog, text = 'Lunch', bg='#ECBD00', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn4.grid(column = 1, row = 5, padx = 2)
                                btn5 = Button(yog, text = 'Evening Snack', bg='#ECBD00', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn5.grid(column = 1, row = 6, padx = 2)
                                btn6 = Button(yog, text = 'Dinner', bg='#ECBD00', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn6.grid(column = 1, row = 7, padx = 2)


                                l3 = Label(yog, text = 'YOGA POSES', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24')
                                l3.grid(column = 1, row = 9, pady = 30)
                                link1 = Label(yog, text="Reference",font=('rockwell', 14), fg='#663A82', cursor="hand2", bg = '#243E24')
                                link1.grid(column = 1, row = 10, padx = 5)
                                link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=BFHsX5mWff8"))

                                def des():
                                    yog.destroy()

                                yogbtn = Button(yog, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                                yogbtn.grid(column = 2, row = 11, pady=5)

                                yog.mainloop()


                            def fit():
                                muscle = Tk()
                                muscle.title('Muscle Underweight')
                                muscle.config(bg = '#243E24')
                                muscle.geometry('465x644')
                                muscle.resizable(False, False)

                                def des():
                                    muscle.destroy()

                                def callback(url):
                                    webbrowser.open_new_tab(url)

                                def eam():
                                    messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                                def brf():
                                    messagebox.showinfo('Breakfast', 'A bowl of oats/wheat flakes/ quinoa with skimmed milk and some nuts \n OR \n Whole wheat toast with peanut butter + milk')
                                def mdm():
                                    messagebox.showinfo('Mid Morning', 'Buttermilk made from low-fat yogurt \n OR \n 1 big bowl of watermelon/pineapple/grapefruit + 2 cheese slices')
                                def lch():
                                    messagebox.showinfo('Lunch', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')
                                def evs():
                                    messagebox.showinfo('Evening Snack', 'Sprouts or boiled legumes (chickpea/ black chana) with onion, tomato, cucumber, and lime juice + whey with water + eggs/cottage cheese/ low fat cheese slice \n Or \n Paneer and spinach roll/ 2 slices of brown bread + fresh juice')
                                def din():
                                    messagebox.showinfo('Dinner', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')

                                lx = Label(muscle, text = 'Let\'s get you fit!!', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                                lx.grid(column = 1, row = 0, pady = 5)

                                l1 = Label(muscle, text = 'DIET PLAN', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24', width = 11)
                                l1.grid(column = 1, row = 1, pady = 10)

                                l2 = Label(muscle, text = 'VEG', font = ('hattenschweiler', 16), fg = '#4C9A2A', bg = '#243E24', width = 13)
                                l2.grid(column = 0, row = 2, pady = 5)

                                l3 = Label(muscle, text = 'NON-VEG', font = ('hattenschweiler', 16), fg = 'red', bg = '#243E24', width = 13)
                                l3.grid(column = 2, row = 2, pady = 5)

                                btn1 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn1.grid(column = 0, row = 3, padx = 2)
                                btn2 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn2.grid(column = 0, row = 4, padx = 2)
                                btn3 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn3.grid(column = 0, row = 5, padx = 2)
                                btn4 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn4.grid(column = 0, row = 6, padx = 2)
                                btn5 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn5.grid(column = 0, row = 7, padx = 2)
                                btn6 = Button(muscle, text = 'Dinner', bg='#CC9900', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn6.grid(column = 0, row = 8, padx = 2)


                                def eamn():
                                    messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                                def brfn():
                                    messagebox.showinfo('Breakfast', '3 to 4 slices of whole wheat bread toast with peanut butter + 3 egg whites + 1 full egg omelette \n OR \n 1 cup of low fat milk + 1 scoop of whey protein+ 150 gms of oatmeal + 1 banana+ a few almonds+ walnuts')
                                def mdmn():
                                    messagebox.showinfo('Mid Morning', '1 orange or apple or 1 cup of green tea + 2 to 3 multigrain biscuits')
                                def lchn():
                                    messagebox.showinfo('Lunch', '150 gms of brown rice or whole wheat chapattis + 150 gms of skinless chicken breast / fish + 1 bowl of mixed vegetables+ green chutney+ salad')
                                def evsn():
                                    messagebox.showinfo('Evening Snack', '1 fruit or green tea or sprouts salad + few nuts')
                                def dinn():
                                    messagebox.showinfo('Dinner', '1 small fish or 100 gms of skinless/ lean chicken + stir fried veggies with baked potato + 1 cup of brown rice/ whole wheat chappati')

                                btn7 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eamn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn7.grid(column = 2, row = 3, padx = 2)
                                btn8 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brfn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn8.grid(column = 2, row = 4, padx = 2)
                                btn9 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdmn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn9.grid(column = 2, row = 5, padx = 2)
                                btn10 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lchn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn10.grid(column = 2, row = 6, padx = 2)
                                btn11 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evsn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn11.grid(column = 2, row = 7, padx = 2)
                                btn12 = Button(muscle, text = 'Dinner', bg='#CC9900', command = dinn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn12.grid(column = 2, row = 8, padx = 2)



                                l3 = Label(muscle, text = 'VIDEOS', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24')
                                l3.grid(column = 1, row = 9, pady = 30)
                                link1 = Label(muscle, text="Leg Day",font=('rockwell', 14), fg='#CC8899', cursor="hand2", bg = '#243E24')
                                link1.grid(column = 1, row = 10, padx = 5)
                                link1.bind("<Button-1>", lambda e: callback(" https://www.youtube.com/watch?v=8HkhW_N1jFg"))
                                link2 = Label(muscle, text="Arm Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                                link2.grid(column = 1, row = 11, padx = 5)
                                link2.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=eytWFViVIvE"))
                                link3 = Label(muscle, text="Back Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                                link3.grid(column = 1, row = 12, padx = 5)
                                link3.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=pDns20FDhhw"))    

                                fitbtn = Button(muscle, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), activebackground = 'grey', width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                                fitbtn.grid(column = 2, row = 13, pady=5)

                                muscle.mainloop()


                            l1 = Label(underweight,text = 'Your BMI is...., you are underweight', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('impact', 20 ))
                            l1.pack(pady = 10)
                            l2 = Label(underweight,text = 'What\'s your goal?', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 16 ))
                            l2.pack(pady = 25)

                            image = Image.open('yog21.png')  # type: ignore
                            resim = image.resize((180, 180), Image.ANTIALIAS) # type: ignore
                            yog = ImageTk.PhotoImage(resim)
                            yogbtn = Button(underweight, image = yog, command = yoga, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                            yogbtn.pack()
                            l3 = Label(underweight,text = 'YOGA', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14 ))
                            l3.pack()

                            image = Image.open('bm2.png') # type: ignore
                            resim = image.resize((180, 180), Image.ANTIALIAS) # type: ignore
                            mus= ImageTk.PhotoImage(resim)
                            musbtn = Button(underweight, image = mus, command = fit, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                            musbtn.pack()
                            l1 = Label(underweight,text = 'BUILD MUSCLE', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14 ))
                            l1.pack()

                            underweight.mainloop()
                        elif (bmi > 18.5) and (bmi < 24.9):
                            normal = Toplevel(bmi_wd)
                            normal.title('normal')
                            normal.config(bg = '#243E24')

                            normal.geometry('465x644')
                            normal.resizable(False, False)

                            def yoga():
                                yog = Tk()
                                yog.title('Yoga normal')
                                yog.geometry('465x644')
                                yog.config(bg = '#243E24')
                                yog.resizable(False, False)

                                def callback(url):
                                    webbrowser.open_new_tab(url)

                                def eam():
                                    messagebox.showinfo('Early Morning', 'Milk + dry fruits')
                                def brf():
                                    messagebox.showinfo('Breakfast', 'Salad with fruits and vegetables + curd \n Or \n Oatmeal with fruit and flaxseeds \n Or \n Greek yogurt with chia seeds and berries')
                                def mdm():
                                    messagebox.showinfo('Mid Morning', 'Lots of water and fruit if required ')
                                def lch():
                                    messagebox.showinfo('Lunch', 'Marinated tofu pita pocket with Greek salad \n Or \n Red lentil veggie burger with avocado salad')
                                def evs():
                                    messagebox.showinfo('Evening Snack','Dry fruits and milk')
                                def din():
                                    messagebox.showinfo('Dinner', 'Chickpea curry with basmati rice \n Or \n Black bean tacos with cauliflower rice')

                                l = Label(yog, text = ' ', bg = '#243E24', width = 23)
                                l.grid(column = 0, row = 0, pady = 10)

                                lx = Label(yog, text = 'Let\'s get you fitter', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                                lx.grid(column = 1, row = 0, pady = 5)

                                l1 = Label(yog, text = 'DIET PLAN', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24', width = 11)
                                l1.grid(column = 1, row = 1, pady = 10)

                                btn1 = Button(yog, text = 'Early Morning', bg='#ECBD00', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn1.grid(column = 1, row = 2, padx = 2)
                                btn2 = Button(yog, text = 'Breakfast', bg='#ECBD00', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn2.grid(column = 1, row = 3, padx = 2)
                                btn3 = Button(yog, text = 'Mid Morning', bg='#ECBD00', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn3.grid(column = 1, row = 4, padx = 2)
                                btn4 = Button(yog, text = 'Lunch', bg='#ECBD00', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn4.grid(column = 1, row = 5, padx = 2)
                                btn5 = Button(yog, text = 'Evening Snack', bg='#ECBD00', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn5.grid(column = 1, row = 6, padx = 2)
                                btn6 = Button(yog, text = 'Dinner', bg='#ECBD00', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn6.grid(column = 1, row = 7, padx = 2)


                                l3 = Label(yog, text = 'YOGA POSES', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24')
                                l3.grid(column = 1, row = 9, pady = 30)
                                link1 = Label(yog, text="Reference",font=('rockwell', 14), fg='#663A82', cursor="hand2", bg = '#243E24')
                                link1.grid(column = 1, row = 10, padx = 5)
                                link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=4A0-aTZpR8M"))

                                def des():
                                    yog.destroy()

                                yogbtn = Button(yog, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                                yogbtn.grid(column = 2, row = 11, pady=5)

                                yog.mainloop()


                            def fit():
                                muscle = Tk()
                                muscle.title('Muscle normal')
                                muscle.config(bg = '#243E24')
                                muscle.geometry('465x644')
                                muscle.resizable(False, False)

                                def des():
                                    muscle.destroy()

                                def callback(url):
                                    webbrowser.open_new_tab(url)

                                def eam():
                                    messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                                def brf():
                                    messagebox.showinfo('Breakfast', 'A bowl of oats/wheat flakes/ quinoa with skimmed milk and some nuts \n OR \n Whole wheat toast with peanut butter + milk')
                                def mdm():
                                    messagebox.showinfo('Mid Morning', 'Buttermilk made from low-fat yogurt \n OR \n 1 big bowl of watermelon/pineapple/grapefruit + 2 cheese slices')
                                def lch():
                                    messagebox.showinfo('Lunch', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')
                                def evs():
                                    messagebox.showinfo('Evening Snack', 'Sprouts or boiled legumes (chickpea/ black chana) with onion, tomato, cucumber, and lime juice + whey with water + eggs/cottage cheese/ low fat cheese slice \n Or \n Paneer and spinach roll/ 2 slices of brown bread + fresh juice')
                                def din():
                                    messagebox.showinfo('Dinner', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')

                                lx = Label(muscle, text = 'Let\'s get you fitter!!', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                                lx.grid(column = 1, row = 0, pady = 5)

                                l1 = Label(muscle, text = 'DIET PLAN', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24', width = 11)
                                l1.grid(column = 1, row = 1, pady = 10)

                                l2 = Label(muscle, text = 'VEG', font = ('hattenschweiler', 16), fg = '#4C9A2A', bg = '#243E24', width = 13)
                                l2.grid(column = 0, row = 2, pady = 5)

                                l3 = Label(muscle, text = 'NON-VEG', font = ('hattenschweiler', 16), fg = 'red', bg = '#243E24', width = 13)
                                l3.grid(column = 2, row = 2, pady = 5)

                                btn1 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn1.grid(column = 0, row = 3, padx = 2)
                                btn2 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn2.grid(column = 0, row = 4, padx = 2)
                                btn3 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn3.grid(column = 0, row = 5, padx = 2)
                                btn4 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn4.grid(column = 0, row = 6, padx = 2)
                                btn5 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn5.grid(column = 0, row = 7, padx = 2)
                                btn6 = Button(muscle, text = 'Dinner', bg='#CC9900', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn6.grid(column = 0, row = 8, padx = 2)


                                def eamn():
                                    messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                                def brfn():
                                    messagebox.showinfo('Breakfast', '3 to 4 slices of whole wheat bread toast with peanut butter + 3 egg whites + 1 full egg omelette \n OR \n 1 cup of low fat milk + 1 scoop of whey protein+ 150 gms of oatmeal + 1 banana+ a few almonds+ walnuts')
                                def mdmn():
                                    messagebox.showinfo('Mid Morning', '1 orange or apple or 1 cup of green tea + 2 to 3 multigrain biscuits')
                                def lchn():
                                    messagebox.showinfo('Lunch', '150 gms of brown rice or whole wheat chapattis + 150 gms of skinless chicken breast / fish + 1 bowl of mixed vegetables+ green chutney+ salad')
                                def evsn():
                                    messagebox.showinfo('Evening Snack', '1 fruit or green tea or sprouts salad + few nuts')
                                def dinn():
                                    messagebox.showinfo('Dinner', '1 small fish or 100 gms of skinless/ lean chicken + stir fried veggies with baked potato + 1 cup of brown rice/ whole wheat chappati')

                                btn7 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eamn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn7.grid(column = 2, row = 3, padx = 2)
                                btn8 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brfn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn8.grid(column = 2, row = 4, padx = 2)
                                btn9 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdmn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn9.grid(column = 2, row = 5, padx = 2)
                                btn10 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lchn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn10.grid(column = 2, row = 6, padx = 2)
                                btn11 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evsn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn11.grid(column = 2, row = 7, padx = 2)
                                btn12 = Button(muscle, text = 'Dinner', bg='#CC9900', command = dinn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn12.grid(column = 2, row = 8, padx = 2)



                                l3 = Label(muscle, text = 'VIDEOS', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24')
                                l3.grid(column = 1, row = 9, pady = 30)
                                link1 = Label(muscle, text="Arm Day",font=('rockwell', 14), fg='#CC8899', cursor="hand2", bg = '#243E24')
                                link1.grid(column = 1, row = 10, padx = 5)
                                link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=eytWFViVIvE"))
                                link2 = Label(muscle, text="Leg Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                                link2.grid(column = 1, row = 11, padx = 5)
                                link2.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=8HkhW_N1jFg"))
                                link3 = Label(muscle, text="Back Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                                link3.grid(column = 1, row = 12, padx = 5)
                                link3.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=pDns20FDhhw"))    

                                fitbtn = Button(muscle, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), activebackground = 'grey', width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                                fitbtn.grid(column = 2, row = 13, pady=5)

                                muscle.mainloop()


                            l1 = Label(normal,text = 'Your BMI is...., you are normal', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('impact', 20 ))
                            l1.pack(pady = 10)
                            l2 = Label(normal,text = 'What\'s your goal?', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 16 ))
                            l2.pack(pady = 25)

                            image = Image.open('yog21.png')  # type: ignore
                            resim = image.resize((180, 180), Image.ANTIALIAS)  # type: ignore
                            yog = ImageTk.PhotoImage(resim)
                            yogbtn = Button(normal, image = yog, command = yoga, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                            yogbtn.pack()
                            l3 = Label(normal,text = 'YOGA', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14 ))
                            l3.pack()

                            image = Image.open('bm1.png')  # type: ignore
                            resim = image.resize((180, 180), Image.ANTIALIAS)  # type: ignore
                            mus= ImageTk.PhotoImage(resim)
                            musbtn = Button(normal, image = mus, command = fit, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                            musbtn.pack()
                            l1 = Label(normal,text = 'BUILD MUSCLE', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14 ))
                            l1.pack()

                            normal.mainloop()
                        elif (bmi > 24.9) and (bmi < 29.9):
                            overweight = Toplevel(bmi_wd)
                            overweight.title('overweight')
                            overweight.config(bg = '#243E24')

                            overweight.geometry('465x644')
                            overweight.resizable(False, False)

                            def yoga():
                                yog = Tk()
                                yog.title('Yoga overweight')
                                yog.geometry('465x644')
                                yog.config(bg = '#243E24')
                                yog.resizable(False, False)

                                def callback(url):
                                    webbrowser.open_new_tab(url)

                                def eam():
                                    messagebox.showinfo('Early Morning', 'Milk + dry fruits')
                                def brf():
                                    messagebox.showinfo('Breakfast', 'Salad with fruits and vegetables + curd \n Or \n Oatmeal with fruit and flaxseeds \n Or \n Greek yogurt with chia seeds and berries')
                                def mdm():
                                    messagebox.showinfo('Mid Morning', 'Lots of water and fruit if required ')
                                def lch():
                                    messagebox.showinfo('Lunch', 'Marinated tofu pita pocket with Greek salad \n Or \n Red lentil veggie burger with avocado salad')
                                def evs():
                                    messagebox.showinfo('Evening Snack','Dry fruits and milk')
                                def din():
                                    messagebox.showinfo('Dinner', 'Chickpea curry with basmati rice \n Or \n Black bean tacos with cauliflower rice')

                                l = Label(yog, text = ' ', bg = '#243E24', width = 23)
                                l.grid(column = 0, row = 0, pady = 10)

                                lx = Label(yog, text = 'Let\'s get you fit', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                                lx.grid(column = 1, row = 0, pady = 5)

                                l1 = Label(yog, text = 'DIET PLAN', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24', width = 11)
                                l1.grid(column = 1, row = 1, pady = 10)

                                btn1 = Button(yog, text = 'Early Morning', bg='#ECBD00', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn1.grid(column = 1, row = 2, padx = 2)
                                btn2 = Button(yog, text = 'Breakfast', bg='#ECBD00', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn2.grid(column = 1, row = 3, padx = 2)
                                btn3 = Button(yog, text = 'Mid Morning', bg='#ECBD00', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn3.grid(column = 1, row = 4, padx = 2)
                                btn4 = Button(yog, text = 'Lunch', bg='#ECBD00', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn4.grid(column = 1, row = 5, padx = 2)
                                btn5 = Button(yog, text = 'Evening Snack', bg='#ECBD00', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn5.grid(column = 1, row = 6, padx = 2)
                                btn6 = Button(yog, text = 'Dinner', bg='#ECBD00', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn6.grid(column = 1, row = 7, padx = 2)


                                l3 = Label(yog, text = 'YOGA POSES', font = ('impact', 18), fg = '#FFCC00', bg = '#243E24')
                                l3.grid(column = 1, row = 9, pady = 30)
                                link1 = Label(yog, text="Reference",font=('rockwell', 14), fg='#663A82', cursor="hand2", bg = '#243E24')
                                link1.grid(column = 1, row = 10, padx = 5)
                                link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=i2zvV8-qsvU"))

                                def des():
                                    yog.destroy()

                                yogbtn = Button(yog, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                                yogbtn.grid(column = 2, row = 11, pady=5)

                                yog.mainloop()

                            def weightloss():
                                lefa = Tk()
                                lefa.title('Weight Loss')
                                lefa.geometry('465x644')
                                lefa.resizable(False, False)
                                lefa.config(bg = '#243E24')     

                                def callback(url):
                                    webbrowser.open_new_tab(url)

                                def eam():
                                    messagebox.showinfo('Early Morning', 'Warm water (1 glass), Almonds(25 gm)')
                                def brf():
                                    messagebox.showinfo('Breakfast', 'Oats porridge in skimmed milk')
                                def mdm():
                                    messagebox.showinfo('Mid Morning', 'Fruits of any kind except mango and banana')
                                def lch():
                                    messagebox.showinfo('Lunch', 'Salad including vegetables , fruits ,(paneer /chole/dal),spices \n Or \n 2 roti ,1 sabzi')
                                def evs():
                                    messagebox.showinfo('Evening Snack', 'Fruit and milk/coffee(containg honey rather than sugar )')
                                def din():
                                    messagebox.showinfo('Dinner', 'Sabzi , 2 chapatis , daal, steamed rice \n Or \n khichdi')

                                lx = Label(lefa, text = 'Let\'s get you fit!!', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                                lx.grid(column = 1, row = 0, pady = 5)

                                l1 = Label(lefa, text = 'DIET PLAN', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24', width = 11)
                                l1.grid(column = 1, row = 1, pady = 10)

                                l2 = Label(lefa, text = 'VEG', font = ('hattenschweiler', 16), fg = '#4C9A2A', bg = '#243E24', width = 13)
                                l2.grid(column = 0, row = 2)

                                l3 = Label(lefa, text = 'NON-VEG', font = ('hattenschweiler', 16), fg = 'red', bg = '#243E24', width = 13)
                                l3.grid(column = 2, row = 2)

                                btn1 = Button(lefa, text = 'Early Morning', bg='#CC9900', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn1.grid(column = 0, row = 3, padx = 2)
                                btn2 = Button(lefa, text = 'Breakfast', bg='#CC9900', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn2.grid(column = 0, row = 4, padx = 2)
                                btn3 = Button(lefa, text = 'Mid Morning', bg='#CC9900', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn3.grid(column = 0, row = 5, padx = 2)
                                btn4 = Button(lefa, text = 'Lunch', bg='#CC9900', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn4.grid(column = 0, row = 6, padx = 2)
                                btn5 = Button(lefa, text = 'Evening Snack', bg='#CC9900', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn5.grid(column = 0, row = 7, padx = 2)
                                btn6 = Button(lefa, text = 'Dinner', bg='#CC9900', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn6.grid(column = 0, row = 8, padx = 2)


                                def eamn():
                                    messagebox.showinfo('Early Morning', 'Warm water (1 glass), Almonds(25 gm )')
                                def brfn():
                                    messagebox.showinfo('Breakfast', 'Oats porridge in skimmed milk')
                                def mdmn():
                                    messagebox.showinfo('Mid Morning', 'Fruits of any kind except mango and banana')
                                def lchn():
                                    messagebox.showinfo('Lunch', '1 cup rice , chicken curry fresh salad \n Or \n 2 roti , 1 sabzi, 1 cup raw salad, 1 piece chicken or fish')
                                def evsn():
                                    messagebox.showinfo('Evening Snack', 'Fruit and milk/coffee(containg honey rather than sugar )')
                                def dinn():
                                    messagebox.showinfo('Dinner', '1 cup daal/egg curry, 1 cup raw salad \n Or \n khichdi')

                                btn7 = Button(lefa, text = 'Early Morning', bg='#CC9900', command = eamn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn7.grid(column = 2, row = 3, padx = 2)
                                btn8 = Button(lefa, text = 'Breakfast', bg='#CC9900', command = brfn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn8.grid(column = 2, row = 4, padx = 2)
                                btn9 = Button(lefa, text = 'Mid Morning', bg='#CC9900', command = mdmn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn9.grid(column = 2, row = 5, padx = 2)
                                btn10 = Button(lefa, text = 'Lunch', bg='#CC9900', command = lchn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn10.grid(column = 2, row = 6, padx = 2)
                                btn11 = Button(lefa, text = 'Evening Snack', bg='#CC9900', command = evsn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn11.grid(column = 2, row = 7, padx = 2)
                                btn12 = Button(lefa, text = 'Dinner', bg='#CC9900', command = dinn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn12.grid(column = 2, row = 8, padx = 2)



                                l3 = Label(lefa, text = 'VIDEO LINKS', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24')
                                l3.grid(column = 1, row = 9, pady = 30)
                                link1 = Label(lefa, text="Pro Advice",font=('rockwell', 14), fg='#CC8899', cursor="hand2", bg = '#243E24')
                                link1.grid(column = 1, row = 10, padx = 5)
                                link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=G3J0XwUlEBo"))
                                link2 = Label(lefa, text="Exercises",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                                link2.grid(column = 1, row = 11, padx = 5)
                                link2.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=b7YoGQuXYRE"))
                                link3 = Label(lefa, text="Aerobics",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                                link3.grid(column = 1, row = 12, padx = 5)
                                link3.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=oR6jkKsORUI"))

                                def des():
                                    lefa.destroy()

                                fitbtn = Button(lefa, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                                fitbtn.grid(column = 2, row = 13, pady=5)

                                lefa.mainloop()

                            def fit():
                                muscle = Tk()
                                muscle.title('Muscle overweight')
                                muscle.config(bg = '#243E24')
                                muscle.geometry('465x644')
                                muscle.resizable(False, False)

                                def callback(url):
                                       webbrowser.open_new_tab(url)

                                def eam():
                                    messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                                def brf():
                                    messagebox.showinfo('Breakfast', 'A bowl of oats/wheat flakes/ quinoa with skimmed milk and some nuts \n OR \n Whole wheat toast with peanut butter + milk')
                                def mdm():
                                    messagebox.showinfo('Mid Morning', 'Buttermilk made from low-fat yogurt \n OR \n 1 big bowl of watermelon/pineapple/grapefruit + 2 cheese slices')
                                def lch():
                                    messagebox.showinfo('Lunch', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')
                                def evs():
                                    messagebox.showinfo('Evening Snack', 'Sprouts or boiled legumes (chickpea/ black chana) with onion, tomato, cucumber, and lime juice + whey with water + eggs/cottage cheese/ low fat cheese slice \n Or \n Paneer and spinach roll/ 2 slices of brown bread + fresh juice')
                                def din():
                                    messagebox.showinfo('Dinner', '2 wheat/jowar/bajra chapattis or brown rice + veggies + bowl of dal + cottage cheese')

                                lx = Label(muscle, text = 'Let\'s get you fit!!', font = ('impact', 14), fg = '#FFCC00', bg = '#243E24')
                                lx.grid(column = 1, row = 0, pady = 5)

                                l1 = Label(muscle, text = 'DIET PLAN', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24', width = 11)
                                l1.grid(column = 1, row = 1, pady = 10)

                                l2 = Label(muscle, text = 'VEG', font = ('hattenschweiler', 16), fg = '#4C9A2A', bg = '#243E24', width = 13)
                                l2.grid(column = 0, row = 2, pady = 5)

                                l3 = Label(muscle, text = 'NON-VEG', font = ('hattenschweiler', 16), fg = 'red', bg = '#243E24', width = 13)
                                l3.grid(column = 2, row = 2, pady = 5)

                                btn1 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eam, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn1.grid(column = 0, row = 3, padx = 2)
                                btn2 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brf, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn2.grid(column = 0, row = 4, padx = 2)
                                btn3 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdm, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn3.grid(column = 0, row = 5, padx = 2)
                                btn4 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lch, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn4.grid(column = 0, row = 6, padx = 2)
                                btn5 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evs, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn5.grid(column = 0, row = 7, padx = 2)
                                btn6 = Button(muscle, text = 'Dinner', bg='#CC9900', command = din, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn6.grid(column = 0, row = 8, padx = 2)


                                def eamn():
                                    messagebox.showinfo('Early Morning', 'A fruit of your choice + whey protein \n OR \n Soaked almonds + 1 glass skimmed milk')
                                def brfn():
                                    messagebox.showinfo('Breakfast', '3 to 4 slices of whole wheat bread toast with peanut butter + 3 egg whites + 1 full egg omelette \n OR \n 1 cup of low fat milk + 1 scoop of whey protein+ 150 gms of oatmeal + 1 banana+ a few almonds+ walnuts')
                                def mdmn():
                                    messagebox.showinfo('Mid Morning', '1 orange or apple or 1 cup of green tea + 2 to 3 multigrain biscuits')
                                def lchn():
                                    messagebox.showinfo('Lunch', '150 gms of brown rice or whole wheat chapattis + 150 gms of skinless chicken breast / fish + 1 bowl of mixed vegetables+ green chutney+ salad')
                                def evsn():
                                    messagebox.showinfo('Evening Snack', '1 fruit or green tea or sprouts salad + few nuts')
                                def dinn():
                                    messagebox.showinfo('Dinner', '1 small fish or 100 gms of skinless/ lean chicken + stir fried veggies with baked potato + 1 cup of brown rice/ whole wheat chappati')

                                btn7 = Button(muscle, text = 'Early Morning', bg='#CC9900', command = eamn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn7.grid(column = 2, row = 3, padx = 2)
                                btn8 = Button(muscle, text = 'Breakfast', bg='#CC9900', command = brfn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn8.grid(column = 2, row = 4, padx = 2)
                                btn9 = Button(muscle, text = 'Mid Morning', bg='#CC9900', command = mdmn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn9.grid(column = 2, row = 5, padx = 2)
                                btn10 = Button(muscle, text = 'Lunch', bg='#CC9900', command = lchn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn10.grid(column = 2, row = 6, padx = 2)
                                btn11 = Button(muscle, text = 'Evening Snack', bg='#CC9900', command = evsn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn11.grid(column = 2, row = 7, padx = 2)
                                btn12 = Button(muscle, text = 'Dinner', bg='#CC9900', command = dinn, cursor = 'hand2', font = ('garamond'), activebackground = 'grey', height = 2, width = 12, bd = 2, relief = RIDGE, fg = 'white')
                                btn12.grid(column = 2, row = 8, padx = 2)



                                l3 = Label(muscle, text = 'VIDEO LINKS', font = ('impact', 16), fg = '#FFCC00', bg = '#243E24')
                                l3.grid(column = 1, row = 9, pady = 30)
                                link1 = Label(muscle, text="Arm Day",font=('rockwell', 14), fg='#CC8899', cursor="hand2", bg = '#243E24')
                                link1.grid(column = 1, row = 10, padx = 5)
                                link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=eytWFViVIvE"))
                                link2 = Label(muscle, text="Leg Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                                link2.grid(column = 1, row = 11, padx = 5)
                                link2.bind("<Button-1>", lambda e: callback(" https://www.youtube.com/watch?v=8HkhW_N1jFg"))
                                link3 = Label(muscle, text="Back Day",font=('rockwell', 14), fg="#CC8899", cursor="hand2", bg = '#243E24')
                                link3.grid(column = 1, row = 12, padx = 5)
                                link3.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=pDns20FDhhw"))

                                def des():
                                    muscle.destroy()

                                fitbtn = Button(muscle, text = 'Back', bg='#CC9900', command = des, font = ('garamond'), activebackground = 'grey', width = 8, bd = 2, relief = RIDGE, fg = 'white', cursor = 'hand2')
                                fitbtn.grid(column = 2, row = 13, pady=5)

                                muscle.mainloop()


                            l1 = Label(overweight,text = 'Your BMI is...., you are overweight', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('impact', 20 ))
                            l1.pack()
                            l2 = Label(overweight,text = 'What\'s your goal?', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 16 ))
                            l2.pack(pady = 25)

                            image = Image.open('yog21.png')  # type: ignore
                            resim = image.resize((125, 125), Image.ANTIALIAS)  # type: ignore
                            yog = ImageTk.PhotoImage(resim)
                            yogbtn = Button(overweight, image = yog, command = yoga, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                            yogbtn.pack()
                            l2 = Label(overweight,text = 'YOGA', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14))
                            l2.pack()

                            image = Image.open('lf1.png')  # type: ignore
                            resim = image.resize((125, 125), Image.ANTIALIAS)  # type: ignore
                            lf = ImageTk.PhotoImage(resim)
                            lfbtn = Button(overweight, image = lf, command = weightloss, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                            lfbtn.pack()
                            l2 = Label(overweight,text = 'WEIGHTLOSS', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14))
                            l2.pack()

                            image = Image.open('bm3.png')  # type: ignore
                            resim = image.resize((125, 125), Image.ANTIALIAS)   # type: ignore
                            mus= ImageTk.PhotoImage(resim)
                            musbtn = Button(overweight, image = mus, command = fit, borderwidth = 0, cursor = 'hand2', bg = '#243E24')
                            musbtn.pack()
                            l2 = Label(overweight,text = 'BUILD MUSCLE', bg = '#243E24', fg = '#FFCC00', padx=5, pady=5, font=('cooper black', 14))
                            l2.pack()

                            overweight.mainloop()
                        else:
                           Label2.config(text="Obesity!")
                           Label3.config(text="Health may be at risk, if they do not \n lose weight !")

                    def ds():
                        bmi_wd.destroy()
                    def BMI():
                        h= float(Height.get())
                        w=float(Weight.get())
                        m=h/100
                        bmi = round(float(w/m**2))
                        Label1.config(text=bmi)
                        if bmi < 18.5:
                           Label2.config(text="Underweight!")
                           Label3.config(text="You have lower weight then normal body !")
                        elif (bmi > 18.5) and (bmi < 24.9):
                            Label2.config(text="Normal!")
                            Label3.config(text="It indicates that you are healthy !")
                        elif (bmi > 24.9) and (bmi < 29.9):
                            Label2.config(text="Overweight!")
                            Label3.config(text="it indicates that a person is \n slightly overweight ! \n  Adoctor may advice to lose some \n weight for health reasons !")
                        else:
                           Label2.config(text="Obesity!")
                           Label3.config(text="Health may be at risk, if they do not \n lose weight !")
                    #icon
                    image_icon=PhotoImage(file="icon.png")
                    bmi_wd.iconphoto(False,image_icon)
                    #top
                    top = PhotoImage(file="top.png")
                    top_image=Label(bmi_wd,image=top,background="#f0f1f5")
                    top_image.place(x=-10,y=-10)
                    #bottom Box
                    Label(bmi_wd,width=72,height=18,bg="lightblue").pack(side = BOTTOM)
                    #two boxes
                    box= PhotoImage(file="box.png")
                    Label(bmi_wd,image=box).place(x=20,y=100)
                    Label(bmi_wd,image=box).place(x=240,y=100)
                    #scale 
                    Scale=PhotoImage(file="scale.png")
                    Label(bmi_wd,image=Scale,bg="Lightblue").place(x=20,y=310)
                    ##################slider1##################################################
                    current_value = tk.DoubleVar()
                    def get_current_value():
                        return '{: .2f}'.format(current_value.get())
                    def slider_changed(event):
                        Height.set(get_current_value())
                        size = int(float(get_current_value()))
                        img= (Image.open("man.png"))  # type: ignore
                        resized_image = img.resize((50,10+size))
                        photo2=ImageTk.PhotoImage(resized_image)
                        secondimage.config(image=photo2)
                        secondimage.place(x=70,y=550-size)
                        secondimage.image=photo2  # type: ignore
                    #Command o change background color of scale
                    style = ttk.Style()
                    style.configure("TScale",background="White")
                    slider = ttk.Scale(bmi_wd,from_=0,to=220,orient="horizontal",style="TScale",
                                            command=slider_changed,variable=current_value)
                    slider.place(x=80,y=250)
                    ########################################################################
                    ##################slider2##################################################
                    current_value2 = tk.DoubleVar()
                    def get_current_value2():
                        return '{: .2f}'.format(current_value2.get()) 
                    def slider_changed2(event):
                        Weight.set(get_current_value2())
                    #Command o change background color of scale
                    style2= ttk.Style()
                    style2.configure("TScale",background="White")
                    slider2 = ttk.Scale(bmi_wd,from_=0,to=200,orient="horizontal",style="TScale",
                                            command=slider_changed2,variable=current_value2)
                    slider2.place(x=300,y=250)
                    #Entry box
                    Height = StringVar()
                    Weight = StringVar()
                    height=Entry(bmi_wd,textvariable=Height,width=5,font="arial 50",bg="#fff",fg="#000",bd=0,justify = CENTER)
                    height.place(x=35,y=160)
                    Height.set(get_current_value())
                    weight = Entry(bmi_wd,textvariable=Weight,width=5,font="arial 50",bg="#fff",fg="#000",bd=0,justify = CENTER)
                    weight.place(x=255,y=160)
                    Weight.set(get_current_value2())
                    #MAN IMAGE
                    secondimage=Label(bmi_wd,bg="lightblue")
                    secondimage.place(x=70,y=530)
                    Button(bmi_wd,text="View Report",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=280,y=340)
                    Label1=Label(bmi_wd,font="Arial 60 bold",bg="lightblue",fg = "#fff")
                    Label1.place(x=125,y=305)
                    Label2=Label(bmi_wd,font="Arial 20 bold",bg="lightblue",fg = "#fff")
                    Label2.place(x=280,y=430)
                    Label3=Label(bmi_wd,font="Arial 10 bold",bg="lightblue",fg = "#fff")
                    Label3.place(x=200,y=500)
                    bmi_wd.mainloop()
                else:
                    messagebox.showerror("Provided OTP is wrong")
            else:
                messagebox.showerror("Email account has not been registered")




        frame = Frame(otpwd,width= 600,height =600,bg="white")
        frame.place(x=50,y=50)

        heading=Label(frame,text='Signin',fg = "#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x= 100,y=5)



        mail=Entry(frame,width=25,fg='black',border =0,bg='white',font=('Microsoft YaHei UI Light',11))
        mail.place(x=30,y=80)
        mail.insert(0,'Email')
        mail.bind('<FocusIn>', on_enter )
        mail.bind('<FocusOut>', on_leave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

        otp2=Entry(frame,width=25,fg='black',border =0,bg='white',font=('Microsoft YaHei UI Light',11))
        otp2.place(x=30,y=150)
        otp2.insert(0,'OTP')
        otp2.bind('<FocusIn>', onenter )
        otp2.bind('<FocusOut>', onleave)

        Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

        otpsend = Button(frame,width=39,pady=7,text='Send OTP',command=otpsender,bg='#57a1f8',fg='white',border=0)
        otpsend.place(x=35,y=387)

        Button(frame,width=39,pady=7,text='Sign in',command=entry,bg='#57a1f8',fg='white',border=0).place(x=35,y=457)


        otpwd.mainloop()
    
    

    #MAINPROGRAM




    root=Tk()
    root.title('Login')
    root.geometry('450x644')

    root.configure(bg='#fff')
    root.resizable(False,False)



    frame = Frame(root,width= 600,height =600,bg="white")
    frame.place(x=50,y=50)

    heading=Label(frame,text='Signin',fg = "#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x= 100,y=5)



    user=Entry(frame,width=25,fg='black',border =0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter )
    user.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    code=Entry(frame,width=25,fg='black',border =0,bg='white',font=('Microsoft YaHei UI Light',11),show = '*')
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>', onenter )
    code.bind('<FocusOut>', onleave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    def showpass():
        if code.cget('show') == '*':
            code.config(show = '')
        else :
            code.config(show = '*')

    check_button = Checkbutton(frame, text = "show password", command=showpass)
    check_button.place(x= 30 , y = 170)


    Button(frame,width=39,pady=7,text='Sign in',command=signin,bg='#57a1f8',fg='white',border=0).place(x=35,y=220)

    label=Label(frame,text="Don't have account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=290)

    sign_up=Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',fg='#57a1f8',command = signup_cc)
    sign_up.place(x=215,y=290)

    label1=Label(frame,text="Sign up with otp",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label1.place(x=75,y=360)

    otpsignin= Button(frame,width=10,text="Click here",border=0,bg='white',cursor='hand2',fg='#57a1f8',command = signinwithootp)
    otpsignin.place(x=175,y= 360)

    root.mainloop() 

home_screen()