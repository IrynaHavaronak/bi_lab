import csv
import numpy as np
imdb_data = open('IMDB-Movie-Data.csv', 'r', encoding='utf-8')

if imdb_data:
    imdb_reader = csv.reader(imdb_data)
    imdb_list = list(imdb_reader)
    top_videos = sorted(imdb_list[1:], key=lambda x: float(x[8]),
                        reverse=True)[:250]
    # find top 250
    with open('top250_movies.csv', 'w', encoding='utf-8',
              newline='') as top250_data:
        top250_writer = csv.writer(top250_data)
        top250_writer.writerow([imdb_list[0][1], imdb_list[0][8]])
        for row in top_videos:
            top250_writer.writerow([row[1], row[8]])
        top250_data.close()

    # calculate average rating
    year_rating_dict = {}
    for row in imdb_list[1:]:
        if year_rating_dict.get(row[6]) is None:
            year_rating_dict[row[6]] = list()
            year_rating_dict[row[6]].append(float(row[8]))
        else:
            year_rating_dict[row[6]].append(float(row[8]))
    print(year_rating_dict)
    with open('rating.csv', 'w', encoding='utf-8', newline='') as rating_data:
        rating_writer = csv.writer(rating_data)
        rating_writer.writerow(['Year', 'Average Rating'])
        sorted_keys = sorted(year_rating_dict.keys(), key=lambda x: int(x))
        for k in sorted_keys:
            rating_writer.writerow([k, '{:1.2f}'.
                                   format(np.mean(year_rating_dict[k]))])
    rating_data.close()
else:
    imdb_data.close()
    raise FileNotFoundError(imdb_data)
