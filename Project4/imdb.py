import csv


def avg_rating(lst):
    imdb_data.sort(key=lambda x: x[6], reverse=True)
    year = list()
    rating = list()
    notes_num = list()
    for item in lst:
        if item[6] in year:
            ind = year.index(item[6])
            rating[ind] += float(item[8])
            notes_num[ind] += 1
        else:
            year.append(item[6])
            rating.append(float(item[8]))
            notes_num.append(1)
    for i in range(0, len(rating)):
        rating[i] /= notes_num[i]
    return [year, rating]


file_name = "IMDB-Movie-Data.csv"
top_filename = "top250_movies.csv"
rating_filename = "ratings.csv"
try:
    with open(file_name, 'r') as imdb_file:
        imdb_file.readline()
        imdb_reader = csv.reader(imdb_file, delimiter=',', quotechar="\"")
        imdb_data = []
        for i in imdb_reader:
            imdb_data.append(i,)
        imdb_data.sort(key=lambda x: x[8], reverse=True)
        top_file = open(top_filename, 'w')
        fieldnames = ['Title', 'Rating']
        top_out = csv.DictWriter(top_file, fieldnames=fieldnames)
        top_out.writeheader()
        for i in range(0, 251):
            top_out.writerow({fieldnames[0]: imdb_data[i][1],
                              fieldnames[1]: imdb_data[i][8]})
        top_file.close()
        rating_file = open(rating_filename, 'w')
        fieldnames = ['Year', 'Avg Rating']
        rating_out = csv.DictWriter(rating_file, fieldnames=fieldnames)
        rating_out.writeheader()
        res = avg_rating(imdb_data)
        for i in range(0, len(res[0])):
            rating_out.writerow({fieldnames[0]: res[0][i],
                                 fieldnames[1]: res[1][i]})
        rating_file.close()
except FileNotFoundError:
    print("ERROR: File %s is not found" % file_name)
