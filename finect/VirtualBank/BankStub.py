def StsRtn(pain001path):
    import xml.etree.ElementTree as ET
    import datetime
#    xml_path = "pain001sam.xml"             # pain.001 XML File path on local downloaded from SFTP Server SEND dir
    xml_path = pain001path             # pain.001 XML File path on local downloaded from SFTP Server SEND dir
    RefList = []
    try:
        tree = ET.parse(xml_path)               # Parse pain.001 XML File
        root = tree.getroot()                   # XML root set
    except:
        return
    ns = {'1': 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.03'} # Define dict as ISO20022 XML Default NameSpace This is etree.ElementTree specific methodlogy for default namespace 
    # check pain.001
    pain001_Xpath = ".//1:CstmrCdtTrfInitn/1:PmtInf" # Search Xpath for pain.001 root 
    pain001flug = root.findall(pain001_Xpath, ns)
    if not pain001flug:
        return
    # pain.001 invoicee contact details other get
    Ref_Xpath = ".//1:CstmrCdtTrfInitn/1:PmtInf/1:CdtTrfTxInf/1:RmtInf/1:Strd/1:Invcee/1:CtctDtls/1:Othr" # Search Xpath for pain.001-pain.002 matching reference tag 
    for i in root.findall(Ref_Xpath, ns):
    #    print(i.tag, i.text)
        RefList.append(i.text)
    for j in RefList:
        print(j)
    
    # pain.002.001.02 Payment Status Report XML Output
    # ET.register_namespace('', 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.02') # for omit XML Name Space Prefix from Output XML file(pain.002)
    # root Element
    Document = ET.Element('Document')
    # Document element is root set
    tree2 = ET.ElementTree(element=Document)
    CstmrPmtStsRpt = ET.SubElement(Document, 'CstmrPmtStsRpt')
    # Add Group Header 
    GrpHdr = ET.SubElement(CstmrPmtStsRpt, 'GrpHdr')
    # Add Message Identification
    MsgId = ET.SubElement(GrpHdr, 'MsgId')
    now = datetime.datetime.now()
    timestamp = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2) + str(now.hour).zfill(2) + str(now.minute).zfill(2) + str(now.second).zfill(2)
    MsgId.text = timestamp
    # Add Creation Date and Time
    CreDtTm = ET.SubElement(GrpHdr, 'CreDtTm')
    # CreDtTm.text = datetime.datetime.now().isoformat(timespec='seconds')
    CreDtTm.text = datetime.datetime.now().isoformat()
    # Add Original Group Information and Status
    OrgnlGrpInfAndSts = ET.SubElement(CstmrPmtStsRpt, 'OrgnlGrpInfAndSts')
    # Add Original Message Identification
    OrgnlMsgId = ET.SubElement(OrgnlGrpInfAndSts, 'OrgnlMsgId')
    OrgnlMsgId.text = 'ORIGINAL MESSAGE IDENTIFICATION'
    # Add Original Message Name Identification
    OrgnlMsgNmId = ET.SubElement(OrgnlGrpInfAndSts, 'OrgnlMsgNmId')
    OrgnlMsgNmId.text = 'pain.001.001.03'
    # Add Group Status (4 digits ISO20022 defined code)
    GrpSts = ET.SubElement(OrgnlGrpInfAndSts, 'GrpSts')
    GrpSts.text = 'ACCP'
    # Add Status Reason Information
    StsRsnInf = ET.SubElement(OrgnlGrpInfAndSts, 'StsRsnInf')
    # Add Reason
    Rsn = ET.SubElement(StsRsnInf, 'Rsn')
    # Add proprietary : Bank defined 7 digits codes
    Prtry = ET.SubElement(Rsn, 'Prtry')
    Prtry.text = '00-0000'  # This stub always return 00-0000(no error)
    # Add Original Payment Information and Status
    OrgnlPmtInfAndSts = ET.SubElement(CstmrPmtStsRpt, 'OrgnlPmtInfAndSts')
    # Add Original Payment Information Identification
    OrgnlPmtInfId = ET.SubElement(OrgnlPmtInfAndSts, 'OrgnlPmtInfId')
    OrgnlPmtInfId.text = 'ORIGINAL PmtInf ID'
    # Transaction Loop
    for i in RefList:
        # Add Transaction Information and Status
        TxInfAndSts = ET.SubElement(OrgnlPmtInfAndSts, 'TxInfAndSts')
        # Add Status Identification
        StsId = ET.SubElement(TxInfAndSts, 'StsId')
        StsId.text = timestamp
        # Add Original Instruction Identification
        OrgnlInstrId = ET.SubElement(TxInfAndSts, 'OrgnlInstrId')
        OrgnlInstrId.text = 'ORIGINAL TxIstruction ID'
        # Add Original End to End Identification
        OrgnlEndToEndId = ET.SubElement(TxInfAndSts, 'OrgnlEndToEndId')
        OrgnlEndToEndId.text = 'ORIGINAL EndToEnd ID'
        # Add Transaction Status
        TxSts = ET.SubElement(TxInfAndSts, 'TxSts')
        TxSts.text = 'ACCP' # This stub always returns Accpeted(no error)
        # Add Status Reason Information
        StsRsnInf2 = ET.SubElement(TxInfAndSts, 'StsRsnInf')
        # Add Reason
        Rsn2 = ET.SubElement(StsRsnInf2, 'Rsn')
        # Add proprietary : Bank defined 7 digits codes
        Prtry2 = ET.SubElement(Rsn2, 'Prtry')
        Prtry2.text = '0140000'  # This stub always return 0140000(no error)
        # Add Original Transaction Reference
        OrgnlTxRef = ET.SubElement(TxInfAndSts, 'OrgnlTxRef')
        # Add Remittance Information
        RmtInf = ET.SubElement(OrgnlTxRef, 'RmtInf')
        # Add Structured
        Strd = ET.SubElement(RmtInf, 'Strd')
        # Add Invoicee
        Invcee = ET.SubElement(Strd, 'Invcee')
        # Add Contract Details
        CtctDtls = ET.SubElement(Invcee, 'CtctDtls')
        # Add Other
        Othr = ET.SubElement(CtctDtls, 'Othr')
        Othr.text = i
    
    # pain.002出力確認標準出力
    root = tree2.getroot()
    for child in root.findall('.CstmrPmtStsRpt//'):
        print(child.tag, child.text)
    tree2.write('textpmt2.xml', encoding='utf-8')
    with open('textpmt2.xml','r') as p002:
        replacestring = p002.read()
    # replacestring = replacestring.replace('<?xml version="1.0"?>','<?xml version="1.0" encoding="UTF-8"?>')
    replacestring = replacestring.replace('<Document>','<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="urn:iso:std:iso:20022:tech:xsd:pain.002.001.03">')
    replacestring = '<?xml version="1.0" encoding="UTF-8"?>' + replacestring
    with open('textpmt2-2.xml','w') as p00202:
        p00202.write(replacestring)
    

import os
import sys
# SEND Directory polling
# User 1900000001SERVERID SEND Directory search
# path = '/home/1900000001SERVERID/sftp-root/SEND/'
path = './'
if os.path.isdir(path):
    pollablelist = os.listdir(path)
    print(pollablelist)
else:
    sys.exit()
for i in pollablelist:
    StsRtn(path + i)
