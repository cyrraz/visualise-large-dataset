import pyarrow.parquet as pq
from plothist import make_hist, plot_hist
import matplotlib.pyplot as plt

parquet_file = pq.ParquetFile("data.pq")
batch_size = int(1e7)

range_ = (0, 6)
bins = 50

hist_normal = make_hist(range=range_, bins=bins)
hist_exponential = make_hist(range=range_, bins=bins)
hist_log_normal = make_hist(range=range_, bins=bins)

for batch in parquet_file.iter_batches(batch_size=batch_size):
    variable = batch.column("variable").to_pandas(zero_copy_only=True).values
    category = batch.column("category").to_pandas(zero_copy_only=True).values
    weight = batch.column("weight").to_pandas(zero_copy_only=True).values

    hist_normal.fill(variable[category == 0], weight=weight[category == 0], threads=0)
    hist_exponential.fill(variable[category == 1], weight=weight[category == 1], threads=0)
    hist_log_normal.fill(variable[category == 2], weight=weight[category == 2], threads=0)

fig, ax = plt.subplots()

plot_hist(
    [hist_normal, hist_exponential, hist_log_normal],
    ax=ax,
    stacked=True,
    label=["Gaussian", "Exponential", "Log-normal"],
    edgecolor="black",
    linewidth=0.5,
    histtype="stepfilled"
    )

ax.set_xlabel("Variable")
ax.set_ylabel("Entries")
ax.set_xlim(range_)

ax.legend(reverse=True)

fig.savefig("variable_categorised_weighted.svg", bbox_inches="tight")
