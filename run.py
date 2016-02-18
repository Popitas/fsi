import search

mi_problema = search.RomaniaGPS('A', 'F', search.romania)

print "Breadth search:"
print search.breadth_first_graph_search(mi_problema)

print "\nDepth search:"
print search.depth_first_graph_search(mi_problema)

