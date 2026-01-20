from bs4 import BeautifulSoup
import smtplib
import requests
import os
from dotenv import load_dotenv
load_dotenv()
SENDER=os.getenv("SENDER")
RECIEVER=os.getenv("RECIEVER")
PW=os.getenv("APP_PW")
URL="https://www.amazon.in/dp/B0DLW427YG/?_encoding=UTF8&pf_rd_p=859234e6-2ce1-4cf0-a12c-276c3081b669&pf_rd_r=RY4TDABHVWK58B4YXNMF&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/138.0.0.0 Safari/537.36 OPR/122.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://myhttpheader.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8,es;q=0.7"
}
response=requests.get(URL,headers=headers)
data=response.text
soup=BeautifulSoup(data,"html.parser")
price = soup.find(class_="a-price-whole").get_text()
price_without_currency = price.replace(",","").strip()

price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 8500
#print(soup.prettify())
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(SENDER,PW)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=RECIEVER,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
