from deltalake import DeltaTable, write_deltalake
import pandas as pd


# Write a Pandas DataFrame to a Delta table
df = pd.DataFrame({"id": [1, 2, 3], "value": ["a", "b", "c"]})
write_deltalake("path/to/delta-table", df)

# Read the Delta table
dt = DeltaTable("path/to/delta-table")
pandas_df = dt.to_pandas()
print(pandas_df)
