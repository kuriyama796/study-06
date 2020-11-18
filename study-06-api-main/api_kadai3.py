import requests
import urllib
import pandas as pd


def get_api(url, parameter):
    # データフレーム作成
    df = pd.DataFrame(index=[], columns=['rank','itemName'] )
    response = requests.get(url, parameter)
    result = response.json()
    
    for i in result["Items"]:
        item = i["Item"]
        tmp_se = pd.Series( [str(item["rank"]) + "位", item["itemName"]], index=df.columns)
        df = df.append( tmp_se, ignore_index = True )

    df.to_csv("ranking.csv", index=True, encoding="utf-8")


def main():
    genre_id = input("genreIdを入力してください: ")
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
    APP_ID = "1019079537947262807"
    parameter = {
        "format"    : "json",
        "genreId"   : genre_id,
        "applicationId" :   [APP_ID]
        }
    get_api(url, parameter)


main()
