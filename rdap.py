import requests
import pandas as pd

def rdap(iplist):
        url = 'http://rdap.arin.net/bootstrap/ip/'
        data = []
        columns = ['IP','StartAddress','EndAddress','Name']
        for a,ip in enumerate(iplist):
                resp = requests.get(url+ip)
                if 'name' in resp.json().keys():
                        data.append([ip,resp.json()['startAddress'],resp.json()['endAddress'],resp.json()['name']])
                elif 'startAddress' in resp.json().keys():
                        data.append([ip,resp.json()['startAddress'],resp.json()['endAddress'],None])
                else:
                        data.append([ip,None,None,None])
        return pd.DataFrame(data=data,columns=columns)
        
if __name__=='__main__':
        rdap()
