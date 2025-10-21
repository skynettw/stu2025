# 使用者輸入算術式
expr = input("請輸入算術式，例如 3+5*2： ")

try:
    # 使用 eval 計算結果，但限制只允許數字與運算符號
    allowed_chars = "0123456789+-*/(). "
    if all(c in allowed_chars for c in expr):
        result = eval(expr)
        print(f"計算結果為：{result}")
    else:
        print("輸入中包含不允許的字元！")
except Exception as e:
    print(f"發生錯誤：{e}")



