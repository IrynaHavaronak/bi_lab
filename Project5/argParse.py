import argparse
import os
import gzip
import save_in_formats as sf
from ftplib import FTP

url_def = 'ftp.fu-berlin.de/pub/misc/movies/database/frozendata/ratings.list' \
          '.gz'
parser = argparse.ArgumentParser()
parser.add_argument("--download", nargs='?', default=url_def)
parser.add_argument("--format", nargs='?',
                    default='csv', help='Put one of the following formats: '
                                        'csv, json, xml, yaml')

url_parse = parser.parse_args().download
filename = url_parse[len(url_parse)-url_parse[::-1].index('/'):]
address = url_parse[:url_parse.index('/'):]
directory = url_parse[url_parse.index('/')+1:len(url_parse)-url_parse[
                                                          ::-1].index('/')-1:]
fformat = url_parse.format
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
    if fformat == 'json':
        sf.save_as_json(filename)
    if fformat == 'csv':
        sf.save_as_csv(filename)
    if fformat == 'yaml':
        sf.save_as_yaml(filename)
    if fformat == 'xml':
        sf.save_as_xml(filename)
except TimeoutError:
    print("ftp.fu-berlin.de isn't available now. Try later")
