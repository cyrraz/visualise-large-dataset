# visualise-large-dataset
Example showing how to visualise ~20GB of data using [plothist](https://plothist.readthedocs.io) and [pyarrow](https://arrow.apache.org/docs/python/index.html).
The data are generated/loaded in batches so that the required memory is only ~2GB.

* `generate_data.py` generates a data file `data.pq` of ~20GB using `pyarrow` (takes ~3min).
* `plot_data.py` plots the generated data using `pyarrow` and `plothist` (takes ~30s).
* `plot_categorised_weighted_data.py` plots the generated data using `pyarrow` and `plothist`, taking into account different data categories and a specific weight for each entry (takes ~1min).

This is the resulting plot of `plot_data.py`:

![variable.svg](https://raw.githubusercontent.com/cyrraz/visualise-large-dataset/main/variable.svg)

And the result of `plot_categorised_weighted_data.py`:

![variable_categorised_weighted.svg](https://raw.githubusercontent.com/cyrraz/visualise-large-dataset/main/variable_categorised_weighted.svg)
