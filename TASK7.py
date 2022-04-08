import json
import requests
from bs4 import BeautifulStoneSoup
with open("task5.json","r+")as file:
    data1=json.load(file)
def analyse_movies_director(data1):
    dic={}
    for i in data1:
        if "director" in i:
            Director=i["Director"]
            for i in Director:
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
    print(dic)
    with open("task6.json","w+") as file1:
        json.dump(dic,file1,indent = 4)
analyse_movies_director(data1)
                  