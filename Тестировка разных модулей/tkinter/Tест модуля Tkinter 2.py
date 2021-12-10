from tkinter import *

ThemeList = ["Миология",
             "Остеология",
             "Суставы",
             "Краниология"]
ThemeListMyology = ["Спина и шея",
              "Грудь и живот",
              "Верхние конечности",
              "Кисть",
              "Мышцы таза",
              "Нижние конечности",
              "Ступни"]
FuncList = ["ClickThemeMuscle",
            "ClickThemeBones",
            "ClickThemeСуставы",
            "ClickThemeКраниология"]
CT2Buttons = ["Myology",
              "Osteology",
              "Joints",
              "Cranilogy"]


# Функции кнопок
def ClickThemeOsteology():
    None

def ClickThemeJoints():
    None

def ClickThemeCraniology():
    None

def ClickTheme2(x):
    if x == 1:
       global Myology, Osteology, Joints, Craniology
       Craniology.destroy()
       Joints.destroy()
       Myology.destroy()
       Osteology.destroy()
    elif x == 0:
       main.title('Выбор темы теста')
       Myology = Button(main,
                      text = 'Миология',
                      font = ('Courier New',10),
                      width = 15,
                      height = 5,
                      bg = 'black', fg = 'white',
                      command = ClickThemeMyology)
       Myology.grid(column = 0, row = 0)
    
       Osteology = Button(main,
                        text = 'Остеология',
                        font = ('Courier New',10),
                        width = 15,
                        height = 5,
                        bg = 'black', fg = 'white',
                        command = ClickThemeOsteology)
       Osteology.grid(column = 0, row = 1)

       Joints = Button(main,
                     text = 'Суставы',
                     font = ('Courier New',10),
                     width = 15,
                     height = 5,
                     bg = 'black', fg = 'white',
                     command = ClickThemeJoints)
       Joints.grid(column = 1, row = 0)

       Craniology = Button(main,
                        text = 'Краниология',
                        font = ('Courier New',10),
                        width = 15,
                        height = 5,
                        bg = 'black', fg = 'white',
                        command = ClickThemeCraniology)
       Craniology.grid(column = 1, row = 1)

def ClickTheme():
    lbl.configure(text = "")
    ClickTheme2(x = 0)
    btnRecord.destroy()
    btnTheme.destroy()
    entr.destroy()

def ClickThemeMyology():
    main.title('Выбор группы мышц')
    ClickTheme2(x = 1)
    for i in ThemeListMyology:
        for j in range(len(ThemeListMyology)):
             i = Button(main,
                        text = ThemeListMyology[j],
                        font = ('Courier New',10),
                        width = 20,
                        height = 5,
                        bg = 'black', fg = 'white')
             z1 = j
             if z1%2 == 0:
                 z2 = 0
             else:
                 z1 = j - 1
                 z2 = 1
                 
             i.grid(column = z1,row = z2)

# Создание рабочего окна и его названия
main = Tk()
main.title("Тест по анатомии")

lbl = Label(main, text='Тест по АНАТОМИИ',
            font = ("Courier New", 30),
            fg = 'black')
#img = PhotoImage(Image.open('baby.jpg'))
#pictureMain = Label(main, image = img)
lbl.grid()

# Разрешения окна
main.geometry('800x600+350+100')


# Кнопки взаимодействия главного меню
btnTheme = Button(main, text="Выбрать тему",
              bg = 'black', fg = 'white',
                  command = ClickTheme)
btnTheme.grid()
btnTheme.place(x = 400, y = 350)
btnRecord = Button(main, text = 'Отчёты о прошлых работах',
              bg = 'black', fg = 'white')
btnRecord.grid()
btnRecord.place(x = 580, y = 571)


# Строка для введения данных
entr = Entry(main, width=30)
entr.grid(column = 0, row = 2)


# Функия, которая постоянно вызывает окно, не давая ему закрываться
# после появления
main.mainloop()
