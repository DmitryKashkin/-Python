# import json
import xml.etree.ElementTree as ET

sample_json = ['"taxCode"', '"section"', '"barcode"', '"partsCount"',
               '"price"', '"name"', '"code"', '"undivided"', '"partPrice"',
               '"measureUnit"', '"typeCode"']
sample_xml = ['BARCODE', 'PRICE', 'NAME', 'PLU']
dict0 = {'BARCODE': '"barcode":', 'PRICE': '"price":',
         'NAME': ',"name":"', 'PLU': '","code":'}
prefix = '{"baseVer":"0.4","base":['
suffix = ']}'
item = ''
item0 = ['{"taxCode":6,"section":1,', ',"partsCount":0,',
         ',"undivided":true,"partPrice":0,"measureUnit":0,"typeCode":1}']
root_node = ET.parse('prazdnik.xml').getroot()
for tag in root_node.findall('WARES/WARE'):
    item += item0[0]
    for i in sample_xml:
        item += dict0[i] + tag.get(i)
        if i == 'BARCODE':
            item += item0[1]
    item += item0[2]
    print(item)
    item = ''

    #     item += str()
    #     items[sample_json[3]] =
    # plu = tag.get(sample_xml[0])
    # namt = tag.get(sample_xml[1])
    # barcode = tag.get('BARCODE')
    # if barcode is not None:
    # print(barcode)
#     items[sample_json[0]] = tax_code
# print(items.items())

# print(root_node)

# f_xml = open('prazdnik.xml')
# ff = f_xml.read(500)
# # print(ff)
# for i in range(100):
#     ff = f_xml.readline(i)
#     # print(type(ff))
#     print(ff)


#
# f_json = open('prazdnik.json')
# ff = json.loads(f_json.read())
#
# print(type(ff))
# print(ff)
#
# f_json.close()
# f_xml.close()
