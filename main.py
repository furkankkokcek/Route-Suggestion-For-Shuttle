import arcpy

shp = r"C:\Users\Furkan\Documents\ArcGIS\Projects\assignment1\datas.shp"
alldata={}
#print([field.name for field in arcpy.ListFields(shp)])
cursor = arcpy.da.SearchCursor(shp, ['FID', 'walk_dista', 'ORIG_FID','FID_route','directionF','priorityFi','densityFie'])
for row in cursor:
	values=[]
	point=0
	if int(row[4])==2:
		point+=5
	if int(row[5])==1:
		point+=9
	if int(row[5])==2:
		point+=7
	if int(row[5])==3:
		point+=5
	if int(row[5])==4:
		point+=1
	if int(row[6])==4:
		point+=15
	if int(row[6])==3:
		point+=9
	if int(row[6])==2:
		point+=7
	if int(row[6])==1:
		point+=3
	#print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],point)
	if int(row[2]) in alldata.keys():
		if point>alldata[int(row[2])][1]:
			alldata[int(row[2])][0]=int(row[3])
			alldata[int(row[2])][1]=point
	else:
		values.append(int(row[3]))		#row[3]=route_id 
		values.append(point)			#point=final score
		alldata[int(row[2])]=values		#row[2]=point_id	
for key in alldata:
	print(key,alldata[key])