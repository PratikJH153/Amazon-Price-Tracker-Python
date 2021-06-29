from bs4 import BeautifulSoup
import requests
import smtplib

TARGET_PRICE = 400

# my_email = "pratik.jh2017@gmail.com"
# my_pass = "aklsjdfklj"

# smtp = smtplib.SMTP("smtp.gmail.com")
# smtp.starttls()
# smtp.login(user=my_email, password=my_pass)

response = requests.get("https://www.amazon.in/iDream-Programming-Language-Software-Stickers/dp/B082GZP8DQ/ref=sr_1_3?dchild=1&keywords=stickers+programming&qid=1624544796&sr=8-3",
    headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36", 'Accept-Language':"en-US,en;q=0.9"
})
response.raise_for_status()

content = response.text

soup = BeautifulSoup(content, "lxml")
print(soup.title.getText())

price = float(soup.select_one("#priceblock_ourprice").getText().split()[1])
print(price)

if price <= TARGET_PRICE:
    print("Subject:Amazon Price Tracker, Stickers\n\nThe price of the product you have added in your list has been dropped to your Target price, go and check out the product.")
# smtp.sendmail(
# from_addr=my_email,
# to_addrs=my_email,
# msg="Subject:Amazon Price Tracker, Stickers\n\n The price of the product you have added in your list has been dropped to your Target price, go and check out the product")

