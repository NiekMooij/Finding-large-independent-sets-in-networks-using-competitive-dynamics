import numpy as np
import networkx as nx
import pandas as pd
import os
import sys

import MIS_algorithms as MIS
from generate_graphs import generate_graphs
from analyse_graphs import analyse_graphs
from histogram import get_histograms

if __name__ == '__main__':
    number_of_runs = 1000
    size_domain = [ 10, 16, 36, 46, 66, 90, 130, 160, 200 ]
    save_after_n_runs = 100

    generate_graphs(number_of_runs, size_domain, overwrite=False)
    print('All graphs generated')
    
    analyse_graphs(save_after_n_runs)
    print('All graphs analysed')

    get_histograms()
    print('All histograms generated')