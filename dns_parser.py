import json
from bs4 import BeautifulSoup
import lxml
import requests

pharms_list = []

for num in range(0, 288, 7):

    url = f"http://gomelpharm.by/aptekas/?curPos={num}"

    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, "lxml")
    all_pharmacies = soup.find_all("tr", class_="ph-row")

    for pharm in all_pharmacies:
        pharm_name = pharm.find("div", class_="tit").text
        pharm_address = pharm.find(class_="td2").find("p").text
        try:
            pharm_phone = pharm.find("div", class_="phone").text
        except Exception:
            pharm_phone = "Нет телефона"
        pharm_schedule = pharm.find(class_="td2").find_all("p")[1].text
        try:
            pharm_cooking = pharm.find(class_="it1 production").text
        except Exception:
            pharm_cooking = "Непроизводственная аптека"


        pharm_data = {
            "Название аптеки": pharm_name.strip(),
            "Адрес аптеки": pharm_address,
            "Режим работы": pharm_schedule,
            "Телефон": pharm_phone,
            "Тип аптеки": pharm_cooking
        }

        pharms_list.append(pharm_data)



    with open("pharmacy.json", "w", encoding="utf-8") as file:
        json.dump(pharms_list, file, indent=4, ensure_ascii=False)
