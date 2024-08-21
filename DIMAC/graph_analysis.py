import os
import sys
import numpy as np
import networkx as nx
import time
import pandas as pd
import MIS_algorithms as MIS

def update_row(row: dict) -> dict:
    """Calculate output values and update row."""
    
    if row['LV_output'] == None or row['continuation_output'] == None or row['greedy_output'] == None:
                
        # Define networkx graph
        G = nx.Graph()
        G.add_nodes_from(row['vertices'])
        G.add_edges_from(row['edges'])
            
        start_time = time.time()
        maximum_count = 0
        for i in range(10):
            LV_output_temp  = MIS.lotka_volterra(G, tau=1.1, x0=np.random.random(len(G)))
            if len(LV_output_temp) > maximum_count:
                LV_output = LV_output_temp
        LV_time = time.time() - start_time
        
        start_time = time.time()
        continuation_output  = MIS.continuation(G)
        continuation_time = time.time() - start_time
        
        start_time = time.time()
        maximum_count = 0
        for i in range(10):
            greedy_output_temp  = MIS.greedy(G)
            if len(greedy_output_temp) > maximum_count:
                greedy_output = greedy_output_temp
        greedy_time = time.time() - start_time
        
        start_time = time.time()
        maximum_count = 0
        for i in range(10):
            rpp_output_temp  = MIS.random_priority_parallel(G)
            if len(rpp_output_temp) > maximum_count:
                rpp_output = rpp_output_temp
        rpp_time = time.time() - start_time
        
        start_time = time.time()
        maximum_count = 0
        for i in range(10):
            luby_output_temp  = MIS.luby(G)
            if len(luby_output_temp) > maximum_count:
                luby_output = luby_output_temp
        luby_time = time.time() - start_time
        
        start_time = time.time()
        maximum_count = 0
        for i in range(10):
            blelloch_output_temp  = MIS.blelloch(G)
            if len(blelloch_output_temp) > maximum_count:
                blelloch_output = blelloch_output_temp
        blelloch_time = time.time() - start_time
    
    row['LV_output'] = LV_output
    row['LV_time'] = LV_time
    row['continuation_output'] = continuation_output
    row['continuation_time'] = continuation_time
    row['greedy_output'] = greedy_output
    row['greedy_time'] = greedy_time
    row['rpp_output'] = rpp_output
    row['rpp_time'] = rpp_time
    row['luby_output'] = luby_output
    row['luby_time'] = luby_time
    row['blelloch_output'] = blelloch_output
    row['blelloch_time'] = blelloch_time

    return row

def save_data(df: pd.DataFrame):
    """Save dataframe to csv and pickle format."""
    start_time = time.time()
    df.to_csv(os.path.join(sys.path[0], 'data_raw/' + "DIMAC" + '.csv'), header=True, index=False)
    df.to_pickle(os.path.join(sys.path[0], 'data_raw/' + "DIMAC" + '.pkl'))
    save_time = time.time() - start_time  
    print(f'Data saved in {np.round(save_time,3)} seconds.')
    
def analyse_graphs():
    """
    Function to analyze graph data stored in a DataFrame, update each row of the DataFrame, 
    save the updated DataFrame, and print status messages.

    Returns:
    None
    """

    # Check if the raw data file exists, if not, check if the empty data file exists
    if os.path.exists(os.path.join(sys.path[0], 'data_raw/' + 'DIMAC' + '.pkl')):
        df = pd.read_pickle(os.path.join(sys.path[0], 'data_raw/' + 'DIMAC' + '.pkl'))
    elif os.path.exists(os.path.join(sys.path[0], 'data_empty/' + 'DIMAC' + '.pkl')):
        df = pd.read_pickle(os.path.join(sys.path[0], 'data_empty/' + 'DIMAC' + '.pkl'))
    else:
        print('No test graphs generated.')
        return

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        row_updated = update_row(row)
        df.iloc[index] = pd.Series(row_updated)

        # Save the updated DataFrame
        save_data(df)
        print('Network analysed.')

if __name__ == '__main__':
    analyse_graphs()