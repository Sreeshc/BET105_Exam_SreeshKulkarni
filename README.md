# Law of Large Numbers (LLN) Simulation

## 📊 Overview
This project is a Snakemake-powered simulation demonstrating the **Law of Large Numbers**. It explores how the sample mean of random integers drawn from a range $[1, n]$ converges to the theoretical mean as the number of draws ($k$) increases.

## 📈 Visual Result
For this simulation, the range was set to $n=2000$. The theoretical mean is **1000.5**.

![LLN Convergence Plot](plots/lln_convergence_n2000.png)

*As seen in the boxplot, the variance of the sample means significantly decreases as $k$ approaches 5000, illustrating the stabilization of the mean.*

## 🛠️ Pipeline Architecture
The workflow is managed via **Snakemake**, ensuring a reproducible and modular analysis:
1. **Simulation:** Generates 50 trials of $k$ random draws for each specified value of $k$.
2. **Aggregation:** Collects individual trial results into a structured dataset.
3. **Visualization:** Produces a categorical boxplot showing the distribution of means.

## 🚀 Minimal Effort Reproduction
To run this pipeline or modify the parameters (e.g., adding $k=10000$ or changing $n$):

1. **Modify the configuration** at the top of the `Snakefile`:
   - `N_VAL`: Set the upper limit (e.g., 2000).
   - `K_VALS`: Add any additional draw counts to the list.

2. **Execute the pipeline:**
   ```bash
   snakemake --cores all
