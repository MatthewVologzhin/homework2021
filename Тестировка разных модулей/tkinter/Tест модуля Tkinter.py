from tkinter import *

ThemeList = ["Миология",
             "Остеология",
             "Суставы",
             "Краниология"]
ThemeListMuscle = ["Спина и шея",
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

# Функции кнопок
def CloseWindow(wind):
   return wind.destroy()

def ClickThemeOsteology():
    None

def ClickThemeJoints():
    None

def ClickThemeCraniology():
    None

def ClickTheme():
    Theme = Tk()
    Theme.title('Выбор темы теста')
    Myology = Button(Theme,
                      text = 'Миология',
                      font = ('Courier New',10),
                      width = 15,
                      height = 5,
                      bg = 'black', fg = 'white',
                      command = ClickThemeMuscle)
    Myology.grid(column = 0, row = 0)
    
    Osteology = Button(Theme,
                        text = 'Остеология',
                        font = ('Courier New',10),
                        width = 15,
                        height = 5,
                        bg = 'black', fg = 'white',
                        command = ClickThemeOsteology)
    Osteology.grid(column = 0, row = 1)

    Joints = Button(Theme,
                     text = 'Суставы',
                     font = ('Courier New',10),
                     width = 15,
                     height = 5,
                     bg = 'black', fg = 'white',
                     command = ClickThemeJoints)
    Joints.grid(column = 1, row = 0)

    Craniology = Button(Theme,
                        text = 'Краниология',
                        font = ('Courier New',10),
                        width = 15,
                        height = 5,
                        bg = 'black', fg = 'white',
                        command = ClickThemeCraniology)
    Craniology.grid(column = 1, row = 1)
    CloseWindow(main)
    Theme.mainloop()

def ClickThemeMuscle():
    ThemeMuscle = Tk()
    ThemeMuscle.title('Выбор темы теста')
    for i in ThemeListMuscle:
        for j in range(len(ThemeListMuscle)):
             i = Button(ThemeMuscle,
                              text = ThemeListMuscle[j],
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
    ThemeMuscle.mainloop()

# Создание рабочего окна и его названия
main = Tk()
main.title("Тест по анатомии")

lbl = Label(main, text='Тест по АНАТОМИИ',
            font = ("Courier New", 30),
            fg = 'white',
            bg = 'black',
            width = 50,
            height = 10)
lbl.grid(column = 0, row = 0)

# Разрешения окна
# main.geometry('1280x720')


# Кнопки взаимодействия главного меню
btnTheme = Button(main, text="Выбрать тему",
              bg = 'black', fg = 'white',
                  command = ClickTheme)
btnTheme.grid(column = 0, row = 1)
btnRecord = Button(main, text = 'Отчёты о прошлых работах',
              bg = 'black', fg = 'white')
btnRecord.grid(column = 1, row = 1)

# Строка для введения данных
entr = Entry(main, width=30)
entr.grid(column = 0, row = 2)


# Функия, которая постоянно вызывает окно, не давая ему закрываться
# после появления
main.mainloop()
