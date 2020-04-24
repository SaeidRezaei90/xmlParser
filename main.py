import socket
import ssl
import urllib.request
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

####### Parse an xml data #####
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

# Check if xml data is correct
try:
  #parse the xml document
  stuff = ET.fromstring(xmldata)
except:
  print("The XML data is not correct")
  quit()

print('#'*10, 'The XML includes followind information', '#'*10,'\n')

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

#Extract the data in items
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
print()

######### Writing information from url #######
txturl = 'http://data.pr4e.org/romeo.txt'
httpurl = 'http://www.dr-chuck.com'
httpsurl = 'https://www.si.umich.edu'

###Write a txt url
print('#'*10, 'Text file in', txturl, ' is...', '#'*10,'\n')
try:
# open an url and return the data as a file
  urlfile = urllib.request.urlopen(txturl)
except:
  print('the url is not found')
  quit()
  
print(urlfile.read().decode())

#parse an https page and extract some information

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
# open an url and return the data as a file
  html = urllib.request.urlopen(httpsurl, context=ctx).read()
except:
  print('the https url is not found or couldn\'t to parse correctly')
  quit()

soup = BeautifulSoup(html, 'html.parser')
#find all 'a' tags
tags = soup('a')
if len(tags)<1:
  print('There is no href in this page')
  quit()
if len(tags)==1:
  print('#'*10, 'The href for', httpsurl, 'is...', '#'*10,'\n')
else:
  print('#'*10, 'The hrefs for', httpsurl, 'are...', '#'*10,'\n')
#print all href in 'a' tags
for tag in tags:
  print('href:', tag.get('href'))
print()


###### Read a url using Socket ######
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysocket.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt #HTTP/1.1\n\n'.encode()
#mysocket.send(cmd)

#while True:
 #   data = mysocket.recv(512)
 #   print(data)
 #   if len(data) < 1:
 #       break
 #   print(data.decode())

#mysocket.close()