import csv
import argparse
from sortedcontainers import SortedDict
parser = argparse.ArgumentParser()


def histogram(lst, el):
    hist = {}
    for r in lst[1:]:
        if hist.get(int(r[el])) is None:
            hist[int(r[el])] = 0
        hist[int(r[el])] += 1
    return SortedDict(hist.items())


parser.add_argument("--year", nargs='?', default='no')
parser.add_argument("--rate", nargs='?', default='no')
parser.add_argument("--all", nargs='?', default='no')
parser.add_argument("--histogram")
parser.add_argument("--output")

imdb_data = open('IMDB-Movie-Data.csv', 'r', encoding='utf-8')

if imdb_data:
    imdb_reader = csv.reader(imdb_data)
    imdb_list = list(imdb_reader)
    top_videos = sorted(imdb_list[1:], key=lambda x: float(x[8]),
                        reverse=True)[:250]

    if parser.parse_args().all is None:
        print("Title    Rating   Year")
        for i in top_videos:
            print(i[1], i[8], i[6])
    if parser.parse_args().year is None:
        print("Title     Year")
        for i in top_videos:
            print(i[1], i[6])
    if parser.parse_args().all is None:
        print("Title    Rating")
        for i in top_videos:
            print(i[1], i[8])
    if parser.parse_args().histogram == 'year':
        print(histogram(imdb_list, 6))
    if parser.parse_args().histogram == 'rating':
        print(histogram(imdb_list, 8))
    if parser.parse_args().output is not None:
        with open(parser.parse_args().output, 'w') as f:
            for row in imdb_list:
                f.writelines(str(row)+'\n')
else:
    imdb_data.close()
    print('File \"IMDB-Movie-Data.csv\" not found!')
