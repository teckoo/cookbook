"""
Snippets for os path related usage
"""
import os.path


def print_path():
    """ print out current dir name, function and class method work the same way
    This is useful when reading resource such as config files in other folders.
    """
    print("os.curdir=[%s]" % os.curdir)
    print("__file__=[%s]" % __file__)
    print("basename=[%s]" % os.path.basename(__file__))
    print("dirname=[%s]" % os.path.dirname(os.path.abspath(__file__)))
    print("real_path=[%s]" % os.path.realpath(__file__))

    folder = os.path.dirname(os.path.abspath(__file__))
    res_file = os.path.join(folder, '../resources/credentials.txt')
    if os.path.isfile(res_file):
        print("found resource: %s" % res_file)
    else:
        print("not found resource: %s" % res_file)


if __name__ == "__main__":
    print_path()

