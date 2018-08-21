
#CSVファイルを読み込んで別のCSVに出力する

import csv
from itertools import islice



#ファイルオブジェクトとしてCSVを開く
with open('gaku-mg1642.csv','r',encoding='shift-jis') as csvFile:
    #readerオブジェクトを取得
    dataReader = csv.reader(csvFile)

    #一時領域用リスト
    datalist = []
    #1行ごとのリストとして取得できるので8行目から1列目と2列目を配列に2次元配列として保存する
    for row in islice(dataReader,7,None):
        datalist.append([row[0],row[1]])

with open('sample.csv','w') as outFile:
    writer = csv.writer(outFile, lineterminator='\r\n')
    writer.writerows(datalist)

