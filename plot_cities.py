import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago",41.9, -87.6],
          ["Boston", 42.4, -71.1],
          ["Northport", 41, -73],
          ["Placerville", 38.7, -120.8],
          ["Topeka", 39.0, -95.7],
          ["Rockford", 42.2677, -89.0878]]

scale = 5

map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)

map.drawstates()
map.drawcountries()
map.drawcoastlines()
map.bluemarble()

# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o',color='Red')
    plt.text(x + 20000, y + 20000, city, fontsize=9, color='white')

plt.savefig("my_map.png")
plt.show()
