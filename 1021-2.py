import tkinter as tk
import math

# === 計算功能 ===
def calculate():
    try:
        expr = entry.get()
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        label_result.config(text=f"＝ {result}", fg="#2e7d32")
    except Exception as e:
        label_result.config(text=f"錯誤：{e}", fg="#c62828")

def clear():
    entry.delete(0, tk.END)
    label_result.config(text="＝", fg="#333333")

def on_click(text):
    if text == "=":
        calculate()
    elif text == "C":
        clear()
    else:
        entry.insert(tk.END, text)

# === 主視窗設定 ===
root = tk.Tk()
root.title("🧮 高質感計算器")
root.geometry("340x640")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

# === 輸入框區 ===
entry = tk.Entry(root, font=("Segoe UI", 20), width=20, justify="right",
                 bg="#ffffff", bd=0, relief="flat", highlightthickness=1, highlightbackground="#cccccc")
entry.pack(pady=20, ipady=8)

# === 結果顯示 ===
label_result = tk.Label(root, text="＝", font=("Segoe UI", 18), bg="#f2f2f2", fg="#333333")
label_result.pack(anchor="e", padx=20)

# === 按鈕設定 ===
frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=15)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "(", ")"],
    ["+", "sin", "cos", "sqrt"],
    ["log", "exp", "C", "="]
]

button_style = {
    "font": ("Segoe UI", 14, "bold"),
    "width": 6,
    "height": 2,
    "bd": 0,
    "relief": "flat",
    "activebackground": "#dfe6e9",
    "fg": "#333333"
}

# === 建立按鈕 ===
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        # 根據按鈕類型指定顏色
        if char == "=":
            color = "#81c784"  # 綠色
        elif char in ["+", "-", "*", "/"]:
            color = "#aed581"  # 淺綠
        elif char == "C":
            color = "#ef9a9a"  # 紅色
        elif char in ["sin", "cos", "sqrt", "log", "exp"]:
            color = "#bbdefb"  # 淺藍
        else:
            color = "#ffffff"  # 預設白色

        btn = tk.Button(frame, text=char, bg=color, **button_style,
                        command=lambda t=char: on_click(t))
        btn.grid(row=r, column=c, padx=5, pady=5)

# === 啟動主迴圈 ===
root.mainloop()
