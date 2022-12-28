from selenium.webdriver.common.by import By
from selenium import webdriver
from tkinter import *
import tkinter.ttk

tk = Tk()
tk.title("Python Crawl")
tk.geometry("540x500+100+100")

brower = webdriver.Chrome("/Users/duhongkim/Desktop/vscode/chromedriver")
brower.get("https://naver.com")


def get_kospi():
    global btn1_flag
    global btn2_flag

    if (btn1_flag):
        brower.find_element(By.ID, "query").click()
        brower.find_element(By.ID, "query").send_keys("코스피")
        brower.find_element(By.ID, "search_btn").click()
        kospi = brower.find_element(By.CLASS_NAME, "spt_tlt").text
        label["text"] = kospi
        btn1_flag = False
        btn2_flag = True
        brower.back()


def get_kosdaq():
    global btn1_flag
    global btn2_flag

    if (btn2_flag):
        brower.find_element(By.ID, "query").click()
        brower.find_element(By.ID, "query").send_keys("코스닥")
        brower.find_element(By.ID, "search_btn").click()
        kosdaq = brower.find_element(By.CLASS_NAME, "spt_tlt").text
        label["text"] = kosdaq
        btn1_flag = True
        btn2_flag = False
        brower.back()


def get_rate():
    global btn3_flag
    if (btn3_flag):
        print(1)
        brower.find_element(By.ID, "query").click()
        brower.find_element(By.ID, "query").send_keys("환율")
        brower.find_element(By.ID, "search_btn").click()
        rate = brower.find_element(
            By.CLASS_NAME, "rate_table_bx").text[18:].split("%")
        # label["text"] = rate
        rate_list = []
        all_list = []
        for i in rate:
            rate_list = i.split("\n")
            all_list.append(rate_list)
        for i in all_list:
            if (len(i) > 4):
                treeview.insert("", 'end', text=i[1], values=i[2:3])
        treeview.pack(pady=30)
        btn3_flag = False
        brower.back()


button = Button(tk, text="현재의 코스피 지수", command=get_kospi)
button.pack()

button = Button(tk, text="현재의 코스닥 지수", command=get_kosdaq)
button.pack()

label = Label(tk, font=20)
label.pack(anchor=CENTER, pady=20)

button = Button(tk, text="현재의 환율", command=get_rate)
button.pack()
# label = Label(tk, font=20)
# label.pack()

treeview = tkinter.ttk.Treeview(
    tk, columns=["one"], displaycolumns=["one"])

# 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
treeview.column("#0")
treeview.heading("#0", text="country", anchor="center")

treeview.column("#1")
treeview.heading("one", text="Price", anchor="center")

btn1_flag = True
btn2_flag = True
btn3_flag = True

tk.mainloop()
