import numpy as np
import os
import sys
import pandas as pd
from scipy import stats

def confidence_interval(data, confidence=0.95):
    """
    Calculate the confidence interval for the mean of the data.

    Parameters:
        data (list or array-like): The input data.
        confidence (float, optional): The desired confidence level (default is 0.95).

    Returns:
        tuple: A tuple (lower_bound, upper_bound) representing the confidence interval.
    """
    data = np.array(data)
    mean = np.mean(data)
    std_error = stats.sem(data)
    # std = np.std(data)
    lower_bound = mean - std_error
    upper_bound = mean + std_error
    return [lower_bound, upper_bound]
        
def data_analysis(type):
    file_loc = os.path.join(sys.path[0], "data_raw/" + type + ".pkl")
    df = pd.read_pickle(file_loc)

    # Determine length of the outputs
    for key in ['exact_output', 'LV_output', 'continuation_output', 'greedy_output', 'luby_output', 'blelloch_output', 'rpp_output']:
        df[key] = df[key].apply(lambda x: len(x))
        
    if type == "random_geometric_probability":
        df.rename(columns={'r_radius': 'p_connection'}, inplace=True)

    if type == "barabasi_albert_probability":
        df.rename(columns={'m': 'p_connection'}, inplace=True)

    # Determine the average performance per size
    df_means = pd.DataFrame(columns=['size', 'p_connection', 'LV_app', 'LV_app_CI_lower', 'LV_app_CI_upper', 'continuation_app', 'continuation_app_CI_lower', 'continuation_app_CI_upper', 'greedy_app', 'greedy_app_CI_lower', 'greedy_app_CI_upper', 'luby_app', 'luby_app_CI_lower', 'luby_app_CI_upper', 'blelloch_app', 'blelloch_app_CI_lower', 'blelloch_app_CI_upper', 'rpp_app', 'rpp_app_CI_lower', 'rpp_app_CI_upper'])
    for p_connection in sorted(list(set(df['p_connection']))):

        df_p = df[df['p_connection'] == p_connection]
        df_p.drop(['vertices', 'edges'], axis=1, inplace=True)
    
        LV_app = np.array(df_p['LV_output'] / df_p['exact_output'])
        continuation_app = np.array(df_p['continuation_output'] / df_p['exact_output'])
        greedy_app = np.array(df_p['greedy_output'] / df_p['exact_output'])
        luby_app = np.array(df_p['luby_output'] / df_p['exact_output'])
        blelloch_app = np.array(df_p['blelloch_output'] / df_p['exact_output'])
        rpp_app = np.array(df_p['rpp_output'] / df_p['exact_output'])
        
        confidence_level=0.99
        
        averages = {
            'size': 60,
            'p_connection': p_connection, 
            
            'LV_app': np.mean(LV_app), 
            'LV_app_CI_lower': confidence_interval(LV_app, confidence_level)[0], 
            'LV_app_CI_upper': confidence_interval(LV_app, confidence_level)[1], 

            'continuation_app': np.mean(continuation_app), 
            'continuation_app_CI_lower': confidence_interval(continuation_app, confidence_level)[0],
            'continuation_app_CI_upper': confidence_interval(continuation_app, confidence_level)[1],

            'greedy_app': np.mean(greedy_app),
            'greedy_app_CI_lower': confidence_interval(greedy_app, confidence_level)[0],
            'greedy_app_CI_upper': confidence_interval(greedy_app, confidence_level)[1],

            'luby_app': np.mean(luby_app),
            'luby_app_CI_lower': confidence_interval(luby_app, confidence_level)[0],
            'luby_app_CI_upper': confidence_interval(luby_app, confidence_level)[1],
            
            'blelloch_app': np.mean(blelloch_app),
            'blelloch_app_CI_lower': confidence_interval(blelloch_app, confidence_level)[0],
            'blelloch_app_CI_upper': confidence_interval(blelloch_app, confidence_level)[1],
            
            'rpp_app': np.mean(rpp_app),
            'rpp_app_CI_lower': confidence_interval(rpp_app, confidence_level)[0],
            'rpp_app_CI_upper': confidence_interval(rpp_app, confidence_level)[1]
        }

        df_new = pd.DataFrame(averages, index=[0])
        df_means = pd.concat([df_means, df_new], ignore_index=True)
        
    if type == "random_geometric_probability":
        df_means.rename(columns={'p_connection': 'r_radius'}, inplace=True)
                
    if type == "barabasi_albert_probability":
        df_means.rename(columns={'p_connection': 'm'}, inplace=True)
                
    df_means.to_csv(os.path.join(sys.path[0], "data_analysed/" + type + ".csv"), index=False)
    df_means.to_pickle(os.path.join(sys.path[0], "data_analysed/" + type + ".pkl"))
    
if __name__ == '__main__':
    types = [
             "erdos_renyi_probability",
             "random_bipartite_probability",
             "random_geometric_probability",
             "barabasi_albert_probability"
             ]

    for t in types:
        data_analysis(t)
    