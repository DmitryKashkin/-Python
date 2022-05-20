import xml.etree.ElementTree as eT
sample_xml = ['BARCODE', 'PRICE', 'NAME', 'PLU']
dict0 = {'BARCODE': '"barcode":', 'PRICE': '"price":',
         'NAME': ',"name":"', 'PLU': '","code":'}
prefix = '{"baseVer":"0.4","base":['
suffix = ']}'
item = ''
item0 = ['{"taxCode":6,"section":1,', ',"partsCount":0,',
         ',"undivided":true,"partPrice":0,"measureUnit":0,"typeCode":1},']
root_node = eT.parse('prazdnik.xml').getroot()
f = open('prazdnik.json', 'w+')
f.truncate(0)
f.write(prefix)
for tag in root_node.findall('WARES/WARE'):
    item += item0[0]
    for i in sample_xml:
        if i == 'PRICE':
            item += dict0[i] + str(int(tag.get(i)) * 100)
            continue
        item += dict0[i] + tag.get(i)
        if i == 'BARCODE':
            item += item0[1]
    item += item0[2]
    f.write(item)
    item = ''
f.seek(f.tell()-1)
f.truncate()
f.write(suffix)
f.close()
f = open('prazdnik.json', 'rb+')
item = f.read()
item = item.decode('cp1251').encode('utf8')
f.seek(0)
f.truncate()
f.write(item)
f.close()
