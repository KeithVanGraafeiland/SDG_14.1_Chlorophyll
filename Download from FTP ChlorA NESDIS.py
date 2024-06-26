import ftplib
import shutil
import os

#Downloads Chlorophyll netCDF files from the NESDIS STAR FTP Site
#ftp://ftp.star.nesdis.noaa.gov/pub/socd1/mecb/coastwatch/viirs/science/L3/global/chlora/anom/WW00/2019/

ftp = ftplib.FTP('ftp.star.nesdis.noaa.gov')
ftp.login(user='anonymous', passwd = 'anonymous@')
ftp.cwd('/pub/socd1/mecb/coastwatch/viirs/science/L3/global/chlora/anom/WW00/2022/')
filenames = ftp.nlst()
fileloc = 'D:/ChlorA/NESDIS'
#fullurl = 'ftp://ftp.star.nesdis.noaa.gov/pub/socd1/mecb/coastwatch/viirs/science/L3/global/chlora/anom/WW00/'

for filename in filenames:

    with open( filename, 'wb' ) as file :
        print ("Downloading file .......... ", filename)
        ftp.retrbinary('RETR %s' % filename, file.write, 1024)
        file.close()
        if os.path.isfile(filename):
            shutil.copy2(filename, fileloc)
            os.remove(filename)
        else:
            shutil.move(filename, fileloc)
        print('Successfully downloaded.......... ', filename)
print("Done Downloading!")
ftp.quit()