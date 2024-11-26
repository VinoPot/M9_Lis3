import tkinter as tk
from tkinter import ttk
import requests


def fetch_exchange_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def update_currency_options():
    rates_data = fetch_exchange_rates()
    if rates_data:
        currency_codes = list(rates_data['rates'].keys())
        base_currency1_combobox['values'] = currency_codes
        base_currency2_combobox['values'] = currency_codes
        target_currency_combobox['values'] = currency_codes


def exchange():
    rates_data = fetch_exchange_rates()
    if rates_data:
        base_currency1 = base_currency1_var.get()
        base_currency2 = base_currency2_var.get()
        target_currency = target_currency_var.get()

        if base_currency1 in rates_data['rates'] and target_currency in rates_data['rates']:
            exchange_rate1 = rates_data['rates'][target_currency] / rates_data['rates'][base_currency1]
            result1_var.set(f'1 {base_currency1} = {exchange_rate1:.4f} {target_currency}')
        else:
            result1_var.set('Invalid currency selection for Base Currency 1')

        if base_currency2 in rates_data['rates'] and target_currency in rates_data['rates']:
            exchange_rate2 = rates_data['rates'][target_currency] / rates_data['rates'][base_currency2]
            result2_var.set(f'1 {base_currency2} = {exchange_rate2:.4f} {target_currency}')
        else:
            result2_var.set('Invalid currency selection for Base Currency 2')
    else:
        result1_var.set('Error fetching data')
        result2_var.set('Error fetching data')


# создание главного окна
root = tk.Tk()
root.title("Конвертор курса валют")

# переменные
base_currency1_var = tk.StringVar(value='USD')
base_currency2_var = tk.StringVar(value='EUR')
target_currency_var = tk.StringVar(value='RUB')
result1_var = tk.StringVar()
result2_var = tk.StringVar()

# создание виджетов
base_currency1_label = ttk.Label(root, text="Базовая валюта 1:")
base_currency1_label.grid(column=0, row=0, padx=5, pady=5)

base_currency1_combobox = ttk.Combobox(root, textvariable=base_currency1_var)
base_currency1_combobox.grid(column=1, row=0, padx=5, pady=5)

base_currency2_label = ttk.Label(root, text="Базовая валюта 2:")
base_currency2_label.grid(column=0, row=1, padx=5, pady=5)

base_currency2_combobox = ttk.Combobox(root, textvariable=base_currency2_var)
base_currency2_combobox.grid(column=1, row=1, padx=5, pady=5)

target_currency_label = ttk.Label(root, text="Целевая валюта:")
target_currency_label.grid(column=0, row=2, padx=5, pady=5)

target_currency_combobox = ttk.Combobox(root, textvariable=target_currency_var)
target_currency_combobox.grid(column=1, row=2, padx=5, pady=5)

exchange_button = ttk.Button(root, text="Конвертировать", command=exchange)
exchange_button.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

update_button = ttk.Button(root, text="Обновить валюты", command=update_currency_options)
update_button.grid(column=0, row=4, columnspan=2, padx=5, pady=5)

result1_label = ttk.Label(root, textvariable=result1_var)
result1_label.grid(column=0, row=5, columnspan=2, padx=5, pady=5)

result2_label = ttk.Label(root, textvariable=result2_var)
result2_label.grid(column=0, row=6, columnspan=2, padx=5, pady=5)

# Инициализация списков валют
update_currency_options()

root.mainloop()