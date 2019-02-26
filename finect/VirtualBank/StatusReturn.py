# -*- coding: utf-8 -*-
from time import sleep
import urllib.request
import urllib.parse
params = {"zn":1030000}
p = urllib.parse.urlencode(params)
url = 'http://zip.cgis.biz/xml/zip.php?' + p

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    xml_string = response.read()
    
print(xml_string)
import xml.etree.ElementTree as ET

root = ET.fromstring(xml_string)

for child in root:
    print(child.tag, child.attrib)
# ADDRESS_valueタグ配下のvalueタグをすべて選択します
for i in root.findall('./ADDRESS_value/value'):
    print(i.attrib)
try:
    while True:
# ここに処理追加
# SENDフォルダにファイル有無確認する
# SENDフォルダのファイル名リストを取得する
# 返却ステータスファイルを作成する
# 返却ステータスファイルのファイル名をオリジナルファイル名に固定値をつけたものにする
# RECVフォルダにステータスファイルを設置する
        sleep(0.1)

except KeyboardInterrupt:
    pass