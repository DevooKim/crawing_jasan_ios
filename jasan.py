import os
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import csv
import time

count = 0

def ext_name():
    jasan = []
    global count
    for filename in os.listdir("."):
        if filename.endswith("txt"):
            with open(filename, 'r', encoding='utf-8') as f:
                if(filename == 'README.txt'):
                    continue
                
                code = f.readlines()
                #del code[len(code)-1]
                code = list(map(lambda s: s.strip(), code)) #개행 제거
                jasan.append(code)

    jasan = sum(jasan,[]) #2차배열 -> 1차배열
    count = len(jasan)
    return jasan
        

def crawing(code):
    total_list = []

    for num in code:
        url = "http://unihints.hannam.ac.kr/admin/servlet_ataf/servlet.do?sMulpumNo=" + num
        
        html = urlopen(url)
        bsObject = BeautifulSoup(html, "html.parser")
        object_list = []
        #물품번호, 물품명, 모델, 규격, 관리부서, 호실번호, 호실명, 취득가액, 관리자/사용자
        for tr in bsObject.find_all('tr'):
            tr_list = []
            tr_list = tr.find_all(text=True)
            object_list.append(tr_list[3])
        del object_list[0] #공백 제거
        total_list.append(object_list)
    return total_list

def toCSV(_list):
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    f_name = date + '자산조사.csv'
    file = open(f_name, 'a', encoding='cp949', newline='')
    csvfile = csv.writer(file)

    for row in _list:
        csvfile.writerow(row)

    file.close
    print(str(count) + '개 완료')


if __name__ == "__main__":
    code = ext_name()
    list = crawing(code)
    toCSV(list)
