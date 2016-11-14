import pygeoip

gpath = input('Enter path of GeoLiteCity database: ')	
gi = pygeoip.GeoIP(gpath)

def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    country = rec['country_name']
    longi = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt + 'Geo-located. '
    print '[+] '+str(city)+', '+str(country)
    print '[+] Latitude: '+ str(lat) + ', Longitude: '+ str(longi)
	
tgt = input('Enter your IPv4 Public IP address: ')	
printRecord(tgt)
