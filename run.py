import search

mi_problema = search.GPSRoutes('A', 'F', search.romania)

print "Breadth search:"
search.breadth_first_graph_search(mi_problema)

print "\nDepth search:"
search.depth_first_graph_search(mi_problema)

