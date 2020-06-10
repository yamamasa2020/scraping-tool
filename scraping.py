import pandas as pd
import requests
from bs4 import BeautifulSoup

i= pd.read_csv(filepath_or_buffer="input.csv", encoding="ms932", sep=",")

cmax=i.size / 5

c = 0

print('now search....')

while c < cmax:
    # データ格納
    r = requests.get(i.values[c, 0])

    soup = BeautifulSoup(r.content, "html.parser")

    elems  = soup.find_all(class_=i.values[c, 1])
    elems2 = soup.find_all(class_=i.values[c, 2])
    elems3 = soup.find_all(class_=i.values[c, 3])

    # データ取得
    f= open("output/" + i.values[c, 4],'w',encoding='utf-8')

    f.write(i.values[c, 0]+'\n')

    for e in elems:
    
        f.write('"'+e.getText()+'"')
        f.write(',')

    f.write('\n')
    for e2 in elems2:
        f.write('"'+e2.getText()+'"')
        f.write(',')

    f.write('\n')
    for e3 in elems3:
        f.write('"'+e3.getText()+'"')
        f.write(',')
    f.close()
    c = c + 1

print('finish!')