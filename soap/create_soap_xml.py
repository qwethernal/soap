import requests

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
 
payload = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <FullCountryInfoAllCountries xmlns="http://www.oorsprong.org/websamples.countryinfo">
    </FullCountryInfoAllCountries>
  </soap:Body>
</soap:Envelope>"""
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}
response = requests.request("POST", url, headers=headers, data=payload)
 
f = open("soap.xml", "a")
f.write(response.text)
f.close()
print(response.text)
print(response)
