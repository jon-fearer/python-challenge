import re
import pandas as pd

# combine dataframes from geoip and rdap lookups
def join(df1,df2):
        return df1.join(df2.set_index('ip'),on='ip')

# write a query of the form SELECT <cols> WHERE ip = ...
# or just SELECT <cols>
def lookup(df,query):
        query = query.lower()
        if 'where' in query:
                cols = query.split('select')[1].split('where')[0]
                cols = [col.strip() for col in cols.split(',')]
                wh = query.split('select')[1].split('where')[1]
                ip = wh.split('=')[1].strip()
                return df[df['ip']==ip][cols]
        else:
                cols = query.split('select')[1]
                cols = [col.strip() for col in cols.split(',')]
                return df[cols]
		

		
