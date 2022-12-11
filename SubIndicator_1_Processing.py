import ftplib
import shutil
import arcpy
arcpy.env.overwriteOutput = True
from PML_Credentials import username, password

#Downloads Chlorophyll netCDF files from the Plymouth Marine Lab FTP site
ftp = ftplib.FTP('ftp.rsg.pml.ac.uk')
ftp.login(user = username, passwd = password)
suburl = '/occci-v5.0/geographic/netcdf/monthly/chlor_a/'
yeardownload = '2000'
ftp.cwd(suburl + yeardownload)
filenames = ftp.nlst()
fileloc = 'D:/ChlorA/PML/5.0'
#example fullurl = 'ftp://ftp.rsg.pml.ac.uk/occci-v4.2/geographic/netcdf/monthly/chlor_a/'
arcpy.env.workspace = 'D:/ChlorA/PML/5.0/TIF'

for filename in filenames:
    with open( filename, 'wb' ) as file :
        print ("Downloading file .......... ", filename)
        ftp.retrbinary('RETR %s' % filename, file.write, 1024)
        file.close()
        shutil.move(filename, fileloc)
        print('Successfully downloaded.......... ', filename)
        ras = "in_memory/ras"
        print("Processing: " + filename)
        arcpy.md.MakeNetCDFRasterLayer(fileloc + "\\" + filename, "chlor_a", "lon", "lat", ras, '', '', "BY_VALUE", "CENTER")
        arcpy.Raster(ras).save("chlor_a_PML_v5_0_" + filename.split("-")[-2] + ".tif")
print("Done Downloading and Processing " + yeardownload)
ftp.quit()