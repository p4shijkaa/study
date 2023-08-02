import json

arr = []

with open("mat.txt", encoding="utf-8") as r:
    for word in r:
        not_mat = word.lower().split("\n")[0]
        if not_mat != "":
            arr.append(not_mat)

with open("not_mat.json", "w", encoding="utf-8") as file:
    json.dump(arr, file)