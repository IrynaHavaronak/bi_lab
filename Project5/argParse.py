import argparse
from ftplib import FTP
import gzip
import os
import save_in_formats as sf

url_def = 'ftp.fu-berlin.de/pub/misc/movies/database/frozendata/ratings.list' \
          '.gz'
parser = argparse.ArgumentParser()
parser.add_argument("--download", nargs='?', default=url_def)
parser.add_argument("--format", nargs='?',
                    default='csv', help='Put one of the following formats: '
                                        'csv, json, xml, yaml')

url_parse = parser.parse_args()
t1 = len(url_parse.download) - url_parse.download[::-1].index('/')
filename = url_parse.download[t1:]
address = url_parse.download[:url_parse.download.index('/'):]
f1 = url_parse.download.index('/') + 1
f2 = len(url_parse.download) - url_parse.download[::-1].index('/') - 1
directory = url_parse.download[f1:f2]
f_format = url_parse.format
print(directory)
print(filename)
print(address)
try:
    if not os.path.isfile(filename):
        ftp = FTP()
        gz_file = gzip.open(filename, 'wb')
        ftp.set_pasv(True)
        ftp.connect(address, timeout=150)
        ftp.login()
        ftp.cwd(directory)
        ftp.retrbinary('RETR ' + filename, gz_file.write)
        ftp.quit()
        gz_file.close()
    if f_format == 'json':
        sf.save_as_json(filename)
    if f_format == 'csv':
        sf.save_as_csv(filename)
    if f_format == 'yaml':
        sf.save_as_yaml(filename)
    if f_format == 'xml':
        sf.save_as_xml(filename)
except TimeoutError:
    print("ftp.fu-berlin.de isn't available now. Try later")
