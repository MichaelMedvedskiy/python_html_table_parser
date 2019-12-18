import pandas as pd

import urllib.request

url = "https://ru.wikipedia.org/wiki/%D0%A3%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82_%D0%98%D0%A2%D0%9C%D0%9E"

fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

#print(mystr)

df_list = pd.read_html(mystr)


for i, df in enumerate(df_list):
    #print(df.index)
    #print(df.columns)
    if 'Национальные исследовательские университеты России' in df.columns:
        print(df['Национальные исследовательские университеты России'])

    # df.to_csv('table {}.csv'.format(i))