"""
Snippets to manipulate files
"""
import unittest
# import pandas as pd
# import pyarrow as pa
# import pyarrow.parquet as pq


class DataFrameTest(unittest.TestCase):
    """DataFrame related operations """
    def test_read_csv(self):
        """ read CSV, and return a DataFrame"""
        df = pd.read_csv('sample-no-header.csv')
        self.assertEquals(type(df), pd.DataFrame)


class CsvTest(unittest.TestCase):
    """ code snippets for handling CSV files """
    def test_load_file(self):
        line = '"a", "b", "1, 2, 3", "d"'
        expect = ['a', 'b', '1, 2, 3', 'd']

        import csv
        reader = csv.reader(open("/tmp/sample.csv"), delimiter=',', quotechar='"')
        result = []
        for row in reader:
            result.append(row)
        self.assertEqual(expect, result[0])

        from io import StringIO
        f = StringIO(line)
        reader = csv.reader(f, delimiter=',', quotechar='"')
        result = []
        for row in reader:
            result.append(row)
        self.assertEqual(expect, result[0])

        # simpler version with split() on newlines:
        reader = csv.reader(line.split('\n'), delimiter=',', quotechar='"')
        result = []
        for row in reader:
            print('\t'.join(row))

        # simpler version with split() on newlines:
        reader = csv.reader(line.split('\n'), delimiter=',', quotechar='"')
        result = []
        for row in reader:
            result.append(row)
        self.assertEqual(expect, result[0])


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


if __name__ == "__main__":
    unittest.main()
