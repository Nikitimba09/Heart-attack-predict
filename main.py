import datetime
import tkinter as tk
from datetime import date
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np
import matplotlib

from backend import *

matplotlib.use("TkAgg")


background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(False, False)
root.config(bg=background)


# ANALYSIS #########
def analysis():
    name = Name.get()
    D1 = Date.get()
    today = datetime.date.today()
    A = today.year - DOB.get()

    try:
        B = selection()
    except:
        messagebox.showerror("missing", "Please select gender!")
        return

    try:
        F = selection2()
    except:
        messagebox.showerror("missing", "Please select fbs!")
        return

    try:
        I = selection3()
    except:
        messagebox.showerror("missing", "Please select exang!")
        return

    try:
        C = int(selection4())
    except:
        messagebox.showerror("missing", "Please select cp!")
        return

    try:
        G = int(restecg_combobox.get())
    except:
        messagebox.showerror("missing", "Please select restecg!")
        return

    try:
        K = int(selection5())
    except:
        messagebox.showerror("missing", "Please select slope!")
        return

    try:
        L = int(ca_combobox.get())
    except:
        messagebox.showerror("missing", "Please select ca!")
        return

    try:
        M = int(thal_combobox.get())
    except:
        messagebox.showerror("missing", "Please select thal!")
        return

    try:
        D = int(trestbps.get())
        E = int(chol.get())
        H = int(thalach.get())
        J = float(oldpeak.get())
    except:
        messagebox.showerror("missing data", "Few missing data entry!")
        return

    ### First graph
    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    a.plot(["Sex", "fbs", "exang"], [B, F, I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas._tkcanvas.place(width=250, height=250, x=600, y=240)

    ### Second graph
    f2 = Figure(figsize=(5, 5), dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(["age", "trestbps", "chol", "thalach"], [A, D, E, H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas2._tkcanvas.place(width=250, height=250, x=860, y=240)

    ### Third graph
    f3 = Figure(figsize=(5, 5), dpi=100)
    a3 = f3.add_subplot(111)
    a3.plot(["oldpeak", "resticg", "cp"], [J, G, C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas3._tkcanvas.place(width=250, height=250, x=600, y=470)

    ### Fourth graph
    f4 = Figure(figsize=(5, 5), dpi=100)
    a4 = f4.add_subplot(111)
    a4.plot(["slope", "ca", "thal"], [K, L, M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas4._tkcanvas.place(width=250, height=250, x=860, y=470)

    # input data
    input_data = (A, B, C, D, E, F, G, H, I, J, K, L, M)

    input_data_as_numpy_array = np.asanyarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshape)
    print(prediction[0])

    if (prediction[0] == 0):
        print('The Person does not have a Heart disease')
        report.config(text=f'Report:{0}', fg="#8dc63f")
        report1.config(text=f'{name}, you do not have a heart disease')
    else:
        print('The Person has Heart disease')
        report.config(text=f'Report:{1}', fg="#ed1c24")
        report1.config(text=f'{name}, you have a heart disease')


# info window (operated by info button)
def Info():
    Icon_window = Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("1000x700")

    # icon image
    icon_image = PhotoImage(file="Images/info.png")
    Icon_window.iconphoto(False, icon_image)

    # Heading
    Label(Icon_window, text="Информация, относящаяся к набору данных", font="robot 19 bold").pack(padx=20, pady=20)

    # info
    Label(Icon_window, text="age(возраст) - возраст в годах", font="arial 11").place(x=20, y=100)
    Label(Icon_window, text="sex(gender) - пол (1 = мужчина, 0 = женщина)", font="arial 11").place(x=20, y=130)
    Label(Icon_window, text="cp - тип боли в груди (0 = типичная стенокардия, "
                            "1 = атипичная стенокардия, "
                            "2 = неангинальная боль, "
                            "3 = бессимптомная)", font="arial 11").place(x=20, y=160)
    Label(Icon_window,
          text="trestbps - артериальное давление в состоянии покоя (в мм рт.ст. при поступлении в больницу)",
          font="arial 11").place(x=20, y=190)
    Label(Icon_window, text="chol -  уровень холестерина в сыворотке крови в мг/дл", font="arial 11").place(x=20, y=220)
    Label(Icon_window, text="fbs - уровень сахара в крови натощак > 120 мг/дл (1 = верно; 0 = ложно)",
          font="arial 11").place(x=20, y=250)
    Label(Icon_window, text="restecg - результаты электрокардиографии в состоянии покоя "
                            "(0 = в норме; "
                            "1 = наличие ST-T; "
                            "2 = гипертрофия)", font="arial 11").place(x=20, y=280)
    Label(Icon_window,
          text="thalach - максимальная частота сердечных сокращений, достигнутая при стенокардии, вызванной физической "
               "нагрузкой (1 = да; 0 = нет)",
          font="arial 11").place(x=20, y=310)
    Label(Icon_window, text="exang - стенокардия, вызванная физической нагрузкой (1 = да; 0 = нет)",
          font="arial 11").place(x=20, y=340)
    Label(Icon_window, text="oldpeak - Депрессия ЭКГ, вызванная физической нагрузкой по сравнению с отдыхом",
          font="arial 11").place(x=20, y=370)
    Label(Icon_window,
          text="slope - наклон пикового сегмента ЭКГ упражнения (0 = подъем; 1 = ровный; 2 = спуск)",
          font="arial 11").place(x=20, y=400)
    Label(Icon_window, text="ca - количество крупных сосудов (0-3), окрашенных при флуороскопии",
          font="arial 11").place(x=20, y=430)
    Label(Icon_window, text="thal - Заболевание крови, называемое талассемией - 0 = норма; 1 = исправленный дефект; "
                            "2 = обратимый дефект", font="arial 11").place(x=20, y=460)

    Icon_window.mainloop()


def Clear():
    Name.get()
    DOB.get()
    trestbps.get()
    chol.get()
    thalach.set("")
    oldpeak.set("")


'''________________________________________________________________'''

# icon 1
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

# header section 2
logo = PhotoImage(file="Images/header.png")
myimage = Label(image=logo, bg=background)
myimage.place(x=0, y=0)

# frame
Heading_entry = Frame(root, width=800, height=190, bg="#df2d4b")
Heading_entry.place(x=600, y=20)

Label(Heading_entry, text="Registration No.", font='arial 13', bg="#df2d4b", fg=framefg).place(x=30, y=0)
Label(Heading_entry, text="Date", font='arial 13', bg="#df2d4b", fg=framefg).place(x=430, y=0)

Label(Heading_entry, text="Patient Name", font='arial 13', bg="#df2d4b", fg=framefg).place(x=30, y=90)
Label(Heading_entry, text="Birth Year", font='arial 13', bg="#df2d4b", fg=framefg).place(x=430, y=90)

Entry_image = PhotoImage(file="Images/Rounded Rectangle 1.png")
Entry_image2 = PhotoImage(file="Images/Rounded Rectangle 2.png")
Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=20, y=30)
Label(Heading_entry, image=Entry_image, bg="#df2d4b").place(x=430, y=30)

Label(Heading_entry, image=Entry_image2, bg="#df2d4b").place(x=20, y=120)
Label(Heading_entry, image=Entry_image2, bg="#df2d4b").place(x=430, y=120)

Registration = IntVar()
reg_entry = Entry(Heading_entry, textvariable=Registration, width=30, font='arial 15', bg="#0e5363", fg="white", bd=0)
reg_entry.place(x=30, y=45)

Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(Heading_entry, textvariable=Date, width=15, font='arial 15', bg="#0e5363", fg="white", bd=0)
date_entry.place(x=500, y=45)
Date.set(d1)

Name = StringVar()
name_entry = Entry(Heading_entry, textvariable=Name, width=20, font='arial 20', bg="#ededed", fg="#222222", bd=0)
name_entry.place(x=30, y=130)

DOB = IntVar()
dob_entry = Entry(Heading_entry, textvariable=DOB, width=20, font='arial 20', bg="#ededed", fg="#222222", bd=0)
dob_entry.place(x=450, y=130)

# BODY
Detail_entry = Frame(root, width=490, height=260, bg="#dbe0e3")
Detail_entry.place(x=30, y=450)

# Radio Button
Label(Detail_entry, text="Пол:", font="arial 13", bg=framebg, fg=framefg).place(x=10, y=10)
Label(Detail_entry, text="fbs:", font="arial 13", bg=framebg, fg=framefg).place(x=180, y=10)
Label(Detail_entry, text="exang:", font="arial 13", bg=framebg, fg=framefg).place(x=335, y=10)


def selection():
    if gen.get() == 1:
        Gender = 1
        return (Gender)
    elif gen.get() == 2:
        Gender = 0
        return (Gender)


def selection2():
    if fbs.get() == 1:
        Fbs = 1
        return (Fbs)
    elif fbs.get() == 2:
        Fbs = 0
        return (Fbs)


def selection3():
    if exang.get() == 1:
        Exang = 1
        return (Exang)
    elif exang.get() == 2:
        Exang = 0
        return (Exang)


gen = IntVar()
R1 = Radiobutton(Detail_entry, text="Муж", variable=gen, value=1, command=selection)
R2 = Radiobutton(Detail_entry, text="Жен", variable=gen, value=2, command=selection)
R1.place(x=43, y=10)
R2.place(x=93, y=10)

fbs = IntVar()
R3 = Radiobutton(Detail_entry, text="True", variable=fbs, value=1, command=selection2)
R4 = Radiobutton(Detail_entry, text="False", variable=fbs, value=2, command=selection2)
R3.place(x=213, y=10)
R4.place(x=263, y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry, text="Yes", variable=exang, value=1, command=selection3)
R6 = Radiobutton(Detail_entry, text="No", variable=exang, value=2, command=selection3)
R5.place(x=387, y=10)
R6.place(x=430, y=10)

# COMBOBOX

Label(Detail_entry, text='cp:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=50)
Label(Detail_entry, text='restecg:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=90)
Label(Detail_entry, text='slope:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=130)
Label(Detail_entry, text='ca:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=170)
Label(Detail_entry, text='thal:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=210)


def selection4():
    input = cp_combobox.get()
    if input == '0 = typical angina':
        return 0
    elif input == '1 = atypical angina':
        return 1
    elif input == '2 = non-anginal pain':
        return 2
    elif input == '3 = asymptomatic':
        return 3


def selection5():
    input = slope_combobox.get()
    if input == '0 = upsloping':
        return 0
    elif input == '1 = flat':
        return 1
    elif input == '2 = downsloping':
        return 2


cp_combobox = Combobox(Detail_entry, values=['0 = typical angina', '1 = atypical angina', '2 = non-anginal pain',
                                             '3 = asymptomatic'], font='arial 12', state='r', width=14)
restecg_combobox = Combobox(Detail_entry, values=['0 ', '1', '2'], font='arial 12', state='r', width=11)
slope_combobox = Combobox(Detail_entry, values=['0 = upsloping', '1 = flat', '2 = downsloping'], font='arial 12',
                          state='r', width=12)
ca_combobox = Combobox(Detail_entry, values=['0 ', '1', '2', '3', '4'], font='arial 12', state='r', width=14)
thal_combobox = Combobox(Detail_entry, values=['0 ', '1', '2', '3', '4'], font='arial 12', state='r', width=14)

cp_combobox.place(x=50, y=50)
restecg_combobox.place(x=80, y=90)
slope_combobox.place(x=70, y=130)
ca_combobox.place(x=50, y=170)
thal_combobox.place(x=50, y=210)

# DATA ENTRY box 2 columns

Label(Detail_entry, text="Smoking:", font='arial 13', width=7, bg=framebg, fg=framefg).place(x=240, y=50)
Label(Detail_entry, text="trestbps:", font='arial 13', width=7, bg=framebg, fg=framefg).place(x=240, y=90)
Label(Detail_entry, text="chol:", font='arial 13', width=7, bg=framebg, fg=framefg).place(x=240, y=130)
Label(Detail_entry, text="thalach:", font='arial 13', width=7, bg=framebg, fg=framefg).place(x=240, y=170)
Label(Detail_entry, text="oldpeak:", font='arial 13', width=7, bg=framebg, fg=framefg).place(x=240, y=210)

trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

trestbps_entry = Entry(Detail_entry, textvariable=trestbps, width=10, font='arial 15', bg='#ededed', fg='#222222', bd=0)
chol_entry = Entry(Detail_entry, textvariable=chol, width=10, font='arial 15', bg='#ededed', fg='#222222', bd=0)
thalach_entry = Entry(Detail_entry, textvariable=thalach, width=10, font='arial 15', bg='#ededed', fg='#222222', bd=0)
oldpeak_entry = Entry(Detail_entry, textvariable=oldpeak, width=10, font='arial 15', bg='#ededed', fg='#222222', bd=0)

trestbps_entry.place(x=320, y=90)
chol_entry.place(x=320, y=130)
thalach_entry.place(x=320, y=170)
oldpeak_entry.place(x=320, y=210)

# END ENTRY #####


# REPORT IMAGE ###

square_report_image = PhotoImage(file="Images/Report.png")
report_background = Label(image=square_report_image, bg=background)
report_background.place(x=1120, y=340)

report = Label(root, font="arial 25 bold", bg='white', fg='#8dc63f')
report.place(x=1170, y=550)

report1 = Label(root, font="arial 10 bold", bg='white')
report1.place(x=1130, y=610)

# GRAPHIC IMAGE ###
graph_image = PhotoImage(file="Images/graph.png")
Label(image=graph_image).place(x=600, y=270)
Label(image=graph_image).place(x=860, y=270)
Label(image=graph_image).place(x=600, y=500)
Label(image=graph_image).place(x=860, y=500)

# Button  ###
analysis_button = PhotoImage(file="Images/Analysis.png")
Button(root, image=analysis_button, bd=0, bg=background, cursor='hand2', command=analysis).place(x=1130, y=240)

# INFO Button  ###
info_button = PhotoImage(file="Images/info.png")
Button(root, image=info_button, bd=0, bg=background, cursor='hand2', command=Info).place(x=10, y=240)

# SAVE Button  ###
save_button = PhotoImage(file="Images/save.png")
Button(root, image=save_button, bd=0, bg=background, cursor='hand2').place(x=1370, y=250)

# Smoking and Non Smoking Button  ###
button_mode = True
choice = 'smoking'


def changemode():
    global button_mode
    global choice

    if button_mode:
        choice = 'non_smoking'
        mode.config(image=non_smoking_icon, activebackground="white")
        button_mode = False
    else:
        choice = "smoking"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode = True

    print(choice)


smoking_icon = PhotoImage(file="Images/smoker.png")
non_smoking_icon = PhotoImage(file="Images/non-smoker.png")

mode = Button(root, image=smoking_icon, bg='#dbe0e3', bd=0, cursor='hand2', command=changemode)
mode.place(x=350, y=495)

# LogOut Button  ###

logout_icon = PhotoImage(file="Images/logout.png")
logout_button = Button(root, image=logout_icon, bg="#df2d4b", cursor="hand2", bd=0, command=exit)
logout_button.place(x=1390, y=60)

root.mainloop()
