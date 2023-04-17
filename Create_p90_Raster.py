import arcpy
arcpy.env.overwriteOutput = True

import csv
with open ('Book8.csv','r') as csv_file:
    reader =csv.reader(csv_file)
    next(reader) # skip first row
    for row in reader:
        print(row)


anomaly_raster = r"D:\ProProject\ChlorA P90\Deviation_Anomaly\09_Anomaly\chlor_a_PML_v5_0_200501_09_Anomaly.tif"
p90_value = 0.891
p90_raster = r"D:\ProProject\ChlorA P90\Deviation_Anomaly\p90_Monthly_Raster\chlor_a_PML_v5_0_200501_p90.tif"

out_raster = arcpy.sa.Times(anomaly_raster, p90_value);
out_raster.save(p90_raster)

