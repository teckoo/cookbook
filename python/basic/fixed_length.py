"""
Run doctest as:
python -m doctest gen_fixed_length.py

Run unittest as:
python -m unittest fixed_length.py

Data processing
* fixed length meta data generation
"""
import unittest


def gen_field_meta(col_len_def):
    """
    >>> col_len_def = (1, 2, 3, 4)
    >>> gen_field_meta(col_len_def)
    [(0, 1), (1, 3), (3, 6), (6, 10)]

    # Here is a verbal implementation:
    col_def = []
    start = 0
    for col_len in col_len_def:
        end = start + col_len
        col_def.append((start, end))
        start = end
    """
    return [(sum(col_len_def[:i]), sum(col_len_def[0:i+1])) for i, _ in enumerate(col_len_def)]


def parse_fixed_len(row_list, field_names, field_lens):
    """
    @:param row_list: data set
    @:field_names
    @:field_lens
    """
    if row_list is None:
        return []

    result = []
    f_lens = gen_field_meta(field_lens)
    for row in row_list:
        result.append([(f, row[l[0]:l[1]]) for f, l in zip(field_names, f_lens)])
    return result


class RecordTest(unittest.TestCase):
    """ Test reading fixed-length records """

    def test_parse_row(self):
        """ parse a record based on field length meta data """
        name_def = ("col_1", "col_2", "col_3", "col_4")
        col_def = (1, 2, 3, 4)
        data = ("1223334444", )
        field_list = parse_fixed_len(data, name_def, col_def)
        self.assertEqual(field_list[0], [("col_1", "1"),
            ("col_2", "22"), ("col_3", "333"), ("col_4", "4444")])


if __name__ == '__main__':
    unittest.main()

