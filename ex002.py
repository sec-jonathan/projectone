from tkinter import *
from functools import partial


def bt1_click(boato):
    print('botão1')


def bt2_click(boato):
    print('botão2')


# comandos basicos da janela
janela = Tk()
janela.title('login')
janela['bg'] = '#011e4c'
janela.geometry('800x610+100+100')
janela.wm_iconbitmap('jjj.ico')

# botões
bt1 = Button(janela, width=20, text='confirm')
bt1['command'] = partial(bt1_click, bt1)
bt1['bg'] = 'white'
bt1.place(x=900, y=250)


bt2 = Button(janela, width=20, text='cancel')
bt2['command'] = partial(bt2_click, bt2)
bt2.place(x=900, y=300)


top = Frame(janela,  width=1330, height=100, bd=9, relief='raise')
top.pack(side=TOP)
top.configure(bg='#1e0530')


left = Frame(janela, width=950, height=800, bd=9, relief='raise')
left.pack(side=LEFT)
left.configure(bg='#300251')





#caixa de entrada
ed1 = Entry(janela)
ed1.place(x=950, y=60)
ed2 = Entry(janela)
ed2.place(x=1130, y=60)

# area de Label
Label(janela)

lb = Label(janela, text='login', bg=['white'])
lb.place(x=900, y=25)

lb = Label(janela, text='Email', bg=['white'])
lb.place(x=950, y=35)

lb = Label(janela, text='Senha', bg=['white'])
lb.place(x=1130, y=35)


janela.geometry('1330x690+10+5')


janela.mainloop()
