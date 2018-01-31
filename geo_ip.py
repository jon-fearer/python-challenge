import requests
import pandas as pd

# Supply a list of ip addresses and return a pandas dataframe with geo ip lookup data
def geoip(iplist):
        url = 'https://freegeoip.net/json/'
        data = []
        for a,ip in enumerate(iplist):
                resp = requests.get(url+ip)
                if a == 0:
                        columns = [key for key in resp.json().keys()]
                data.append([resp.json()[key] for key in columns])
        return pd.DataFrame(data=data,columns=columns)
                
if __name__=='__main__':
        geoip()

