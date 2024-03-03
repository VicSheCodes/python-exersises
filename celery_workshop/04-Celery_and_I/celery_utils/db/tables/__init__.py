import glob
from os.path import basename
from os.path import dirname
from os.path import isfile
from os.path import join

modules = glob.glob(join(dirname(__file__), "*.py"))
# this allows us to `from db.tables import *` and get all the tables.
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]

