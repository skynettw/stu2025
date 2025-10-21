import gradio as gr

def loan_calculator(principal, years, annual_rate, method):
    try:
        # 將輸入轉換為數值
        P = float(principal)
        n = int(years) * 12
        r = float(annual_rate) / 100 / 12  # 月利率

        if method == "等額本息":
            # 每月還款金額公式：M = P * r * (1+r)^n / ((1+r)^n - 1)
            M = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
            result = f"📘 每月應還金額：約 NT$ {M:,.0f}"
        else:  # 等額本金
            # 每月本金固定，利息遞減
            monthly_principal = P / n
            first_month = monthly_principal + P * r
            last_month = monthly_principal + monthly_principal * r
            avg = (first_month + last_month) / 2
            result = (
                f"📗 首月應還金額：約 NT$ {first_month:,.0f}\n"
                f"📙 最後一期：約 NT$ {last_month:,.0f}\n"
                f"📘 平均每月：約 NT$ {avg:,.0f}"
            )
        return result
    except Exception as e:
        return f"❌ 輸入有誤：{e}"

# 建立 Gradio 介面
with gr.Blocks(title="貸款每月還款試算") as demo:
    gr.Markdown("## 💰 貸款每月還款試算")
    gr.Markdown("輸入貸款條件後，選擇還款方式，按下按鈕即可試算每月應繳金額。")

    with gr.Row():
        loan = gr.Number(label="貸款金額（NT$）", value=1000000)
        years = gr.Slider(1, 30, value=20, step=1, label="貸款年限（年）")
        rate = gr.Number(label="年利率（%）", value=2.5)

    method = gr.Radio(["等額本息", "等額本金"], label="還款方式", value="等額本息")

    btn = gr.Button("計算")
    output = gr.Textbox(label="結果", lines=3)

    btn.click(fn=loan_calculator, inputs=[loan, years, rate, method], outputs=output)

demo.launch(share=True)
