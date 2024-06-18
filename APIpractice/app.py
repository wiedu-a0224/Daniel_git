import requests
from pprint import pprint 


class WeaG:

    token = 'CWB-127EE37E-6AEB-4068-9908-DFAA7D1A0E4F'

    url1 = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001'
    url2 = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0002-001'
    url3 = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'

    def grab(self, sname):
        params = {'Authorization': __class__.token,
                  'StationName': sname}
        
        info={}
            
        r = requests.get(WeaG.url1, params=params)
        if not r.json()['records']['Station']:
            r = requests.get(self.url2, params=params) #check 沒人

        if r.json()['records']['Station']:
            s = r.json()['records']['Station'][0]
            info['O']= s['ObsTime']['DateTime']
            info['T']= float(s['WeatherElement']['AirTemperature'])
            info['H']= float(s['WeatherElement']['RelativeHumidity'])/100          

        r =  requests.get(__class__.url3, params=params)  #rain
        if  r.json()['records']['Station']:
            s=r.jason()['records']['Station'][0]
            info['O']= s['ObsTime']['DateTime']
            info['R']= float(s['RainfallElement']['Now']['Precipitation'])
            
        return info
w = WeaG()
w.grab(input('請輸入氣象站名稱：'))
