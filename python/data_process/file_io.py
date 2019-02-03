"""
Snippets to manipulate files
"""
import unittest
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


class DataFrameTest(unittest.TestCase):
    """DataFrame related operations """
    def test_read_csv(self):
        """ read CSV, and return a DataFrame"""
        df = pd.read_csv('sample-no-header.csv')
        self.assertEquals(type(df), pd.DataFrame)


def read_parquet(fn):
  """ read parquet file with Spark """
  print("Loading parquest file: %s..."% fn)
  file_name = 'parquet_sample.dat'
  read_parquest(file_name)
  fn = 'sample.parquet'
  tbl = pq.read_table(fn)
  df = tbl.to_pandas()
  d=df.iloc[:, 0:3]

  table = pa.Table.from_pandas(d)
  pq.write_table(table, 'example.parquet')

  pass


def write_parquet(df, fn):
  """ use DataFrame df to write parquet file name as fn """
  df.write.parquet(fn)


if __file__ == "__main__":
    unittest.main()

