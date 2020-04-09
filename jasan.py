import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time


def ext_name():

    for filename in os.listdir("."):
        if filename.endswith("txt"):
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.readlines()
                del code[len(code)-1]   
                code = list(map(lambda s: s.strip(), code))
    return code
        

def crawing(code):
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
        return object_list

def toCSV(object_list):
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    f_name = date + '자산조사.csv'
    file = open(f_name, 'a', encoding='cp949', newline='')
    csvfile = csv.writer(file)
    csvfile.writerow(object_list)
    file.close
    print('완료')


if __name__ == "__main__":
    code = ext_name()
    list = crawing(code)
    toCSV(list)
