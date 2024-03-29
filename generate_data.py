import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path

filename = "data.pq"
total_size = int(2e10)
batch_size = int(1e7)

# Define schema for the Parquet file
schema = pa.schema(
    [("variable", pa.float64()), ("category", pa.int8()), ("weight", pa.int64())]
)


# Check if the file already exists
file_path = Path(filename)
if file_path.exists():
    raise FileExistsError(f"File {filename} already exists.")


with pq.ParquetWriter(filename, schema) as writer:
    while file_path.stat().st_size < total_size:
        array_variable = np.concatenate(
            [
                np.random.normal(loc=3, size=batch_size),
                np.random.exponential(size=batch_size),
                np.random.lognormal(size=batch_size),
            ]
        )
        array_category = np.concatenate(
            [
                np.zeros(batch_size, dtype=np.int8),
                np.ones(batch_size, dtype=np.int8),
                2 * np.ones(batch_size, dtype=np.int8),
            ]
        )
        array_weight = np.random.poisson(size=3 * batch_size)

        # Convert the NumPy array to a PyArrow Table
        table = pa.Table.from_arrays(
            [array_variable, array_category, array_weight],
            names=["variable", "category", "weight"],
        )

        # Save the Table as a Parquet file
        writer.write_table(table)

print(f"Created a Parquet file.")
