import urllib.request
import urllib.parse
params = {"zn":1650031}
p = urllib.parse.urlencode(params)
url = 'http://zip.cgis.biz/xml/zip.php?' + p

req = urllib.request.Request(url)
f = open('pain001sam.xml')
with urllib.request.urlopen(req) as response:
    xml_string = f.read()
#    xml_string = response.read()
    
# print(xml_string)
import xml.etree.ElementTree as ET

root = ET.fromstring(xml_string)

for child in root:
    print(child.tag, child.attrib)
# ADDRESS_valueタグ配下のvalueタグをすべて選択します
for i in root.findall('./ADDRESS_value/value'):
    print(i.attrib)