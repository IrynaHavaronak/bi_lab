from ftplib import FTP
import gzip
import os


try:
    if not os.path.isfile("ratings.gz"):
        ftp = FTP()
        gz_file = gzip.open("ratings.gz", 'wb')
        ftp.set_pasv(True)
        ftp.connect('ftp.fu-berlin.de', timeout=150)
        ftp.login()
        ftp.cwd("pub/misc/movies/database/frozendata")
        ftp.dir()
        ftp.retrbinary('RETR ratings.list.gz', gz_file.write)
        ftp.quit()
        gz_file.close()
    with gzip.open('ratings.list.gz', 'rb')as f_gz:
        with open('ratings.txt', 'wb')as f_txt:
            f_txt.write(f_gz.read().decode("cp437").encode('utf8'))

except TimeoutError:
    print("ftp.fu-berlin.de isn't available now. Try later")
