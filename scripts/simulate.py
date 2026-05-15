import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int)
parser.add_argument("--k", type=int)
parser.add_argument("--trials", type=int)
parser.add_argument("--out", type=str)
args = parser.parse_args()

# Generate 'trials' number of means, each from 'k' random draws between 1 and n
means = [np.mean(np.random.randint(1, args.n + 1, args.k)) for _ in range(args.trials)]

df = pd.DataFrame({"k": [f"k={args.k}"] * args.trials, "mean_val": means})
df.to_csv(args.out, index=False)
