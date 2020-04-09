import os

#code = [] #자산번호 리스트

def ext_name():

    for filename in os.listdir("."):
        if filename.endswith("txt"):
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.readlines()
                del code[len(code)-1]   
                code = list(map(lambda s: s.strip(), code))
    return code
        

#def crawing(code):

if __name__ == "__main__":
    ext_name()
