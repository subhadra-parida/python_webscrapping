import requests
from bs4 import BeautifulSoup
import json
# movie_url="http://www.rottentomatoes.com/m/i_lost_my_body"
movie_url="https://www.imdb.com/title/tt0066763/"
movie_name="i_lost_my_body_"
def scrape_movie_details(movieurl,movie_name):
    url=requests.get(movieurl)
    data=BeautifulSoup(url.text,"html.parser")
    main_div=data.find_all("li",class_="")
    dic1={}
    bio=data.find("div",id="movieSynopis",class_="Movie_Synopis clamp-6 js-clamp").get_text.strip()
    dic1["Bio"]=bio
    movie_name=data.find("h1",slot="title",class_="scoreboard_title").get_text()
    dic1["movie_name"]=movie_name
    for i in main_div:
        a=i.text
        b=a.split(":")
        if "/nRating" in b:
            dic1["Rating"]=b[1].replace("/n","").strip()
        elif "/nGenre" in b:
            ga=b[1].repalce("/n","").strip()
            list1=[]
            for i in ga:
                if i==",":
                    list.append(s)
                    s=""
                else:
                    s=s+1
            dic1["genre"]=list1
        elif "/nOriginal Language" in b:
            dic1["Language"]=b[1].repalce("/n","").strip()
            dir1=[j.strip() for j in b]
        elif "/nDirector" in b:
            i=0                
            list2=[]
            while i<len(b):
                if i==0:
                    i=i+1
                    continue
                list2.append(b[i].replace("/n",""))
                i=i+1
            dic1["Producer"]=list2
        elif "/nRuntime" in b:
            s=b[1].replace("/n","").strip()
            h=int(s[0])*60 or s[i]
            i=0
            import requests
from bs4 import BeautifulSoup
import json
# movie_url="http://www.rottentomatoes.com/m/i_lost_my_body"
movie_url="https://www.imdb.com/title/tt0066763/"
movie_name="i_lost_my_body_"
def scrape_movie_details(movieurl,movie_name):
    url=requests.get(movieurl)
    data=BeautifulSoup(url.text,"html.parser")
    main_div=data.find_all("li",class_="")
    dic1={}
    bio=data.find("div",id="movieSynopis",class_="Movie_Synopis clamp-6 js-clamp").get_text.strip()
    dic1["Bio"]=bio
    movie_name=data.find("h1",slot="title",class_="scoreboard_title").get_text()
    dic1["movie_name"]=movie_name
    for i in main_div:
        a=i.text
        b=a.split(":")
        if "/nRating" in b:
            dic1["Rating"]=b[1].replace("/n","").strip()
        elif "/nGenre" in b:
            ga=b[1].repalce("/n","").strip()
            list1=[]
            for i in ga:
                if i==",":
                    list.append(s)
                    s=""
                else:
                    s=s+1
            dic1["genre"]=list1
        elif "/nOriginal Language" in b:
            dic1["Language"]=b[1].repalce("/n","").strip()
            dir1=[j.strip() for j in b]
        elif "/nDirector" in b:
            i=0                
            list2=[]
            while i<len(b):
                if i==0:
                    i=i+1
                    continue
                list2.append(b[i].replace("/n",""))
                i=i+1
            dic1["Producer"]=list2
        elif "/nRuntime" in b:
            s=b[1].replace("/n","").strip()
            h=int(s[0])*60 or s[i]
            i=0
            j=""
            while i<len(s):
                if s[i]=="h" or s[i]=="" or i==0:
                    i=i+1
                    continue
                else:
                    j=j+s[i]
                    i=i+1
            h=h+int(j)
            dic1["Runtime"]=h
            dic1["moviename"]=movie_name
    with open("task4.json","w") as file4:
        json.dump(dic1,file4,indent=4)
        a=json.dumps(dic1)
        return dic1
scrape_movie_details("http://www.rottentomatoes.com/m/i_lost_my_body",movie_name)
# scrape_movie_details("https://www.imdb.com/title/tt0066763/",movie_name)
        