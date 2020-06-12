import pandas as pd
import requests
from bs4 import BeautifulSoup

i= pd.read_csv(filepath_or_buffer="weather.csv", encoding="ms932", sep=",")

c = 0

city = [[44,47662,"東京"],[62,47772,"大阪"],[67,47765,"広島"],[74,47893,"高知"],[82,47807,"福岡"],[86,47819,"熊本"],[88,47827,"鹿児島"],[91,47936,"沖縄"]]

print('now search....')

# データ取得
f= open("output/weather_out.csv",'w',encoding='Shift_JIS')

while c < 8:
    # データ格納
    url = "http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=" + str(city[c][0]) + "&block_no=" + str(city[c][1]) + "&year=" + str(i.values[0, 0]) + "&month=" + str(i.values[0, 1]) + "&day=1&view="
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    elems  = soup.find_all(class_="a_print")

    if  c == 0:
        for e in elems:
            f.write(',')
            f.write('"'+e.getText()+'"')
        f.write('\n')

    elems2 = soup.find_all(class_="data_0_0")

    f.write(city[c][2]+',')

    cnt = 0
    for e2 in elems2:
        cnt = cnt + 1
        rem = cnt % 20
        if  rem == 19:
            f.write('"'+e2.getText()+'"')
            f.write(',')
    f.write('\n')
    c = c + 1

f.close()

print('finish!')