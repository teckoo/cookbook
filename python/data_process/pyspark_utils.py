"""
Snippets to manipulate files
"""
import unittest
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession


class DataFrameTest(unittest.TestCase):
    """DataFrame related operations """

    @unittest.skip("for now")
    def test_read_csv(self):
        """ read CSV, and return a DataFrame
        The data files can contain header and comments
        python -m unittest pyspark_utils
        """
        conf = SparkConf().setMaster("local").setAppName("DataConversion")
        sc = SparkContext(conf=conf)
        df = SQLContext(sc).read.csv("/tmp/sample-no-header.csv", header=None)
        self.assertIsNotNone(df)
        df = SQLContext(sc).read.csv("/tmp/sample-with-header.csv", header=True, sep=',',
                                     comment='#')
        self.assertIsNotNone(df)
        # brutal force to skip first 4 rows
        df.rdd.zipWithIndex().filter(lambda tup: tup[1] > 4).map(lambda x: x[0])

    def test_header_footer(self):
        # df is DataFrame instance
        spark = SparkSession.builder.appName("ReadFixedWidth").getOrCreate()
        # df = spark.read.csv("/tmp/fixed-with-header.dat", header=True, sep='|')
        df = spark.read.format("text").load("fixture/fixed-with-header.dat")
        header_line = 2
        footer_line = 2
        end_index = df.count() - footer_line
        result = df.rdd.zipWithIndex().filter(
            lambda row: header_line <= row[1] < end_index) \
            .map(lambda x: x[0])
        t = result.map(lambda x: x.value.split('|'))
        # Above can be shortened as
        # result = df.rdd.zipWithIndex().filter(
        #             lambda row: row[1] >= header_line and row[1] < end_index) \
        #             .map(lambda x: x[0].value.split('|'))
        t.first()
        # [u'1', u'data', u'line']
        t.toDF(cols.split('|'))
        # DataFrame[a: string, b: string, c: string]
        t.toDF(cols.split('|')).show()

        df.show()
        self.assertEqual(df.count(), 5)
        print(result.first(), result.count())
        result.toDF().show()
        self.assertEqual(result.count(), 3)

    @unittest.skip("for now")
    def test_pandas_dataframe_to_spark(self):
        """
        https://bryancutler.github.io/createDataFrame/
        """
        pass

    def test_convert_list_to_dataframe(self):
        """ sample code to convert regular list to dataframe,
        assume everything is a string"""
        mylist = [['a', 'b', 'c'], ['1', '2', '3']]
        spark = SparkSession.builder.appName("ReadFixedWidth").getOrCreate()
        spark.createDataFrame(mylist, ('name', 'group', 'dept')).show()
        # +----+-----+----+
        # |name|group|dept|
        # +----+-----+----+
        # |   a|    b|   c|
        # |   1|    2|   3|
        # +----+-----+----+


if __name__ == "__main__":
    unittest.main()
