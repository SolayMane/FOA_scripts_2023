
import pandas as pd
import matplotlib.pyplot as plt

# Load the RepeatMasker output ( parsed by Parsing-RepeatMasker-Outputs/parseRM.pl script) file into a pandas DataFrame
df = pd.read_csv("RepeatMasker.out", sep="\t", engine="python", skiprows=3,
                 names=["repeat_name", "repeat_class", "repeat_family", "repeat_length", "num_occurrences_all", "num_occurrences_reconstructed",
                        "length_masked_nonredundant", "avg_percent_divergence", "med_percent_divergence", "avg_percent_deletion",
                        "med_percent_deletion", "avg_percent_insertion", "med_percent_insertion", "avg_length_masked", "percent_genome"])

# Group the repeats by class and family
grouped = df.groupby(["repeat_class", "repeat_family"])

# Calculate the percentage of genome covered by each repeat class and family
percent_genome = grouped["percent_genome"].sum() * 100

# Reset the index to make it a single-level index
percent_genome = percent_genome.reset_index()

# Pivot the data to create a matrix with repeat families as columns and repeat classes as rows
pivoted = percent_genome.pivot(index="repeat_class", columns="repeat_family", values="percent_genome")

# Create a stacked horizontal bar chart of the percentage of genome covered by each repeat class and family
fig, ax = plt.subplots(figsize=(10, 10))
colors = plt.cm.Set3(range(len(pivoted.columns)))
for i, repeat_family in enumerate(pivoted.columns):
    ax.barh(pivoted.index, pivoted[repeat_family], left=pivoted.iloc[:, :i].sum(axis=1), color=colors[i], label=repeat_family)
ax.set_xlabel("Percentage of genome covered")
ax.set_ylabel("Repeat class")
ax.set_title("RepeatMasker results by repeat class and family")
ax.legend(loc="upper right")
#plt.show()


# Adjust the layout of the subplots
plt.tight_layout()
