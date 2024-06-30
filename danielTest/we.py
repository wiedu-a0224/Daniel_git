from threading import Thread
import json

import requests

class WeaG:
    '''this is a test '''

    url = ['https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001',
           'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001',
           'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0002-001'
          ]

    def __init__(self, conf='env.json'):
        with open(conf) as f:
            env = json.load(f)
        self.token = env.get('token')
    
    def grab(self, site):
        '''this is a main method, for weather info collection,
           will output a dict as {'O': ...}'''
    
        def _grab(url, site):
            nonlocal info
            
            params = {'Authorization': self.token,
                      'StationName': site}
            r = requests.get(url, params=params)
            if r.json()['records']['Station']:
                s = r.json()['records']['Station'][0]
                info['O'] = s['ObsTime']['DateTime']
                if 'WeatherElement' in s:
                    info['T'] = float(s['WeatherElement']['AirTemperature'])
                    info['H'] = float(s['WeatherElement']['RelativeHumidity']) / 100
                elif 'RainfallElement' in s:
                    info['R'] = float(s['RainfallElement']['Now']['Precipitation'])
        
        info = {}      
        ths = [None] * len(__class__.url)
        for i in range(len(__class__.url)):
            ths[i] = Thread(target=_grab, args=(__class__.url[i], site), daemon=True)
            ths[i].start()
        
        for i in range(len(__class__.url)):
            ths[i].join()
        
        return info

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('site')
    #parser.add_argument('-t', '--timeout', type=float, default=3, help='timeout, default 3s')
    #parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    w = WeaG()
    print(w.grab(args.site))
