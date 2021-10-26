import xml.etree.ElementTree as ET
import pandas as pd

def intr_docs(xml_doc,attribute):
    attr = xml_doc.attrib
    
    for xml in xml_doc.iter(attribute):
        doc_dict = attr.copy()
        doc_dict.update(xml.attrib)
        doc_dict['data'] = xml.text

        yield doc_dict

etree = ET.parse('./Doc/example.xml')
list_of_connections = etree.getroot()
list_of_conn = list_of_connections.iter('conn')
for i in list_of_conn:
    list_of_signals = i.iter('fld')
    counter = 0
    for j in list_of_signals:
        list_of_enumerative = j.iter('cp')
        for k in list_of_enumerative:
            print(k.attrib)
            counter = counter + 1
            if counter == 10:
                break

        
# doc_df = pd.DataFrame(list(intr_docs(etree.getroot())))
# print(doc_df)