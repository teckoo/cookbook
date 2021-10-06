"""
Python standard library function usage on text processing
"""
import unittest


class IOTest(unittest.TestCase):
    """ text process show cases """
    def test_append_files(self):
        """ append multiple files into one big file
        use shutil to handle huge files
        python -m unittest text_processing.IOTest.test_append_files
        """
        import shutil
        input_files = ('/tmp/f1.dat', '/tmp/f2.dat', '/tmp/f3.dat')
        out_file_path = '/tmp/f_out.dat'
        for fn in input_files:
            with open(fn, 'r') as fi, open(out_file_path, 'a') as fo:
                shutil.copyfileobj(fi, fo)

    def test_gen_fixed_width_column(self):
        """
        parse only required columns
        cfg = {
            "columns": {"2-4":"pan", "5-8":"pan"},
            "record_length": 10
        }
        :return:
        ((0, 2), (2, 4), (4, 5), (5, 8), (8, 10))
        """
        cfg = {
            "columns": {"2-4": "pan", "5-8": "pan"},
            "record_length": 10
        }
        expected = [(0, 2), (2, 4), (4, 5), (5, 8), (8, 10)]
        pairs = [(int(pos.split('-', 1)[0]), int(pos.split('-', 1)[1])) for pos in cfg.get("columns", {}).keys()]
        pairs.sort()  # [(2, 4), (5, 8)]

        result = []
        start, end = 0, 0
        for s, e in pairs:
            if start < s:
                end = s
                result.append((start, end))
            result.append((s, e))
            start, end = e, e
        rec_end = cfg.get("record_length", 0)
        if end < rec_end:
            result.append((start, rec_end))
        print('result = {}'.format(result))
        self.assertEqual(result, expected)

    def test_json_handling(self):
        """
        Standard JSON encode/decode usage
        Another useful package is 'simplejson' which is much less strict on syntax
        """
        import json
        # encode: give a dict or list, convert to JSON string
        sample_list = ['foo', {'bar': ('baz', None, 1.0, 2)}]
        print(json.dumps(sample_list))
        # expect: '["foo", {"bar": ["baz", null, 1.0, 2]}]'

        print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True, indent=4))
        # expect:
        # {
        # "a": 0,
        # "b": 0,
        # "c": 0
        # }

        # write to a file
        with open('sample_json.dump', 'w') as outfile:
            json.dump(sample_list, outfile)

        # decode:
        sample_dict = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
        # expect: ['foo', {'bar': ['baz', None, 1.0, 2]}]
        assert sample_dict[0] == 'foo'

        # read from file
        with open('sample_json.txt') as infile:
            print(json.load(infile))

    def test_string_format(self):
        """
        Correct way to format string in Python 2 and 3.
        https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator

        Which way to use?
        User supplied format strings? Yes, #4 template string

        Python 3.6+? #3 f-string
        < Python 3.6 #2 str.format

        #1 Old C style
        %s - String (or any object with a string representation, like numbers)
        %d - Integers
        %f - Floating point numbers
        %.<number of digits>f - Floating point numbers with a fixed amount of digits
            to the right of the dot.
        %x/%X - Integers in hex representation (lowercase/uppercase)

        #2 New style: str.format
        'Hello, {}'.format(name)
        'Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno)

        #3 String Interpolation / f-Strings (Python 3.6+)

        #4 Template Strings (Standard Library)
        """

        # 1 Old style
        group = "MyGroup"
        size = 30
        # C style
        print("c style - Group: '%s', number of users: %d" % (group, size))
        # using dict, better in reading
        print("old style - Group: '%(g)s', number of users: %(n)d" % {'g': group, 'n': size})

        # 2 New style
        print("new style - Group: {group}, number of users: {size}".format(group=group, size=size))

        # 3 String Interpolation / f-Strings (Python 3.6+)
        f_str = """
            >>> f"f-strings - Group: {group}, size: {size:#d}"
            # this is similar below, but more readable
            "f-strings - Group:" + group + ", size: " + size

            >>> a = 5
            >>> b = 10
            >>> f'Five plus ten is {a + b} and not {2 * (a + b)}.'
            'Five plus ten is 15 and not 30.'
        """
        assert f_str is not None

        # 4 Template Strings (Standard Library)
        from string import Template
        templ_string = 'Template style - Group: $group, size: $n'
        print(Template(templ_string).substitute(group=group, n=int(size)))


if __name__ == "__main__":
    unittest.main()
