# visualise-large-dataset
Example showing how to visualise 20GB of data using [plothist](https://plothist.readthedocs.io) and [pyarrow](https://arrow.apache.org/docs/python/index.html).
The data are generated/loaded in batches so that the required memory is only ~2GB.
The hardware used to measure the running times is reported at the end of this page.

* `generate_data.py` generates a data file `data.pq` of ~20GB using `pyarrow` (takes ~3min).
* `plot_data.py` plots the generated data using `plothist` and `pyarrow` (takes ~30s).
* `plot_categorised_weighted_data.py` plots the generated data using `plothist` and `pyarrow`, taking into account different data categories and a specific weight for each entry (takes ~1min).

This is the resulting plot of `plot_data.py`:

![variable.svg](https://raw.githubusercontent.com/cyrraz/visualise-large-dataset/main/variable.svg)

And the result of `plot_categorised_weighted_data.py`:

![variable_categorised_weighted.svg](https://raw.githubusercontent.com/cyrraz/visualise-large-dataset/main/variable_categorised_weighted.svg)

## Hardware used
* CPU: Intel Core i5-1235U
* RAM: 16GB DDR4, 3200 MT/s
* Disk: 500GB SSD, Read/Write Speed: 2.1/1.1 GB/s

*This repository is dedicated to N.K.R.*
