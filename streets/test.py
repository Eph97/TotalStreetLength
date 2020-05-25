import osmnx as ox
import os
import csv
import networkx as nx
total = 0
with open('cities.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	dist = 0
    	location = row['Cities'] + ', ' + row['States'] +', USA'
    	print(location)
    	G = ox.graph_from_place(location, network_type='drive')
    	basic_stats = ox.basic_stats(G)
    	dist = basic_stats['street_length_total']
    	print("Total street length %d meters" % dist)
    	total += dist

print("Total street length of all the cities combined %d meters" % total)

    	
    	#print("total edge length ie undirected graph %d" %basic_stats['edge_length_total']) 


#Note, data for largest cities from https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population
