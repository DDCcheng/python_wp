# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import sqlite3
import tkinter as tk


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    print("Hello, World!")



def fibonacci_dp(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.
    :param n: The position in the Fibonacci sequence.
    :return: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def calculate():
    try:
        result = eval(entry.get())
        result_var.set(result)
    except Exception:
        result_var.set("错误")


root = tk.Tk()
root.title("简单计算器")

entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=('Arial', 16))
result_label.grid(row=1, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


def on_click(char):
    if char == '=':
        calculate()
    else:
        entry.insert(tk.END, char)


row, col = 2, 0
for b in buttons:
    action = lambda x=b: on_click(x)
    tk.Button(root, text=b, width=5, height=2, command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='清空', width=22, height=2, command=lambda: entry.delete(0, tk.END)).grid(row=row, column=0, columnspan=4)

root.mainloop()
