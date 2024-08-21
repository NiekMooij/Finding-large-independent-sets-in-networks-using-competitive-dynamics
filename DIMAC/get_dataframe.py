import os
import sys
import numpy as np
import pandas as pd
import networkx as nx
from scipy.io import mmread

def get_data():
    """
    Function to read graph data from Matrix Market files, compute various graph properties, 
    and save the data to CSV and pickle files.

    Returns:
    None
    """

    # Initialize an empty list to store data for each graph
    data = []

    # Loop through each graph file in the 'graphs' directory
    for graph_name in sorted(os.listdir(os.path.join(sys.path[0], 'graphs'))):
        if graph_name == '.DS_Store':
            continue
        
        # Read the Matrix Market file and convert it to a dense matrix
        a = mmread(os.path.join(sys.path[0], f'graphs/{graph_name}/{graph_name}.mtx'))
        A = a.todense()

        # Convert the dense matrix to a NetworkX graph
        G = nx.from_numpy_array(A)

        # Compute the size (number of vertices) and density of the graph
        size = len(G)
        density = np.round(len(G.edges()) / (size * (size - 1) / 2), 2)

        # Compute the minimum and maximum degrees of the vertices in the graph
        degrees = [G.degree(node) for node in G]
        degree_min = min(degrees)
        degree_max = max(degrees)

        # Create a dictionary containing the graph properties
        new_row = {
            'graph_name': graph_name,
            'vertices': G.nodes(),
            'edges': G.edges(),
            'size': size,
            'density': density,
            'degree_min': degree_min,
            'degree_max': degree_max,
            'LV_output': None,
            'LV_time': None,
            'continuation_output': None, 
            'continuation_time': None,
            'greedy_output': None,
            'greedy_time': None,
            'rpp_output': None,
            'rpp_time': None,
            'luby_output': None,
            'luby_time': None,
            'blelloch_output': None,
            'blelloch_time': None,
        }
        
        # Append the dictionary to the list of data
        data.append(new_row)
            
    # Create a DataFrame from the list of data
    df = pd.DataFrame(data)

    # Save the DataFrame to CSV and pickle files
    df.to_csv(os.path.join(sys.path[0], "data_empty/DIMAC.csv"), index=False)
    df.to_pickle(os.path.join(sys.path[0], "data_empty/DIMAC.pkl"))

if __name__ == '__main__':
    get_data()