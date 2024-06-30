from threading import Thread
import json
import requests

class WeaG:
    '''this is a test'''

    url = [
        'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001',
        'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001',
        'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0002-001'
    ]

    def __init__(self, conf='env.json'):
        with open(conf) as f:
            env = json.load(f)
        self.token = env.get('token')

    def grab(self, site):
        '''this is a main method for weather info collection,
           will output a dict as {'O': ...}'''

        def _grab(url, site, info):
            params = {'Authorization': self.token, 'StationName': site}
            r = requests.get(url, params=params)
            if 'records' in r.json() and 'location' in r.json()['records'] and r.json()['records']['location']:
                s = r.json()['records']['location'][0]
                if 'time' in s:
                    info['O'] = s['time']['obsTime']
                if 'weatherElement' in s:
                    for elem in s['weatherElement']:
                        if elem['elementName'] == 'TEMP':
                            info['T'] = float(elem['elementValue'])
                        if elem['elementName'] == 'HUMD':
                            info['H'] = float(elem['elementValue'])
                if 'parameter' in s:
                    for param in s['parameter']:
                        if param['parameterName'] == 'RAIN':
                            info['R'] = float(param['parameterValue'])

        info = {}
        threads = [Thread(target=_grab, args=(url, site, info), daemon=True) for url in self.url]
        
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        return info

    def tostr(self, info):
        w = []
        sep = ' '

        if o := info.get('O'):
            w.append(f'觀測時間: {o}')  
        if t := info.get('T'):
            w.append(f'氣溫: {t:.1f}度')     
        if h := info.get('H'):
            w.append(f'濕度: {h:.0%}')
        if (r := info.get('R')) is not None:
            w.append(f'降雨量: {r:.1f} mm')
        
        return sep.join(w)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('site')
    args = parser.parse_args()
    
    w = WeaG()
    result = w.grab(args.site)
    print(w.tostr(result))
