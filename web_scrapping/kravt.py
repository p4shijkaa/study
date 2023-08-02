"""
Спарсить все страниц товара сегмента корейская косметика (название, цена, производитель, рейтинг, ссылка)
"""
import json

import requests
from bs4 import BeautifulSoup

goods_list = []

for num in range(1, 16):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    url = f"https://oz.by/sseries/more1501803.html?availability=1%3B2&page={num}"

    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    all_goods = soup.find("div", class_="products__grid viewer-type-card--js-active").find_all(
        class_="products__item item product-card")

    for good in all_goods:
        good_name = good.find("div", class_="product-card__title").text
        good_price = good.find("div", class_="product-card__cost").find("strong").text
        good_firm = good.find("div", class_="product-card__subtitle").text
        good_link = good.find("a").get("href")
        try:
            good_rating = good.find("div", class_="product-card__rating").text
        except Exception:
            good_rating = "нет отзывов"

        goods_dict = {
            'Название товара': good_name.replace('\"', ""),
            'Цена товара': good_price.replace('\xa0', ' '),
            'Производитель': good_firm,
            'Рейтинг': good_rating.replace('\n', ''),
            'Ссылка': good_link
        }
        goods_list.append(goods_dict)

with open("oz_by.json", "w", encoding="utf-8") as file:
    json.dump(goods_list, file, ensure_ascii=False, indent=4)
