# NEST Performance Benchmarks

This repository contains performance benchmark results for the NEST Simulator across different versions. The benchmarks
demonstrate NEST's scalability and performance characteristics on high-performance computing systems.

## Why do we have a separate repo for benchmark results?

The benchmark results are maintained in a separate repository for several practical reasons:

- **Independent release cycles**: Benchmark results can be updated and corrected without affecting NEST Simulator releases
- **Clean separation of concerns**: Keeps the main NEST repository focused on source code rather than generated artifacts
- **beNNch workflow flexibility**: When beNNch workflow improvements or bug fixes are made, we can re-run benchmarks for any NEST version without touching the NEST codebase
- **Repository size management**: Avoids bloating the main repository with large binary assets (benchmark images)
- **Specialized tooling**: Allows for documentation-specific configurations and workflows optimized for presenting benchmark results

## Documentation

This repo has its own dedicated Read the Docs page and is cross-linked to the main NEST Simulator documentation.


📖 **Read the Docs**: [Link to be added when documentation is published]

## About the Benchmarks

The performance benchmarks in this repository are generated using the **BeNNch workflow**.
This standardized benchmarking framework allows for consistent performance evaluation across different
NEST versions and computing environments.

### Benchmark Types

The repository includes three main types of performance benchmarks:

1. **Microcircuit Model** - Strong scaling experiments with ~80,000 neurons and ~300 million synapses
2. **Multi-area Model** - Strong scaling experiments with ~4.1 million neurons and ~24 billion synapses
3. **HPC Benchmark Model** - Weak scaling experiments scaling up to ~5.8 million neurons and ~65 billion synapses

Each benchmark includes performance visualizations showing:
- Simulation time vs. number of compute resources
- Strong scaling and weak scaling characteristics

## Adding New Benchmark Results

When NEST is preparing for a new release, we need to run the benchmarks from the NEST release candidate. Once completed,
a new entry needs to be created in this repository and the index page needs to be updated.

### Process for Adding New Results

1. **Run benchmarks** on the NEST release candidate using the BeNNch workflow
2. **Create a new benchmark results page** following the naming convention: `nest<version>_benchmark_results.rst`
3. **Update the index page** (`source/index.rst`) to include a link to the new results
4. **Add benchmark images** to the `source/_static/img/` directory with version-specific naming
5. **Update the toctree** in the index to maintain proper navigation

### File Naming Convention

- Benchmark results pages: `<version>_benchmark_results.rst`
- Benchmark images: `<benchmark_type>_benchmark_NEST-v<version>.png`
- Example: `v3.10_benchmark_results.rst` with images like `mc_benchmark_NEST-v3.10.png`

### Version Management

We maintain all benchmark versions (starting with v3.8) to provide a historical record of NEST's performance evolution.
Each version gets its own dedicated page, ensuring that previous results remain accessible while new results are
prominently featured.

## Repository Structure

```
source/
├── index.rst                           # Main index page
├── benchmark_results.rst              # Latest benchmark results
├── <version>_benchmark_results.rst   # Version-specific results
├── _static/img/                       # Benchmark images
└── conf.py                           # Sphinx configuration
```

## Building the Documentation

The documentation is built using Sphinx with the Material theme. To build locally:

```bash
# Install requirements
pip install -r requirements.txt

# Build the documentation
sphinx-build source/ build/
```

The built documentation will be available in the `build/html/` directory.
