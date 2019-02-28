import xml.etree.ElementTree as ET
xml_path = "pain001sam.xml"             # pain.001 XML File path on local downloaded from SFTP Server SEND dir
tree = ET.parse(xml_path)               # Parse pain.001 XML File
ET.register_namespace('', 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.03') # for omit XML Name Space Prefix from Output XML file(pain.002)
root = tree.getroot()                   # XML root set
ns = {'1': 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.03'} # Define dict as ISO20022 XML Default NameSpace This is etree.ElementTree specific methodlogy for default namespace 
Ref_Xpath = ".//1:CstmrCdtTrfInitn/1:PmtInf/1:CdtTrfTxInf/1:RmtInf/1:Strd/1:Invcee/1:CtctDtls/1:Othr" # Search Xpath for pain.001-pain.002 matching reference tag 
for i in root.findall(Ref_Xpath, ns):
    print(i.tag, i.text)