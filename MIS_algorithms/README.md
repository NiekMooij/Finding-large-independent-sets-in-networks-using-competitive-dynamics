## Overview

This Python package provides efficient algorithms for calculating maximal independent sets in graphs. The project includes various scripts in the `MIS-algorithms` folder, each implementing a different algorithm for computing these sets. The Lotka-Volterra Algorithm and the Continuation Lotka-Volterra Algorithm are both described in the paper "Finding Large Independent Sets in Networks Using Competitive Dynamics".

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)
- [Contact](#contact)

## Features

- **Lotka-Volterra Algorithm:** Efficient implementation of the Lotka-Volterra algorithm for maximal independent set calculation.
- **Continuation Algorithm:** The Continuation Clgorithm to find maximal independent sets in graphs.
- **Minimum Degree Greedy Algorithm:** Implementation of the Minimum Degree Greedy algorithm for maximal independent set approximation, where we select vertices based on the minimum degree.
- **Exact Algorithm:** An exact algorithm to find the exact maximal independent set in a given graph. Used much functionality from the PuLP package!
- **Random-Priority Parallel Algorithm:** An approximation algorithm to the maximum independent set problem.
- **Luby Algorithm:** An approximation algorithm to the maximum independent set problem.
- **Blelloch Algorithm:** An approximation algorithm to the maximum independent set problem.

## Installation

You can install the package using pip (~20 seconds on MacBook Pro 2022 Sonoma 14.7 (Apple M2, RAM 16GB)):
```bash
pip install MIS-algorithms
```

## Example

```python
import MIS_algorithms as MIS
LV_output  = MIS.lotka_volterra(G, tau=1.1, x0=np.random.random(len(G)))
continuation_output  = MIS.continuation(G)
greedy_output  = MIS.greedy(G)
rpp_output  = MIS.random_priority_parallel(G)
luby_output  = MIS.luby(G)
blelloch_output  = MIS.blelloch(G)
```

## Usage
To use the package, import the relevant script from the MIS folder based on the algorithm you'd like to apply.

## Configuration
No specific configuration is required.

## License
This package is distributed under the MIT license.

## Contact
You can contact me at mooij.niek@gmail.com for any questions or suggestions.