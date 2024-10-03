import numpy as np
import networkx as nx
import pandas as pd
import os
import sys

import MIS_algorithms as MIS
from generate_graphs import generate_graphs
from analyse_graphs import analyse_graphs

if __name__ == '__main__':
    number_of_runs = 10
    size_domain = [ 10, 20, 30 ]
    save_after_n_runs = 10

    generate_graphs(number_of_runs, size_domain, overwrite=False)
    print('All graphs generated')
    
    analyse_graphs(save_after_n_runs)