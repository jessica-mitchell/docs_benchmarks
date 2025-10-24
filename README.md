# NEST Performance Benchmarks

This repository contains performance benchmark results for the NEST Simulator across different versions. The benchmarks demonstrate NEST's scalability and performance characteristics on high-performance computing systems.

## Documentation

📖 **Read the Docs**: [Link to be added when documentation is published]

## About the Benchmarks

The performance benchmarks in this repository are generated using the **BeNNch workflow** (Benchmarking Neural Network Simulations). This standardized benchmarking framework allows for consistent performance evaluation across different NEST versions and computing environments.

### Benchmark Types

The repository includes three main types of performance benchmarks:

1. **Microcircuit Model** - Strong scaling experiments with ~80,000 neurons and ~300 million synapses
2. **Multi-area Model** - Strong scaling experiments with ~4.1 million neurons and ~24 billion synapses
3. **HPC Benchmark Model** - Weak scaling experiments scaling up to ~5.8 million neurons and ~65 billion synapses

Each benchmark includes performance visualizations showing:
- Simulation time vs. number of compute resources
- Strong scaling and weak scaling characteristics
- Error bars indicating standard deviation across multiple runs

## Adding New Benchmark Results

When NEST is preparing for a new release, we need to run the benchmarks from the NEST release candidate. Once completed, a new entry needs to be created in this repository and the index page needs to be updated.

### Process for Adding New Results

1. **Run benchmarks** on the NEST release candidate using the BeNNch workflow
2. **Create a new benchmark results page** following the naming convention: `nest<version>_benchmark_results.rst`
3. **Update the index page** (`source/index.rst`) to include a link to the new results
4. **Add benchmark images** to the `source/_static/img/` directory with version-specific naming
5. **Update the toctree** in the index to maintain proper navigation

### File Naming Convention

- Benchmark results pages: `nest<version>_benchmark_results.rst`
- Benchmark images: `<benchmark_type>_benchmark_NEST-v<version>.png`
- Example: `nest3.10_benchmark_results.rst` with images like `mc_benchmark_NEST-v3.10.png`

### Version Management

We maintain all benchmark versions to provide a historical record of NEST's performance evolution. Each version gets its own dedicated page, ensuring that previous results remain accessible while new results are prominently featured.

## Repository Structure

```
source/
├── index.rst                           # Main index page
├── benchmark_results.rst              # Latest benchmark results
├── nest<version>_benchmark_results.rst # Version-specific results
├── _static/img/                       # Benchmark images
└── conf.py                           # Sphinx configuration
```

## Building the Documentation

The documentation is built using Sphinx with the Material theme. To build locally:

```bash
# Install requirements
pip install -r requirements.txt

# Build the documentation
make html
```

The built documentation will be available in the `build/html/` directory.
