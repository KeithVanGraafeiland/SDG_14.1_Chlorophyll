import arcpy
#arcpy.env.workspace = "D:/ChlorA/PML/5.0/Monthly/2021"
arcpy.env.workspace = "E:/ChlorA/NESDIS/coastwatch/viirs/science/L3/global/chlora/anom/WW00/2023"
# outgdb = "D:/ProProject/ChlorA P90/Subindicator2/VIIRS_PDIF.gdb/"
outtif = "E:/ChlorA_Sub2/"
#filelist = arcpy.ListFiles("*.nc")
filelist = arcpy.ListFiles("*chlorapdif.nc")
arcpy.env.overwriteOutput = True

for name in filelist:
    ras = "in_memory/ras"
    #fgdb_ras = outgdb + name.split(".")[0]
    tif_ras = outtif + name.split(".")[0] + ".tif"
    print("Processing: " + name)
    #ncRaster = "D:/ChlorA/PML/5.0/Monthly/2023/" + name
    ncRaster = "E:/ChlorA/NESDIS/coastwatch/viirs/science/L3/global/chlora/anom/WW00/2023/" + name
    print(ncRaster)
    #arcpy.md.MakeNetCDFRasterLayer(ncRaster, "chlor_a", "lon", "lat", ras, '', None, "BY_VALUE", "CENTER")
    arcpy.md.MakeNetCDFRasterLayer(ncRaster, "chlor_a_pdif", "lon", "lat", ras, '', None, "BY_VALUE", "CENTER")
    #arcpy.Raster(ras).save("chlor_a_PML_v5_0_" + name.split("-")[-2] +  ".tif")
    arcpy.Raster(ras).save(tif_ras)
    #arcpy.management.BuildPyramids(fgdb_ras,-1, "NONE", "NEAREST", "DEFAULT", 75, "OVERWRITE")
    #con_raster = arcpy.sa.Con(fgdb_ras, fgdb_ras, None, "VALUE >= -20 And VALUE <= 20")
    con_raster = arcpy.sa.Con(tif_ras, tif_ras, None, "VALUE >= -20 And VALUE <= 20")
    con_raster.save(tif_ras.split(".")[0] + "_con.tif")
    arcpy.management.Delete(tif_ras)

print("Done")



