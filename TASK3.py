from operator import mod
from TASK1 import movie_data
import json
import pprint
def group_by_decade(movies):
    decade_year=[]
    index=0
    while index<len(movies):
        for key in movies[index]:
            if key=="Year":
                mod=movies[index][key]%10
                decade=movie_data[index][key]-mod
                decade_year.append(decade)
        index=index+1
    decade_year.sort()
    movies_dic={}
    i=0
    while i <len(movies):
        dec=decade_year[i]+10
        Year_list=[]
        j=0
        while j<len(decade_year):
            if movies[j]["Year"]>decade_year[i] and movies[j]["Year"]<dec:
                Year_list.append(movies[j])
            movies_dic[decade_year[i]]=Year_list
            j=j+1
        i=i+1
    with open("task3.json","w+")as Year_info:
        json.dump(movies_dic,Year_info,indent=4)
        return movies_dic
store=group_by_decade(movie_data)
pprint.pprint(store)