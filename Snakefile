# --- CONFIGURATION ---
N_VAL = 2000
K_VALS = [5, 10, 25, 50, 100, 200, 1000, 2000]
TRIALS = 10

# Use max() to find the largest k value for the filename
K_MAX = max(K_VALS)
FINAL_PLOT = f"plots/lln_n{N_VAL}_kmax{K_MAX}.png"

rule all:
    input: FINAL_PLOT

rule simulate:
    output: "data/means_k{k}.csv"
    params:
        n = N_VAL,
        t = TRIALS
    shell:
        "python3 scripts/simulate.py --n {params.n} --k {wildcards.k} "
        "--trials {params.t} --out {output}"

rule plot:
    input: expand("data/means_k{k}.csv", k=K_VALS)
    output: FINAL_PLOT
    params:
        n = N_VAL
    shell:
        "python3 scripts/plot_lln.py --files {input} --n {params.n} --out {output}"
