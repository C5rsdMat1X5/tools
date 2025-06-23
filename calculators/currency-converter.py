from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.environ.get("API_KEY")

def conversion_rate():
    while True:
        quantity = float(input("Enter the amount to convert: "))
        coin1 = input("Enter the first currency (e.g., USD): ")
        coin2 = input("Enter the second currency (e.g., EUR): ")
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{coin1}/{coin2}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            data = data['conversion_rate']
            print(data * quantity, coin2)
            break
        else:
            print("Error:", response.status_code, "try again.")

conversion_rate()