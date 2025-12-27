import tkinter as tk
from tkinter import ttk
import requests

API_KEY="159f2524ca2ff4ba607dc1b8"

def get_rates(base="INR"):
    api_key="2f0bd95aeb4113bf050e6b11"
    url=f"https://v6.exchangerate-api.com/v6/2f0bd95aeb4113bf050e6b11/latest/INR"
    response=requests.get(url)
    data=response.json()
    if data["result"]=="success":
        return data["conversion_rates"]
    else:
        return None
def convert():
    amount=entry.get()
    if amount=="":
        result_label.config(text="Please enter the amount",fg="red")
        return
    
    try:
        amount=float(amount)
        from_cur=from_currency.get()
        to_cur=to_currency.get()
        
        rates=get_rates(from_cur)
        if rates:
            rate=rates[to_cur]
            converted=amount*rate
            result_label.config(text=f"{amount}{from_cur}={converted:.2f}{to_cur}",fg="green")
        else:
            result_label.config(text="Rate not found",fg="red")
    except ValueError:
        result_label.config(text="Invalid number",fg="red")
        
        
root=tk.Tk()
root.title("Currency converter")
root.geometry("420x360")

tk.Label(root, text="Enter Amount",font=("Arial",12,"bold")).pack(pady=(15,5))

tk.Label(root, text="Amount",font=("Arial",12)).pack(pady=5)
entry=tk.Entry(root,font=("Arial",12))
entry.pack(pady=5)

entry.bind('<Return>',lambda event:convert())

tk.Label(root, text="From Currency",font=("Arial",12)).pack(pady=5)
from_currency=tk.StringVar(value="INR")
from_menu=ttk.Combobox(root, textvariable=from_currency, values=["INR","USD","EUR","GBP","JPY","AUD","CAD"],state="readonly")
from_menu.pack(pady=5)

tk.Label(root, text="To Currency", font=("Arial",12)).pack(pady=5)
to_currency=tk.StringVar(value="USD")
to_menu=ttk.Combobox(root, textvariable=to_currency,values=["INR","USD","EUR","GBP","JPY","AUD","CAD"],state="readonly")
to_menu.pack(pady=5)

tk.Button(root, text="Convert", command=convert).pack(pady=15)
result_label=tk.Label(root, text="", font=("Arial",13,"bold"))
result_label.pack(pady=10)


root.mainloop()