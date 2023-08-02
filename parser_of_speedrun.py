import requests
import lxml
from bs4 import BeautifulSoup
import json

# url = "https://calorizator.ru/product"
# #
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

# r = requests.get(url=url, headers=headers)
# soup = BeautifulSoup(r.text, "lxml")
# all_results = soup.find_all("ul", class_="product")
#
# all_categories_dict = {}
#
# for category in all_results:
#     category_names = category.find_all("a")
#
#     for category in category_names:
#         category_name = category.text
#         category_href = f"https://calorizator.ru/product/{category.get('href').split('/')[1]}"
#         all_categories_dict[category_name] = category_href
#
# with open("all_categories_dict.json", "w") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_categories_dict.json") as file:
    all_categories = json.load(file)


list_of_max_pages = [1, 2, 5, 1, 5, 3, 6, 7, 2, 7, 2, 6, 8, 2, 3, 1, 1, 6, 1, 2, 2, 3, 2, 1, 2, 2, 1, 1, 2, 2, 4, 4, 1, 1, 1, 1, 1]

for num in list_of_max_pages:
    for count in range(num):
        for category_name, category_href in all_categories.items():
            if count == num:
                continue
            else:
                req = requests.get(url=f"{category_href}?page={count}", headers=headers)
                src = req.text
                soup = BeautifulSoup(src, "lxml")


            try:
                table_title = soup.find(class_="views-table").find_all("td", class_="views-field views-field-title active")
            except Exception:
                table_title = None

            if table_title is not None:
                for table in table_title:
                    table_name = table.find("a").text
                    print(table_name)
            else:
                continue

        # попробовать собрать через дикт
