# visualise-large-dataset
Example showing how to visualise ~20GB of data using [plothist](https://plothist.readthedocs.io) and [pyarrow](https://arrow.apache.org/docs/python/index.html).


* `generate_data.py` generates a data file `data.pq` of ~20GB using `plothist` (takes ~3min).
* `plot_data.py` plots the generated data using `pyarrow` and `plothist` (takes ~1min).

This is the resulting plot:
![variable.svg](https://raw.githubusercontent.com/cyrraz/visualise-large-dataset/077a162645e40d709b0393e25efeafa5a8c9ca6d/variable.svg)
