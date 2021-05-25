#!/usr/bin/env python3
import xlrd
import json
import operator

def read_xlsx(filename):
    data1 = xlrd.open_workbook('test.xlsx')
    table = data1.sheets()[0]
    n_rows = table.nrows
    
    data = []
    
    for v in range(1, n_rows-1):
        values = table.row_values(v)
        
        data.append({
            'title': values[0],
            'uid': values[1],
            'name': values[2],
        })
    return data

if __name__ == '__main__':
    d=[]
    d1 = read_xlsx('./test.xlsx')
    d.extend(d1)
    d = sorted(d, key=operator.itemgetter('uid'))
    
    with open('myData.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=2))