"""
Snippets to manipulate files
"""
import unittest
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext


class DataFrameTest(unittest.TestCase):
    """DataFrame related operations """

    def test_read_csv(self):
        """ read CSV, and return a DataFrame
        The data files can contain header and comments
        python -m unittest pyspark_utils
        """
        conf = SparkConf().setMaster("local").setAppName("DataConversion")
        sc = SparkContext(conf=conf)
        df = SQLContext(sc).read.csv("/tmp/sample-no-header.csv", header=None)
        self.assertIsNotNone(df)
        df = SQLContext(sc).read.csv("/tmp/sample-with-header.csv", header=True, sep=',', comment='#')
        self.assertIsNotNone(df)
        # brutal force to skip first 4 rows
        df.rdd.zipWithIndex().filter(lambda tup: tup[1] > 4).map(lambda x: x[0])

    def test_panda_dataframe_to_spark(self):
        '''
        https://bryancutler.github.io/createDataFrame/
        '''
        pass


if __file__ == "__main__":
    unittest.main()

