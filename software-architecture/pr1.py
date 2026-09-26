import xml.etree.ElementTree as ET
xml_file = 'pr1.xml'

def print_objects():
    XMLTree = ET.parse(xml_file)
    root = XMLTree.getroot()
    print("Данные в базе:")
    for obj in root.findall('object'):
        art = obj.find('art').text
        tipe = obj.find('tipe').text
        color = obj.find('color').text
        print(f'арткул: {art}, тип: {tipe}, цвет: {color}')

def add_object(art, tipe, color):
    XMLTree = ET.parse(xml_file)
    root = XMLTree.getroot()
    new_obj = ET.Element('object')
    new_art = ET.SubElement(new_obj, 'art')
    new_art.text = art
    new_tipe = ET.SubElement(new_obj, 'tipe')
    new_tipe.text = tipe
    new_color = ET.SubElement(new_obj, 'color')
    new_color.text = color
    root.append(new_obj)
    XMLTree.write(xml_file)
    print("Добавлен новый артикул: " f"{art}")

def delete_object(art):
    XMLTree = ET.parse(xml_file)
    root = XMLTree.getroot()
    for obj in root.findall('object'):
        if obj.find('art').text == art:
            root.remove(obj)
    XMLTree.write(xml_file)
    print("Удалён артикул: " f"{art}")

print_objects()

add_object('кровать', 'домашняя', 'синяя')
add_object('стул', 'уличный', 'чёрный')
print_objects()

delete_object('стол')
print_objects()