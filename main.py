#main.py
#coding:utf-8

import requests
import csv

url = "http://ci.nii.ac.jp/books/opensearch/search?"
csvFile = open("sample.csv", encoding="utf-8")

csvDict = csv.DictReader(csvFile, delimiter=",", quotechar='"')#csvを辞書型で読み込み

result = open("result.txt","a",encoding="utf-8")#結果書き出し用ファイル準備

for row in csvDict:
    author = row["author"]
    title = row["title"]
    str = author + ", " + title + " 邦訳："

    query = {"format":"json",
             "author":author,
             "title":title,
             "lang":"jpn",
             "count":10}
    res = requests.get(url,params=query)

    if res.json()["@graph"][0]["opensearch:itemsPerPage"] != "0":#検索結果が0件でない場合
        for i in res.json()["@graph"][0]["items"]:
            str += i["dc:creator"] + "，" + i["title"] + "\n"

            result.write(str)

    else:
        str += "該当なし" + "\n"
        result.write(str)
result.close()
