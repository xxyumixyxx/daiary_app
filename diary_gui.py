import tkinter as tk
import tkinter.ttk as ttk
import datetime as date
import calendar as calen
from tkinter import Button, messagebox
from turtle import left, right


#カレンダーの定数--週、週カラー
WEEK = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
WEEK_COLOUR = ["red","black","black","black","black","black","blue"]


def todayyyymm(arg):
    global year
    global month
    #"<"、">"ボタンを押下したときに渡される引数-- 1 or -1
    #それ以外渡される引数--0
    #' month + 0' or 'month + 1' or 'month -1' 
    month[0] += arg

    #月が1未満なら前年にする
    if month[0] < 1:
        month, year = 12, year - 1
    #月が12以上なら来年にする
    elif month[0] > 12:
        month, year = 1, year + 1
    
    #カレンダー上記に年月を表示させるラベルウィジェットを初期化
    for widget in head1.winfo_children():
        widget.destroy()

    #YYYY年MM月 と表示する(カレンダー上部)---yearとmonthを文字列にして
    # "["、"]"を削除するためにindex[1]からindex[5]を抜き出す 
    str_year_tmp = str(year)
    str_year = str_year_tmp[1:5]
    
    str_month_tmp = str(month)
    str_month = str_month_tmp[1:2]
    
    label = tk.Label(master = head1, text = str_year + "年" + str_month + "月")
    label.pack()
    
    #カレンダー本体
    YYYYMM = calen.Calendar(firstweekday=6)
    YYYYMM = YYYYMM.monthdayscalendar(year[0],month[0])
    
    #カレンダー用のラベルウィジェットを初期化
    for widget in calender_frame.winfo_children():
        widget.destroy()
    
    #行カウンター
    r = 0
    #曜日の取得--enumerate():インデックスと要素を取得する i=index x=値
    for i,x in enumerate(WEEK):
        label_week = tk.Label(
            calender_frame,
            text = x,
            font = ('',10),
            width = 3,
            #tkinter--文字の色の指定
            fg = WEEK_COLOUR[i])
        label_week.grid(row=r, column=i, pady=2)
    

    #???
    r = 1
    #日の取得
    #1週間ごと
    for week in YYYYMM:
        for i, day in enumerate(week):
            day = " " if day == 0 else day
            label_day = tk.Label(
                calender_frame,
                text = day,
                font = ('', 10),
                fg = WEEK_COLOUR[i],
                borderwidth = 1)
            #グローバル変数のyear,month,todayの値とfor文内のyear,month,dayの値が==なら線で囲む
            if(year[0], month[0], today) == (year[0], month[0], day):
                label_day["relief"] = "solid"
            #???
            """
            if check(year[0], month[0],day):
                label_day["background"] = "gray"
            """
            #Button-1 をクリックしたら選択した値がバインドされる
            #label_day.bind("<Button-1>", click)
            label_day.grid(row = r, column = i, padx = 2, pady = 1)
        r = r + 1
    
    
#メインウィンドウ
root = tk.Tk()
root.title("日記アプリ")
root.geometry("520x280")
root.resizable(0,0)

#メインフレーム
main_frame = tk.Frame(root)
calender_frame = tk.Frame(main_frame)
head1 = tk.Frame(root)

#カレンダー_ヘッド表示
head1.pack()
#カレンダー表示
main_frame.pack()

for n in range(3):
    main_frame.grid_columnconfigure(n, weight=1)

year = [date.date.today().year]
month = [date.date.today().month]
today = date.date.today().day

#左側のカレンダーのlabelやbutton
label = tk.Label(main_frame, font=('', 10))
#前月へのボタン--todayyyymmの引数に -1 を渡す
button_1 = tk.Button(main_frame,
                    text = "<",
                    font =("",10),
                    command = lambda:todayyyymm(-1))
button_1.grid(row = 0, column = 0, pady = 10)
#???
label.grid(row = 0, column = 1)
#次月へのボタン--todayyyymmの引数に 1 を渡す
button_2 = tk.Button(main_frame,
                    text = ">",
                    font =("",10),
                    command = lambda:todayyyymm(1))
button_2.grid(row = 0, column = 2)
#カレンダーの位置
calender_frame.grid(row=1, column=0, columnspan=3)

#ボタンを表示
button_1.pack
button_2.pack



#カレンダーの呼び出し
todayyyymm(0)





#上記で記述した通りに表示し続ける
root.mainloop()