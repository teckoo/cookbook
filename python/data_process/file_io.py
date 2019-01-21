"""
Snippets to manipulate files
"""
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

import unittest


class DataFrameTest(unittest.TestCase):
    """DataFrame related operations """
    def test_read_csv(self):
        """ read CSV, and return a DataFrame"""
        df = pd.read_csv('sample.csv')
        self.assertEquals(type(df), pd.DataFrame)


def read_parquet(fn):
  """ read parquet file with Spark """
  print("Loading parquest file: %s..."% fn)
  pass


def write_parquet(df, fn):
  """ use DataFrame df to write parquet file name as fn """
  df.write.parquet(fn)

if __file__ == "__main__":
  file_name = 'parquet_sample.dat'
  read_parquest(file_name)
  fn = '20190106232202_CapOne_FraudVerified_Tenant.parquet'
  tbl = pq.read_table(fn)
  df = tbl.to_pandas()
  d=df.iloc[:, 0:3]

  'CASE_LEVEL_CD' 'CASE_REFERENCE_NUM' 'CREATED_BY_MODULE_CD'
  d.loc['CASE_REFERENCE_NUM'] = d['CASE_LEVEL_CD'].apply(lambda x: x[:4])

  d.iloc[:, 2] = 'TRY'
  d.iloc[:, 1] = d.iloc[:, 2].apply(lambda x: x[:1])
  col_def = [(0, 4), (4, 21), (21, 50)] 
  col_def = [(0, 16), (16, 50), (21, 50)] 

  for idx in range(1, col_len):
    d.iloc[:, i] = d.iloc[:, 0].apply(lambda x: x[col_def[idx][0]:col_def[idx[1]])
  d.iloc[:, 1] = d.iloc[:, 0].apply(lambda x: x[16:56])
  d.iloc[:, 2] = d.iloc[:, 0].apply(lambda x: x[56:72])
  d.iloc[:, 0] = d.iloc[:, 0].apply(lambda x: x[:16])

  table = pa.Table.from_pandas(d)
  pq.write_table(table, 'example.parquet')


