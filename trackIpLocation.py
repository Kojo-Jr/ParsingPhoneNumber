import geo

ip = geo.getIP()
print(ip)

country = geo.getCountry(ip, 'plain')
print(country)

country = geo.getCountry(ip, 'json')
print(country)

geoData = geo.getGeoData(ip)
print(geoData)

ptrData = geo.getPTR(ip)
print(ptrData)

geo.showIpDetails('41.218.194.106')

geo.showCountryDetails('41.218.194.106')