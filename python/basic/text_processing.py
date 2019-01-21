"""
Python standard library function usage on text processing
"""


def json_handling():
    """
    Starndard JSON encode/decode usage
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


def string_format():
    """
    Correct way to format string in Python 2 and 3.
    https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator

    Which way to use?
    User supplied format strings? #4 template string

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
    string_format()

