from bs4 import BeautifulSoup
import requests
import lxml
Product_url = input("Give Product URL")
Your_price = float(input("How much do want to pay"))


Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36", "Accept-Language":"en-US,en;q=0.9","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

response = requests.get(Product_url, headers=Headers)

product = response.content
# print(product)

soup = BeautifulSoup(product, "lxml")
price = soup.find("span", class_="a-price-whole").getText()
price_tag = price.replace(",", "").split()[0]


#
if float(price_tag) <= Your_price:
    print(f"you can buy it now, Current price is {price}")