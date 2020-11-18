import requests
import urllib


def get_maxPrice_item(url, parameter):
    parameter.update(sort='-itemPrice')
    response = requests.get(url, parameter)
    result = response.json()
    item = result["Items"][0]["Item"]
    return item

def get_minPrice_item(url, parameter):
    parameter.update(sort='+itemPrice')
    response = requests.get(url, parameter)
    result = response.json()
    item = result["Items"][0]["Item"]
    return item


def main():
    keyword = input("検索ワードを入力してください: ")
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    APP_ID = "1019079537947262807"
    parameter = {
        "format"    : "json",
        "keyword"   : keyword,
        "applicationId" :   [APP_ID],
        "hits"  :   1
        }
    print(get_maxPrice_item(url, parameter))
    print(get_minPrice_item(url, parameter))


main()
