import xml.etree.ElementTree as eT
import tkinter as tk
from tkinter.filedialog import askopenfilename


def open_file():
    global filepath
    filepath = askopenfilename(
        filetypes=[("xml", "*.xml")]
    )
    label['text'] = label_text + filepath


def convert():
    global filepath
    file_json = filepath[:-3] + 'json'
    # Создаем пары соответствия названий xml-json
    dict0 = {'BARCODE': '"barcode":', 'PRICE': '"price":',
             'NAME': ',"name":"', 'PLU': '","code":'}
    prefix = '{"baseVer":"0.4","base":['
    suffix = ']}'
    item = ''
    item0 = ['{"taxCode":6,"section":1,', ',"partsCount":0,',
             ',"undivided":true,"partPrice":0,"measureUnit":0,"typeCode":1},']
    root_node = eT.parse(filepath).getroot()
    f = open(file_json, 'w+')
    f.truncate(0)
    f.write(prefix)
    for tag in root_node.findall('WARES/WARE'):
        item += item0[0]
        for i in dict0.keys():
            if i == 'PRICE':
                item += dict0[i] + str(int(tag.get(i)) * 100)
                # цена в xml в рублях, в json в копейках
                continue
            item += dict0[i] + tag.get(i)
            if i == 'BARCODE':
                item += item0[1]
        item += item0[2]
        f.write(item)
        item = ''
    # удаляем лишнюю запятую в конце
    f.seek(f.tell() - 1)
    f.truncate()
    f.write(suffix)
    f.close()
    # перекодируем в utf8
    f = open(file_json, 'rb+')
    item = f.read()
    item = item.decode('cp1251').encode('utf8')
    f.seek(0)
    f.truncate()
    f.write(item)
    f.close()
    label['text'] = 'Done!'
    return


filepath = ''
label_text = 'You file is: '
window = tk.Tk()
window.title("xml-to-json converter")
btn_open = tk.Button(text="Выбрать xml-файл", command=open_file)
btn_open.pack()
label = tk.Label(text=label_text, width=100, height=2)
label.pack()
btn_conv = tk.Button(text="Convert", command=convert)
btn_conv.pack()
window.mainloop()
