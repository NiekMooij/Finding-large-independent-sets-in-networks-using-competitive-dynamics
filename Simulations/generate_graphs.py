import numpy as np
import networkx as nx
import pandas as pd
import os
import sys
import MIS_algorithms as MIS

def generate_row_erdos_renyi(size, p):
        
    G = MIS.erdos_renyi(size, p, connected=True)
    
    new_row = {
                'type': 'erdos_renyi',
                'size': len(G),
                'p_connection': p,
                'vertices': sorted(G.nodes()),
                'edges': G.edges(), 
                'exact_output': None, 
                'exact_time': None,
                'LV_output': None, 
                'LV_time': None, 
                'continuation_output': None, 
                'continuation_time': None, 
                'greedy_output': None, 
                'greedy_time': None,
                'luby_output': None, 
                'luby_time': None,
                'blelloch_output': None, 
                'blelloch_time': None,
                'rpp_output': None, 
                'rpp_time': None
                }

    return new_row

def generate_row_bipartite(size_a, size_b, p):
        
    G = MIS.random_bipartite(size_a, size_b, p, connected=True)
    
    new_row = {
                'type': 'random_bipartite',
                'size1': int(len(G) / 2), 
                'size2': int(len(G) / 2), 
                'p_connection': p,
                'vertices': sorted(G.nodes()),
                'edges': G.edges(), 
                'exact_output': None, 
                'exact_time': None,
                'LV_output': None, 
                'LV_time': None, 
                'continuation_output': None, 
                'continuation_time': None, 
                'greedy_output': None, 
                'greedy_time': None,
                'luby_output': None, 
                'luby_time': None,
                'blelloch_output': None, 
                'blelloch_time': None,
                'rpp_output': None, 
                'rpp_time': None
                }

    return new_row

def generate_row_geometric(size, p):
    
    G = MIS.random_geometric(size, p, connected=True)
    
    new_row = {
                'type': 'random_geometric',
                'size': len(G),
                'r_radius': p,
                'vertices': sorted(G.nodes()),
                'edges': G.edges(), 
                'exact_output': None, 
                'exact_time': None,
                'LV_output': None, 
                'LV_time': None, 
                'continuation_output': None, 
                'continuation_time': None, 
                'greedy_output': None, 
                'greedy_time': None,
                'luby_output': None, 
                'luby_time': None,
                'blelloch_output': None, 
                'blelloch_time': None,
                'rpp_output': None, 
                'rpp_time': None
                }

    return new_row

def generate_row_barabasi_albert(size, m):
    
    G = MIS.barabasi_albert(size, m)
    
    new_row = {
                'type': 'barabasi_albert',
                'size': len(G),
                'm': m,
                'vertices': sorted(G.nodes()),
                'edges': G.edges(), 
                'exact_output': None, 
                'exact_time': None,
                'LV_output': None, 
                'LV_time': None, 
                'continuation_output': None, 
                'continuation_time': None, 
                'greedy_output': None, 
                'greedy_time': None,
                'luby_output': None, 
                'luby_time': None,
                'blelloch_output': None, 
                'blelloch_time': None,
                'rpp_output': None, 
                'rpp_time': None
                }

    return new_row

def generate_graphs(number_of_runs, size_domain, overwrite=False):
    print('\nStart generating Erdos_renyi graphs')
    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/erdos_renyi_probability.csv')):
        print('Erdos-renyi - probability started.')
        # Generate Erdos-Renyi graphs
        rows = [ generate_row_erdos_renyi(60, np.log(60) / 60 +  k * (1 - np.log(60) / 60) / 10) for k in range(11) for i in range(number_of_runs) ]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/erdos_renyi_probability.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/erdos_renyi_probability.pkl'))

    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/erdos_renyi_size_sparse.csv')):
        print('Erdos-renyi - sparse started.')
        rows = [ generate_row_erdos_renyi(size, np.log(size) / size) for size in size_domain for i in range(number_of_runs)]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/erdos_renyi_size_sparse.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/erdos_renyi_size_sparse.pkl'))

    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/erdos_renyi_size_dense.csv')):
        print('Erdos-renyi - dense started.')
        rows = [ generate_row_erdos_renyi(size, 1/2) for size in size_domain for i in range(number_of_runs)]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/erdos_renyi_size_dense.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/erdos_renyi_size_dense.pkl'))
    
    print('Erdos_renyi graphs done.')

    # Generate random bipartite graphs
    print('\nStart generating random bipartite graphs')
    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/random_bipartite_probability.csv')):
        print('Random bipartite - probability started.')
        rows = [ generate_row_bipartite(30, 30, np.log(30) / 30 +  k * (1 - np.log(30) / 30) / 10) for k in range(11) for i in range(number_of_runs) ]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/random_bipartite_probability.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/random_bipartite_probability.pkl'))

    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/random_bipartite_size_sparse.csv')):
        print('Random bipartite - sparse started.')
        rows = [ generate_row_bipartite(int(size/2), int(size/2), np.log(size/2) / (size/2)) for size in size_domain for i in range(number_of_runs)]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/random_bipartite_size_sparse.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/random_bipartite_size_sparse.pkl'))

    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/random_bipartite_size_dense.csv')):
        print('Random bipartite - dense started.')
        rows = [ generate_row_bipartite(int(size/2), int(size/2), 1/2) for size in size_domain for i in range(number_of_runs)]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/random_bipartite_size_dense.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/random_bipartite_size_dense.pkl'))
    
    print('Random bipartite graphs done.')

    # Generate random geometric graphs
    print('\nStart generating random geometric graphs')
    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/random_geometric_probability.csv')):
        print('Random geometric - probability started.')
        rows = [ generate_row_geometric(60, 1.2*np.sqrt(np.log(60) / (np.pi * 60)) +  k * (np.sqrt(2) - 1.2*np.sqrt(np.log(60) / (np.pi * 60))) / 10) for k in range(11) for i in range(number_of_runs) ]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/random_geometric_probability.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/random_geometric_probability.pkl'))

    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/random_geometric_size_sparse.csv')):
        print('Random geometric - sparse started.')
        rows = [ generate_row_geometric(size, 1.2*np.sqrt(np.log(size) / (np.pi * size))) for size in size_domain for i in range(number_of_runs)]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/random_geometric_size_sparse.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/random_geometric_size_sparse.pkl'))

    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/random_geometric_size_dense.csv')):
        print('Random geometric - dense started.')
        rows = [ generate_row_geometric(size, 1/2) for size in size_domain for i in range(number_of_runs)]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/random_geometric_size_dense.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/random_geometric_size_dense.pkl'))
    
    print('Random geometric graphs generated')
        
    # Generate barabasi-albert graphs
    print('\nStart generating barabasi-albert graphs')
    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/barabasi_albert_probability.csv')):
        print('Barabasi-albert - probability started.')
        rows = [ generate_row_barabasi_albert(150, m) for m in [2, 4, 6, 8] for i in range(number_of_runs) ]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/barabasi_albert_probability.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/barabasi_albert_probability.pkl'))

    if overwrite or not os.path.exists(os.path.join(sys.path[0], 'data_empty/barabasi_albert_size_sparse.csv')):
        print('Barabasi-albert - sparse started.')
        rows = [ generate_row_barabasi_albert(size, 5) for size in size_domain for i in range(number_of_runs)]
        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(sys.path[0], 'data_empty/barabasi_albert_size_sparse.csv'), index=False)
        df.to_pickle(os.path.join(sys.path[0], 'data_empty/barabasi_albert_size_sparse.pkl'))
    
    print('Barabasi-albert graphs generated')