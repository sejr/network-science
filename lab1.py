import time
import random
import networkx as nx

# Given a node, it prints the calculated centrality measures
def print_node_data(node):
    for k, v in node.items():
        print(k + ": " + str(round(v, 6)))

# Reading data into networkx graph structures
print("Reading datasets. This may take a while.")
wiki = nx.read_edgelist("networks/wiki-Vote.txt")
gnutella = nx.read_edgelist("networks/p2p-Gnutella08.txt")
grqc = nx.read_edgelist("networks/ca-GrQc.txt")
fb = nx.read_edgelist("networks/egonets-Facebook/facebook_combined.txt")

# Wiki Vote centrality measures
print("Starting centrality calculations for wiki-Vote. This may take a while.")
wiki_degree_centrality = nx.degree_centrality(wiki)
wiki_closeness_centrality = nx.closeness_centrality(wiki)
wiki_betweenness_centrality = nx.betweenness_centrality(wiki)
wiki_eigenvector_centrality = nx.eigenvector_centrality(wiki)
wiki_pagerank_centrality = nx.pagerank(wiki, alpha=0.85)
wiki_clustering_coefficients = nx.clustering(wiki)

# gnutella centrality
print("Starting centrality calculations for p2p-Gnutella08. This may take a while.")
gnutella_degree_centrality = nx.degree_centrality(gnutella)
gnutella_closeness_centrality = nx.closeness_centrality(gnutella)
gnutella_betweenness_centrality = nx.betweenness_centrality(gnutella)
gnutella_eigenvector_centrality = nx.eigenvector_centrality(gnutella)
gnutella_pagerank_centrality = nx.pagerank(gnutella, alpha=0.85)
gnutella_clustering_coefficients = nx.clustering(gnutella)

# grqc centrality
print("Starting centrality calculations for ca-GrQc. This may take a while.")
grqc_degree_centrality = nx.degree_centrality(grqc)
grqc_closeness_centrality = nx.closeness_centrality(grqc)
grqc_betweenness_centrality = nx.betweenness_centrality(grqc)
grqc_eigenvector_centrality = nx.eigenvector_centrality(grqc)
grqc_pagerank_centrality = nx.pagerank(grqc, alpha=0.85)
grqc_clustering_coefficients = nx.clustering(grqc)

# facebook centrality
print("Starting centrality calculations for ego-Facebook. This may take a while.")
fb_degree_centrality = nx.degree_centrality(fb)
fb_closeness_centrality = nx.closeness_centrality(fb)
fb_betweenness_centrality = nx.betweenness_centrality(fb)
fb_eigenvector_centrality = nx.eigenvector_centrality(fb)
fb_pagerank_centrality = nx.pagerank(fb, alpha=0.85)
fb_clustering_coefficients = nx.clustering(fb)

# Processing results
wiki_results = dict()
gnutella_results = dict()
grqc_results = dict()
fb_results = dict()

# Storing results for each node
for node in wiki.nodes():
    wiki_results[node] = dict()
    wiki_results[node]["degree"] = wiki_degree_centrality[node]
    wiki_results[node]["closeness"] = wiki_closeness_centrality[node]
    wiki_results[node]["betweenness"] = wiki_betweenness_centrality[node]
    wiki_results[node]["eigenvector"] = wiki_eigenvector_centrality[node]
    wiki_results[node]["pagerank"] = wiki_pagerank_centrality[node]
    wiki_results[node]["clustering_coeff"] = wiki_clustering_coefficients[node]
for node in gnutella.nodes():
    gnutella_results[node] = dict()
    gnutella_results[node]["degree"] = gnutella_degree_centrality[node]
    gnutella_results[node]["closeness"] = gnutella_closeness_centrality[node]
    gnutella_results[node]["betweenness"] = gnutella_betweenness_centrality[node]
    gnutella_results[node]["eigenvector"] = gnutella_eigenvector_centrality[node]
    gnutella_results[node]["pagerank"] = gnutella_pagerank_centrality[node]
    gnutella_results[node]["clustering_coeff"] = gnutella_clustering_coefficients[node]
for node in grqc.nodes():
    grqc_results[node] = dict()
    grqc_results[node]["degree"] = grqc_degree_centrality[node]
    grqc_results[node]["closeness"] = grqc_closeness_centrality[node]
    grqc_results[node]["betweenness"] = grqc_betweenness_centrality[node]
    grqc_results[node]["eigenvector"] = grqc_eigenvector_centrality[node]
    grqc_results[node]["pagerank"] = grqc_pagerank_centrality[node]
    grqc_results[node]["clustering_coeff"] = grqc_clustering_coefficients[node]
for node in fb.nodes():
    fb_results[node] = dict()
    fb_results[node]["degree"] = fb_degree_centrality[node]
    fb_results[node]["closeness"] = fb_closeness_centrality[node]
    fb_results[node]["betweenness"] = fb_betweenness_centrality[node]
    fb_results[node]["eigenvector"] = fb_eigenvector_centrality[node]
    fb_results[node]["pagerank"] = fb_pagerank_centrality[node]
    fb_results[node]["clustering_coeff"] = fb_clustering_coefficients[node]

# Printing results for each network
print("wiki-Vote nodes")
for k, v in wiki_results.items():
    print("Node: " + k)
    print_node_data(wiki_results[k])

print("gnutella nodes")
for k, v in gnutella_results.items():
    print("Node: " + k)
    print_node_data(gnutella_results[k])

print("grqc nodes")
for k, v in grqc_results.items():
    print("Node: " + k)
    print_node_data(grqc_results[k])

print("fb nodes")
for k, v in fb_results.items():
    print("Node: " + k)
    print_node_data(fb_results[k])

# We're done!
print("All nodes have been printed. Thank you for your patience.")