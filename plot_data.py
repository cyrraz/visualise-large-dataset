import pyarrow.parquet as pq
from plothist import make_hist, plot_hist
import matplotlib.pyplot as plt

parquet_file = pq.ParquetFile("data.pq")
batch_size = int(1e7)

range_ = (0, 6)
bins = 50

hist = make_hist(data=[], range=range_, bins=bins)

for batch in parquet_file.iter_batches(batch_size=batch_size, columns=["variable"]):
    hist.fill(batch.column("variable"), threads=0)

fig, ax = plt.subplots()

plot_hist(hist, ax=ax, label="Data")

ax.set_xlabel("Variable")
ax.set_ylabel("Entries")
ax.set_xlim(range_)

ax.legend()

fig.savefig("variable.svg", bbox_inches="tight")
