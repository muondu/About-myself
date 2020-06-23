import requests
from bs4 import BeautifulSoup
from termcolor import colored
from datetime import datetime

# CREATOR: Munene Muondu (me)

header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

print("Hi, I am Munene Muondu. I am currently 11 years old. I live in Kenya. When I was 8, I was introduced coding by my parents. I started with simple scratch and after 2 months. I started playing some easy coding games and then moved to basic HTML. I progressed slowly and then I reached CSS. I used HTML and CSS then I learned how to use github. After Github I went to bootstrap which I continued learning till I was 9 and a half. Then I started learning Javascript till 10 years old. Where I started with Python till now. .\n\n")

input("Press enter to continue: ")

print(colored("\nHere is a live update(in universal time(UTC)) of all the stocks in my personal stock portfolio I made:\n", "green"))

stocklist = ["AMD", "BA", "TSLA", "UBER", "BYND", "GOOG", "MSFT", "QCOM", "TWTR", "COST", "NVDA", "BOTZ", "TCEHY", "BABA", "FB"]

while True:
    for i in range(len(stocklist)):
        URL = "https://finance.yahoo.com/quote/" + stocklist[i] + "?p=" + stocklist[i]

        page = requests.get(URL, headers=header)

        soup = BeautifulSoup(page.content, 'html.parser')

        price = soup.find("div", {"class": "D(ib) Va(m) Maw(65%) Maw(60%)--tab768 Ov(h)"}).find("span")

        cleanerprice = str(list(price)).replace("['", "").replace("']", "")

        date_ = datetime.now().strftime("%b %d %Y %H:%M:%S")

        print(colored(stocklist[i], "red") + " " + colored(date_, "green") + " $" + cleanerprice)
