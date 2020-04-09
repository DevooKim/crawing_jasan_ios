import os

#code = [] #자산번호 리스트

def ext_name():

    for filename in os.listdir("."):
        if filename.endswith("txt"):
            f = open(filename, 'rt', encoding='utf-8')
            code = f.readlines()

    return code
        

def crawing(code):
    for a in code:
        print(a)

if __name__ == "__main__":
    a = ext_name()
    crawing(a)

