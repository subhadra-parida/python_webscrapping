from TASK5 import*
genre_info=movie_info
def analyse_movie_genre():
    genre_dic={}
    for data in genre_info:
        count=0
        for genre in data["Genre"]:
            for check_genre in data["Genre"]:
                if genre==check_genre:
                    count=count+1
            genre_dic[genre]=count
    with open("task11.json","w+") as genre_data:
        json.dump(genre_dic,genre_data,indent=4)
    pprint(genre_dic)
    return genre_dic
analyse_movie_genre()
