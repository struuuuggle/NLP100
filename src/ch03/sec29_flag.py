# -*- coding: utf-8 -*-
import json, requests
from sec28_mediawiki import remove_mediawiki

def flag():
    dict = remove_mediawiki()
    img_name = dict['国旗画像']
    url = 'https://www.mediawiki.org/w/api.php?action=query&titles=File:{}&prop=imageinfo&iiprop=url&format=json'.format(img_name)

    # APIからJSONをダウンロード
    response = requests.get(url)
    response.raise_for_status()

    # JSONデータを読み込む
    j = json.loads(response.text)
    image_info = j['query']['pages']['-1']['imageinfo']
    return image_info[0]['url']


def main():
    print(flag())

if __name__ == '__main__':
    main()
