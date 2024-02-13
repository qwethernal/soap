
import xml.etree.ElementTree as ET 
import mysql.connector 
conn = mysql.connector.connect(
	user='admin2', 
	password='admin2', 
	host='localhost', 
	database='countries5') 

tree = ET.parse('soap.xml') 

data2 = tree.findall('tCountryInfo') 
c = conn.cursor() 
create_table_query = "CREATE TABLE IF NOT EXISTS country (sISOCode INT AUTO_INCREMENT PRIMARY KEY, sName VARCHAR(50), sCapitalCity VARCHAR(50), sPhoneCode INT, sContinentCode INT, sCurrencyISOCode INT)"
c.execute(create_table_query)


for i, j in zip(data2, range(1, 250)): 
	code= i.find('m:sISOCode').text 
	name = i.find('m:sName').text 
	capital = i.find('m:sCapitalCity').text
	pcode = i.find('m:sPhoneCode').text
	ccode = i.find('m:sContinentCode').text
	currency = i.find('m:sCurrencyISOCode').text
	
	db_update = """INSERT INTO country(sISOCode,sName,sCapitalCity,sPhoneCode,sContinentCode,sCurrencyISOCode) VALUES(%s,%s,%s,%s,%s,%s)"""
	data = (code,name,capital,pcode,ccode,currency)
	c.execute(db_update, data) 
	conn.commit() 
	print("stored successfully") 
	
c.close()
conn.close()