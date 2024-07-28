import tkinter as tk

# Создание главного окна:
root = tk.Tk()  # Основное окно
root.title("Кликер Баксов $")  # Надпись в топе окна
root.geometry("500x500")  # Размер окна X*Y
root.resizable(False, False)  # Запрещение изменения окна по X и Y
root.configure(bg="#d1ddde")  # Фон окна
balance = 0  # Cчётчик баланса
click_price = 1  # Начальная цена клика
boost_price = 50  # Начальная цена буста клика


# Обновление кнопок
def btns_update():
    global balance, click_price, boost_price
    label1["text"] = "Balance: " + str(balance) + " $"
    btn1["text"] = "Click + " + str(click_price) + "$"
    btn2["text"] = "Boost Click +" + str(click_price) + "$ = " + str(boost_price)
    if balance < boost_price:
        btn2["state"] = "disabled"
    if balance >= boost_price:
        btn2["state"] = "normal"
    root.update()


def nplus():
    global balance
    balance += click_price
    label1["text"] = "Balance: " + str(balance) + " $"
    if balance >= boost_price:
        btn2["state"] = "normal"


def click_boost():
    global balance, click_price, boost_price
    if balance >= boost_price:
        balance -= boost_price
        click_price = click_price * 2
        boost_price = boost_price * 2
        btns_update()


# Инициализация формы
label1 = tk.Label(root, text="Balance: " + str(balance) + " $", font="Helvetica 50", background="#d1ddde")
btn1 = tk.Button(text="Click + " + str(click_price) + "$", background="#75a9fa", foreground="#fff",
                 padx="50", pady="10", font="16", command=nplus)
btn2 = tk.Button(text="Boost Click +" + str(click_price) + "$ = " + str(boost_price), background="#75a9fa",
                 foreground="#fff", padx="50", pady="10", font="16", command=click_boost, state="disabled")
label1.pack()
btn1.pack()
btn2.pack()
root.mainloop()
