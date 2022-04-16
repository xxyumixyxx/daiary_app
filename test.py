
from calendar import month
import datetime as date

a = [date.date.today().year] * 2
b = [date.date.today().month] * 2

def a(arg):
    global a
    global b
    a[0] += arg
    
    if a[0] < 1:
        print("1より小さいです")
    elif a[0] > 12:
        print("12以上です")
a(0)

"""
print("こんにちは、これからpython頑張ろうね！")
name = input("何か入力してね")
print(name + " ⇒繰り返したよ")
"""


