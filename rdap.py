import requests
import pandas as pd

def rdap(iplist):
        url = 'http://rdap.arin.net/bootstrap/ip/'
        data = []
        columns = ['ip','startaddress','endaddress','name']
        for a,ip in enumerate(iplist):
                resp = requests.get(url+ip)
                if 'name' in resp.json().keys():
                        data.append([ip,resp.json()['startAddress'],resp.json()['endAddress'],resp.json()['name']])
        return pd.DataFrame(data=data,columns=columns)
