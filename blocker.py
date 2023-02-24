# importing required liberary
from tkinter import *
# creating a window
window = Tk()
window.geometry('650x500')
window.minsize(650, 500)
window.maxsize(650, 500)
window.title(" DataFlair Website Blocker")

heading = Label(window, text='Website Blocker', font='arial')
heading.pack()

host_path = 'D:\Blocked'
ip_address = '192.168.1.105'

label1 = Label(window, text='Enter Website :', font='arial 13 bold')
label1.place(x=5, y=60)

enter_Website = Text(window, font='arial', height='2', width='40')
enter_Website.place(x=140, y=60)


def Blocker():
    website_lists = enter_Website.get(1.0, END)
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as f:
        file_content = f.read()
        for web in Website:
            if web in file_content:
                display = Label(window, text='Already Blocked', font='arial')
                display.place(x=200, y=200)
                pass
            else:
                f.write(ip_address + " " + web + '\n')
                Label(window, text="Blocked", font='arial').place(x=230, y=200)


def Unblock():
    website_lists = enter_Website.get(1.0, END)
    Website = list(website_lists.split(","))
    with open(host_path, 'r+') as host:
        file_content = host.readlines()
    for web in Website:
        if web in website_lists:
            with open(host_path, 'r+') as file:
                for line in file_content:
                    if line.strip(',') != website_lists:
                        file.write(line)
                        Label(window, text="UnBlocked",
                              font='arial').place(x=350, y=200)
                        pass
                    else:
                        display = Label(
                            window, text='Already UnBlocked', font='arial')
                        display.place(x=350, y=200)


block_button = Button(window, text='Block', font='arial', pady=5,
                      command=Blocker, width=6, bg='royal blue1', activebackground='grey')
block_button.place(x=230, y=150)

unblock_button = Button(window, text='UnBlock', font='arial', pady=5,
                        command=Unblock, width=6, bg='royal blue1', activebackground='grey')
unblock_button.place(x=350, y=150)
window.mainloop()
