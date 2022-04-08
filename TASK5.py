from TASK2 import group_by_year
from TASK4 import*
from TASK1 import movie_data, scrap_top_list
from TASK1 import pprint
movie=movie_data
user=int(input("Enter how many movie="))
def get_movie_list_details():
    movie_url=[]
    movie_list=[]
    i=0
    while i<len(movie[:user]):
        movie_list.append(scrape_movie_details(movie_data[i]["url"],movie_data[i]["movie_name"]))
    with open("task5.json","w+") as movie_details:
        json.dump(movie_details,movie_details,indent=4)
    return movie_list
movie_info=get_movie_list_details()