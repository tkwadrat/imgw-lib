import requests
from pprint import pprint
baza = 'cbdh'
stacjaKod = '150210170'
stacjaKlasyfikacja = "B010B050CD"
zakres = "doba"
dataOd = "2011-11-25"

r = requests.get('https://dane.imgw.pl/1.0/pomiary/'+baza+'/'+stacjaKod+'-'+stacjaKlasyfikacja+'/'+zakres+'/'+dataOd, auth=('tomasz@tomaszewski.it', 'c6a96b6c'))
pprint(r.status_code)
pprint(r.json())
