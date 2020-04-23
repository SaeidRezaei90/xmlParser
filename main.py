import xml.etree.ElementTree as ET

xmldata = '''
<shiporder orderid="889923"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="shiporder.xsd">
  <orderperson>John Smith</orderperson>
  <shipto>
    <name>Ola Nordmann</name>
    <address>Langgt 23</address>
    <city>4000 Stavanger</city>
    <country>Norway</country>
  </shipto>
  <item>
    <title>Empire Burlesque</title>
    <note>Special Edition</note>
    <quantity>1</quantity>
    <price>10.90</price>
  </item>
  <item>
    <title>Hide your heart</title>
    <quantity>1</quantity>
    <price>9.90</price>
  </item>
</shiporder>
            '''

stuff = ET.fromstring(xmldata)
print('Order id  :', stuff.get('orderid'))
print('order person : ', stuff.find('orderperson').text)
print()
#shipto = stuff.find('shipto')
#print('sellers name:', shipto.find('name').text)
print('Customer Address')
print('Name:', stuff.find('shipto/name').text)
print('Address:', stuff.find('shipto/address').text)
print('Country:', stuff.find('shipto/country').text)
print()

print('List of items...')
items = stuff.findall('item')
print("Number of Ordered items:", len(items))

itemnum = 1
for item in items:
  print()    
  print('Item number', itemnum)
  if item.find('title') != None :
    print("Title:", item.find('title').text)
  if item.find('note') != None:
    print("Note:", item.find('note').text)
  if item.find('quantity') != None:
    print("Quantity:", item.find('quantity').text)
  if item.find('price') != None:
    print("Price:", item.find('price').text)

  itemnum = itemnum + 1
  

