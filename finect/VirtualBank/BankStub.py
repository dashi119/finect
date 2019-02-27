xml_path = "pain001sam.xml"
# f = open(xml_path)

import xml.etree.ElementTree as ET

tree = ET.parse(xml_path)
ET.register_namespace('', 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.03')
root = tree.getroot()
ns = "{urn:iso:std:iso:20022:tech:xsd:pain.001.001.03}"
# for child in root:
#     print(child.tag, child.attrib)
# ADDRESS_valueタグ配下のvalueタグをすべて選択します
#Ref_Xpath = "." + ns + "CstmrCdtTrfInitn/" + ns + "PmtInf/" + ns + "CdtTrfTxInf/" + ns + "RmtInf/" + ns + "Strd/" + ns + "Invcee/" + ns + "CtctDtls/" + ns + "Othr"
Ref_Xpath = ".hoge:CstmrCdtTrfInitn/hoge:PmtInf/hoge:CdtTrfTxInf/hoge:Strd/hoge:Invcee/hoge:CtctDtls/hoge:Othr"
#print(Ref_Xpath)
for i in root.findall(Ref_Xpath, namespaces={"hoge" : "urn:iso:std:iso:20022:tech:xsd:pain.001.001.03"}):
    print(i.tag, i.text)