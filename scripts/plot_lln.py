import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--files", nargs="+")
parser.add_argument("--n", type=int)
parser.add_argument("--out", type=str)
args = parser.parse_args()

df = pd.concat([pd.read_csv(f) for f in args.files])

# Convert 'k' to a categorical type so it sorts numerically on the X-axis
df['k_val'] = df['k'].str.replace('k=', '').astype(int)
df = df.sort_values('k_val')

plt.figure(figsize=(12, 6))
sns.boxplot(x="k", y="mean_val", data=df, color="white")
plt.axhline((args.n + 1) / 2, color='red', linestyle='--', label=f"True Mean ({(args.n+1)/2})")
plt.title(f"Law of Large Numbers: Testing Draws for {args.n}")
plt.xlabel("Number of Draws (k)")
plt.ylabel("Sample Mean")
plt.legend()
plt.savefig(args.out)
