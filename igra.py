
from random import randint
from tkinter import *
from tkinter import ttk

from slojka import StateMacine, States

mashine = StateMacine()

config = {
    States.Easy: {'min': 0, 'max': 100, 'tries': 8},
    States.Normal: {'min': -100, 'max': 100, 'tries': 10},
    States.Difficult: {'min': -1000, 'max': 1000, 'tries': 12}
}

global gues
global new_window_2
global txt

def difficulty_selection():
    new_window_1 = Tk()
    new_window_1.title('Выбор сложности')
    new_window_1.geometry('1300x750')
    btn_00 = Label(new_window_1, text='Выберите сложность игры', bg='white', fg='black', font=('Times New Roman', 35))
    btn_00.grid(row=0, column=1, ipadx=5, ipady=10, sticky=W, padx=90, pady=80)
    btn_11 = Button(new_window_1, text='Простая: -50 до 50(8 попыток)', bg='white', fg='black', font=('Times New Roman', 35),
                    command=lambda: mashine.set_state(States.Easy))
    btn_11.grid(row=1, column=1, sticky=W, padx=70, pady=0)
    btn_22 = Button(new_window_1, text='Средняя: -100 до 100(10 попыток)', bg='white', fg='black', font=('Times New Roman', 35),
                    command=lambda: mashine.set_state(States.Normal))
    btn_22.grid(row=2, column=1, sticky=W, padx=40, pady=10)
    btn_33 = Button(new_window_1, text='Высокая: -1000 до 1000(12 попыток)', bg='white', fg='black', font=('Times New Roman', 35),
                    command=lambda: mashine.set_state(States.Difficult))
    btn_33.grid(row=3, column=1, sticky=W, padx=20, pady=0)
    btn_44 = Button(new_window_1, text='Назад', bg='white', fg='black', font=('Times New Roman', 35),
                    command=new_window_1.destroy)
    btn_44.grid(row=5, column=0, padx=20, pady=80)
    btn_55 = Button(new_window_1, text='Ввести имя', bg='white', fg='black', font=('Times New Roman', 35),
                    command=name)
    btn_55.grid(row=5, column=2, padx=0, pady=0)

# def name_player():     получаем введенное имя
#     Label["text"] = Entry.get()


def name():
    new_window_5 = Tk()
    new_window_5.title('Имя Игрока')
    new_window_5.geometry('700x400')
    btn_1_1 = Button(new_window_5, text='Назад', bg='white', fg='black', font=('Times New Roman', 25),
                    command=new_window_5.destroy)
    btn_1_1.grid(row=1, column=0, padx=5, pady=0)
    btn_1_2 = Button(new_window_5, text='Играем!', bg='white', fg='black', font=('Times New Roman', 25),
                     command=new_window_5.destroy and game)
    btn_1_2.grid(row=1, column=3, padx=0, pady=0)
    txt = Entry(new_window_5, width=35)
    txt.grid(row=0, column=1, padx=100, pady=150)




def game():
    global txt
    global new_window_2
    new_window_2 = Tk()
    new_window_2.title('Игра "Угадай число')
    new_window_2.geometry('1600x1000')
    mode = config.get(mashine.get_state(), {'min': 0, 'max': 100, 'tries': 8})
    gues = randint(mode['min'], mode['max'])
    print(gues)
    frame = LabelFrame(new_window_2, padx=200, pady=100)
    frame.place(x=900, y=100)


    txt = Entry(frame, width=20)
    txt.grid(row=4, column=0, columnspan=5, padx=1, pady=100)


    btn_0_0 = Button(frame, text=1, bg='white', fg='black', font=('Times New Roman', 20),
                     command=lambda: set_txt(txt, "1"))
    btn_0_0.grid(row=0, column=0, pady=1, padx=1)
    btn_1_1 = Button(frame, text=2, bg='white', fg='black', font=('Times New Roman', 20),
                     command=lambda: set_txt(txt, "2"))
    btn_1_1.grid(row=0, column=1, pady=1, padx=1)
    btn_2_2 = Button(frame, text=3, bg='white', fg='black', font=('Times New Roman', 20),
                     command=lambda: set_txt(txt, "3"))
    btn_2_2.grid(row=0, column=2, pady=1, padx=1)
    btn_3_3 = Button(frame, text=4, bg='white', fg='black', font=('Times New Roman', 20),
                     command=lambda: set_txt(txt, "4"))
    btn_3_3.grid(row=1, column=0, pady=1, padx=1)
    btn_4_4 = Button(frame, text=5, bg='white', fg='black', font=('Times New Roman', 20),
                     command=lambda: set_txt(txt, "5"))
    btn_4_4.grid(row=1, column=1, pady=1, padx=1)
    btn_5_5 = Button(frame, text=6, bg='white', fg='black', font=('Times New Roman', 20),
                     command=lambda: set_txt(txt, "6"))
    btn_5_5.grid(row=1, column=2, pady=1, padx=1)
    btn_6 = Button(frame, text=7, bg='white', fg='black', font=('Times New Roman', 20),
                   command=lambda: set_txt(txt, "7"))
    btn_6.grid(row=2, column=0, pady=1, padx=1)
    btn_7 = Button(frame, text=8, bg='white', fg='black', font=('Times New Roman', 20),
                   command=lambda: set_txt(txt, "8"))
    btn_7.grid(row=2, column=1, pady=1, padx=1)
    btn_8 = Button(frame, text=9, bg='white', fg='black', font=('Times New Roman', 20),
                   command=lambda: set_txt(txt, "9"))
    btn_8.grid(row=2, column=2, pady=1, padx=1)
    btn_9 = Button(frame, text=0, bg='white', fg='black', font=('Times New Roman', 20),
                   command=lambda: set_txt(txt, "0"))
    btn_9.grid(row=3, column=1, pady=1, padx=1)
    btn_10 = Button(frame, text='Del', bg='white', fg='black', font=('Times New Roman', 14),
                    command=clear)
    btn_10.grid(row=3, column=0, pady=1, padx=1)
    btn_11 = Button(frame, text="-", bg='white', fg='black', font=('Times New Roman', 20),
                    command=lambda: set_minuse(txt))
    btn_11.grid(row=3, column=2)
    btn_12 = Button(new_window_2, text="Попробовать число!", bg='white', fg='black', font=('Times New Roman', 20),
                    command=games)
    btn_12.grid(row=3, column=3, padx=430, pady=890)
    btn_13 = Button(new_window_2, text="Изменить сложность!", bg='white', fg='black', font=('Times New Roman', 20),
                    command=difficulty_selection)
    btn_13.grid(row=3, column=0, padx=100, pady=10)
    btn_14 = Button(new_window_2, text="Правила игры!", bg='white', fg='black', font=('Times New Roman', 20),
                    command=game_rules)
    btn_14.grid(row=3, column=1, padx=0, pady=20)

def games():                                                       # здесь
    global new_window_2
    global txt
    global gues
    frame_2 = LabelFrame(new_window_2, padx=300, pady=320)
    frame_2.place(x=10, y=70)

    btn_0_0 = Button(frame_2, text=1, bg='white', fg='black', font=('Times New Roman', 20),
                     command=lambda: set_txt(txt, "1"))
    btn_0_0.grid(row=0, column=0, pady=1, padx=1)

    tries = 0
    while True:
        msg = txt.get()
        int(msg)
        if msg == gues:
            tries += 1
            print("Поздравляем ты угадал, использовав {'tries'} попыток!")
            break
        elif msg < gues:
            print('Твое число меньше загаданного числа')
            tries += 1
        elif msg > gues:
            print('Твое число больше загаданного числа')
            tries += 1
        else:
            print('К сожалению вы использовали все свои попытки.')
            break

def oops():                 # кончились попытки повтор игры?
    new_window_6 = Tk()
    new_window_6.title('Упс!')
    new_window_6.geometry('530x300')
    btnn0 = Label(new_window_6, text='У вас кончились попытки.\nСыграем еще?', bg='white', fg='black', font=('Times New Roman', 20))
    btnn0.grid(row=0, column=1, ipadx=5, ipady=10, sticky=W, padx=0, pady=55)
    btnn1 = Button(new_window_6, text='Нет', bg='white', fg='black', font=('Times New Roman', 20),
                   command=new_window_6.quit)
    btnn1.grid(row=1, column=0, pady=20, padx=20)
    btnn2 = Button(new_window_6, text='Да', bg='white', fg='black', font=('Times New Roman', 20),
                   command=game)
    btnn2.grid(row=1, column=2, pady=20, padx=20)
def congratulations():    # окно повтора игры
    new_window_5 = Tk()
    new_window_5.title('Вы выйграли!!')
    new_window_5.geometry('550x300')
    btnn0 = Label(new_window_5, text='Поздравляем!!!Сыграем еще?', bg='white', fg='black', font=('Times New Roman', 20))
    btnn0.grid(row=0, column=1, ipadx=5, ipady=10, sticky=W, padx=0, pady=80)
    btnn1 = Button(new_window_5, text='Нет', bg='white', fg='black', font=('Times New Roman', 20),
                     command=new_window_5.quit)
    btnn1.grid(row=1, column=0, pady=20, padx=20)
    btnn2 = Button(new_window_5, text='Да', bg='white', fg='black', font=('Times New Roman', 20),
                     command=game)
    btnn2.grid(row=1, column=2, pady=20, padx=20)
def clear():
    txt.delete(0, END)


def pr(txt):
    value = txt.get()
    if not value.isdigit():
        print(213)
        return


def set_txt(txt_frame: Entry, txt):
    old_value = txt_frame.get()
    txt_frame.delete(0, len(old_value) + 1)
    txt_frame.insert(0, old_value + txt)


def set_minuse(txt_frame: Entry):
    old_value = txt_frame.get()
    if not '-' in old_value:
        txt_frame.insert(0, "-")


def game_rules():
    new_window_3 = Tk()
    new_window_3.title('Правила игры')
    new_window_3.geometry('850x700')
    btn_11 = Button(new_window_3, text='Назад', bg='white', fg='black', font=('Times New Roman', 35),
                    command=new_window_3.destroy)
    btn_11.grid(row=1, column=0, padx=0, pady=100)
    text = "«Угадай число» это одна из простейших игр для \nдвух игроков  или игра с компьютером.\n Один игрок(копмпьютер)задумывает число\n из известного диапазона,второй пытается\n угадать это число. После каждой попытки \nигроку дается ответ «больше», «меньше» \nили «угадал», в зависимости от того, является \nзадуманное им число большим, меньшим или \nравным предложенному:"
    lbl = Label(new_window_3, text=text, font=("Times New Roman", 30))
    lbl.grid(column=0, row=0)



def leaderboard():                                    #почему то не высвечивается шапка таблицы лидеров
    new_window_4 = Tk()
    new_window_4.title("Таблица лидеров")
    new_window_4.geometry("800x1000")
    columns = ("name", "difficulty", "tries")
    tree = ttk.Treeview(columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)
    tree.heading("name", text="Имя")
    tree.heading("difficulty", text="Выбранная сложность")
    tree.heading("tries", text="Количество попыток")
    btn_10 = Button(new_window_4, text='Назад', bg='white', fg='black', font=('Times New Roman', 35),
                    command=new_window_4.destroy)
    btn_10.grid(row=1, column=1, padx=300, pady=850)
    # scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
    # tree.configure(yscroll=scrollbar.set)
    # scrollbar.grid(row=0, column=1, sticky="ns")



# def settings():
window = Tk()
window.title('Добро пожаловать!')
window.geometry('1200x900')
main_frame = Frame(window)
main_frame.pack()
top_frame = Frame(main_frame)
top_frame.pack(side=TOP)

btn_0 = Label(top_frame, text='С чего начнем?', bg='white', fg='black', font=('Times New Roman', 35))
btn_0.grid(row=1, column=0, sticky=W, padx=380, pady=80)
btn_1 = Button(top_frame, text='Выбор сложности', bg='white', fg='black', font=('Times New Roman', 35),
               command=difficulty_selection)
btn_1.grid(row=2, column=0, sticky=W, padx=350, pady=0)
btn_2 = Button(top_frame, text='Таблица лидеров', bg='white', fg='black', font=('Times New Roman', 35),
               command=leaderboard)
btn_2.grid(row=3, column=0, sticky=W, padx=353, pady=0)
btn_3 = Button(top_frame, text='Правила игры', bg='white', fg='black', font=('Times New Roman', 35),
               command=game_rules)
btn_3.grid(row=4, column=0, sticky=W, padx=400, pady=0)
btn_4 = Button(top_frame, text='Выход', bg='white', fg='black', font=('ATimes New Roman', 35),
               command=window.destroy)
btn_4.grid(row=5, column=0, padx=400, pady=180)

window.mainloop()
