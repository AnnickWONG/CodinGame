import math

lon = input()
lat = input()
lon = math.radians(float(lon.replace(',','.')))
lat = math.radians(float(lat.replace(',','.')))

defib_list = []
n = int(input())
for i in range(n):
    defib = input()
    no,name,addr,phone,longitude,latitude = defib.split(';')
    longitude = math.radians(float(longitude.replace(',','.')))
    latitude = math.radians(float(latitude.replace(',','.')))
    defib_list.append([no,name,addr,phone,longitude,latitude])

dist_list = []
for i in range(n):
    lon_defib = defib_list[i][4]
    lat_defib = defib_list[i][5]
    x = (lon_defib - lon) * math.acos((lat_defib+lat)/2)
    y = lat_defib - lat
    d = math.sqrt(x*x + y*y) * 6371
    dist_list.append(d)

idx = dist_list.index(min(dist_list))
print(defib_list[idx][1])
