from TASK5 import*
movie_dic={}
movie_list=movie_info
def analyse_director_and_language():
    for name in movie_list:
        count_language=0
        movie_language=0
        for info in movie_list:
            if name["Director"]==info["Director"] and name["Language"]==info["Language"]:
                director_name=str(name["Director"])[2:-2]
                language=str(name["Language"])
                count_language=count_language+1
        movie_dic[director_name]=movie_language
    pprint(movie_dic)
    with open("task10.json","w+")as json_data:
        json.dump(movie_dic,json_data,indent=4)
    return movie_dic
analyse_director_and_language()