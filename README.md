# Genetic Algorithm TSP Solver

An optimized genetic algorithm engine for solving large-scale 3D Travelling Salesman Problem (TSP) instances with adaptive parameter tuning, intelligent initialization strategies, and custom evolutionary operators.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![NumPy](https://img.shields.io/badge/numpy-required-orange.svg)](https://numpy.org/)

## 📋 Overview

This project implements a sophisticated genetic algorithm to solve the Travelling Salesman Problem in 3D space. The algorithm efficiently handles problem instances ranging from small datasets (< 10 cities) to large-scale problems (6000+ cities) through adaptive parameter tuning and multiple optimization strategies.

### Key Features

- **Adaptive Parameter Tuning**: Automatically adjusts population size, mutation rate, and generation count based on problem size
- **Hybrid Approach**: Combines genetic algorithms with greedy heuristics and brute-force methods for optimal performance
- **Intelligent Initialization**: Uses multiple seeding strategies including lexicographic sorting and greedy nearest-neighbor
- **Distance Caching**: Pre-computes and caches all city-to-city distances for O(1) lookups
- **Elitism Strategy**: Preserves top-performing solutions across generations
- **Custom Crossover**: Implements ordered crossover to maintain valid tour sequences
- **Smart Mutation**: Applies adaptive swap mutations with configurable rates

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- NumPy

```bash
pip install numpy
```

### Basic Usage

1. **Generate a random test case:**
```bash
python input_generator.py
```

2. **Run the optimized solver:**
```bash
python improved_test_solver.py
```

3. **Check the results:**
The solution will be written to `output.txt` with the format:
```
<total_distance>
<city1_x> <city1_y> <city1_z>
<city2_x> <city2_y> <city2_z>
...
<city1_x> <city1_y> <city1_z>  # Returns to start
```

## 📁 Project Structure

```
genetic-algorithm-tsp-solver/
├── GeneticAlgorithm_TSP/
│   ├── improved_test_solver.py    # Main optimized solver with adaptive parameters
│   ├── basic_test_solver.py       # Basic solver with manual parameter tuning
│   ├── input_generator.py         # Random test case generator
│   ├── time_test_code.py          # Performance timing and benchmarking
│   ├── input.txt                  # Current problem instance
│   ├── output.txt                 # Solution output
│   └── log.txt                    # Execution logs
├── LICENSE                        # MIT License
└── README.md                      # This file
```

## 🔧 Detailed Usage

### Input Generator

Generate custom test cases with specific parameters:

```bash
# Generate with fixed number of cities
python input_generator.py --fixed_size 100

# Set maximum coordinate value
python input_generator.py --max_coord 5000

# Set maximum random city count
python input_generator.py --max_size 1000

# Combine parameters
python input_generator.py --fixed_size 500 --max_coord 10000
```

**Input Format:**
```
N
x1 y1 z1
x2 y2 z2
...
xN yN zN
```

Where `N` is the number of cities, and each subsequent line contains 3D coordinates.

### Basic Solver

Run with custom genetic algorithm parameters:

```bash
# Set breeding population size
python basic_test_solver.py --bpop 200

# Set mutation rate (percentage)
python basic_test_solver.py --mr 10

# Set maximum generations
python basic_test_solver.py --mpop 500

# Set gene pool division factor
python basic_test_solver.py --part 3

# Combine parameters
python basic_test_solver.py --bpop 150 --mr 5 --mpop 1000
```

### Improved Solver

The improved solver automatically optimizes parameters based on problem size:

```bash
python improved_test_solver.py
```

**Adaptive Parameter Table:**

| Cities      | Population | Mutation Rate | Generations | Strategy         |
|-------------|-----------|---------------|-------------|------------------|
| ≤ 6         | 5000      | 1%            | 1           | Brute Force      |
| 7-50        | 128       | 8%            | 1500        | GA + Greedy      |
| 51-100      | 128       | 8%            | 1024        | GA + Greedy      |
| 101-200     | 64        | 8%            | 1024        | GA + Greedy      |
| 201-500     | 64        | 4%            | 512         | GA + Greedy      |
| 501-1000    | 32        | 4%            | 400         | GA + Greedy      |
| 1001-2000   | 32        | 8%            | 256         | GA + Greedy      |
| 2001-4000   | 16        | 8%            | 128         | GA Only          |
| 4001-6000   | 16        | 8%            | 64          | GA Only          |
| 6000+       | 16        | 8%            | 32          | GA Only          |

### Performance Testing

Run with timing analysis:

```bash
python time_test_code.py
```

Results are logged to `log.txt` with execution time and solution quality.

## 🧬 Algorithm Details

### Initialization Strategies

1. **Lexicographic Sorting**: 6 different orderings based on coordinate priorities
2. **Greedy Nearest Neighbor**: 3 randomized greedy paths (for problems < 4000 cities)
3. **Random Permutations**: Fill remaining population slots

### Fitness Evaluation

- Calculates total Euclidean distance for complete tour
- Uses pre-computed distance lookup table for efficiency
- Complexity: O(n) per solution evaluation

### Selection

- **Elitism**: Top 50% of population automatically advances
- **Tournament Selection**: Remaining slots filled via reproduction

### Crossover (Reproduction)

- **Ordered Crossover**: Preserves relative gene ordering
- Random segment from parent 1, remaining cities from parent 2
- Maintains tour validity (no duplicate cities)

### Mutation

- **Adjacent Swap**: Swaps neighboring cities based on mutation rate
- **Boundary Mutation**: 5% chance to swap first and last cities
- Prevents premature convergence

### Termination

Fixed number of generations based on problem size, with early stopping if no improvement.

## 📊 Performance Characteristics

- **Small Problems (< 10 cities)**: Near-optimal solutions via brute force
- **Medium Problems (10-1000 cities)**: High-quality solutions in seconds
- **Large Problems (1000-4000 cities)**: Good approximate solutions in under a minute
- **Very Large Problems (4000+ cities)**: Reasonable solutions with reduced generation count

## 🛠️ Implementation Notes

### Key Optimizations

1. **Distance Caching**: All pairwise distances computed once at initialization
2. **NumPy Vectorization**: Efficient array operations for population management
3. **Partial Fitness Evaluation**: Only re-evaluate modified solutions
4. **Memory-Efficient**: Reuses arrays to minimize allocations

### Limitations

- Requires sufficient RAM for distance lookup table: O(n²) space
- Very large problems (> 6000 cities) may need parameter tuning
- 3D coordinates only (can be adapted for 2D)

## 📝 Input/Output Examples

### Example Input (`input.txt`)
```
4
1000 2000 1500
3000 2500 1000
2000 1000 3000
1500 3500 2000
```

### Example Output (`output.txt`)
```
8246
1000 2000 1500
2000 1000 3000
3000 2500 1000
1500 3500 2000
1000 2000 1500
```

The first line shows the total distance, followed by the optimal tour sequence, ending by returning to the starting city.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Code improvements
- Parallelizing fitness calculation
- Alternative crossover operators (PMX, CX)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Nikhil Singla**
