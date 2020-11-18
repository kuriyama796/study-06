import requests
import urllib


def get_api(url, parameter):
    # 商品情報をリストで取得
    item_list = []
    response = requests.get(url, parameter)
    result = response.json()
    print(result)

    # resultから必要な情報を抜き出したdictを作る
    item_key = ['itemName', 'itemPrice']

    for i in range(0, len(result['Items'])):
        tmp_item = {}
        item = result['Items'][i]['Item']
        for key, value in item.items():
            if key in item_key:
                tmp_item[key] = value
        item_list.append(tmp_item.copy())

    return item_list


def main():
    keyword = input("検索ワードを入力してください: ")
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    APP_ID = "1019079537947262807"
    parameter = {
        "format"    : "json",
        "keyword"   : keyword,
        "applicationId" :   [APP_ID]
        }
    print(get_api(url, parameter))


main()
