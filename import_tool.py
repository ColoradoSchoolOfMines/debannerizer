# A tool to help you import data from banner
import sys
from debannerizer import importer

if len(sys.argv) == 2:
    importer.import_term(sys.argv[1])
else:
    print("A tool to help you import data from banner")
    print("Usage: python3 import_tool.py BANNER_TERM")
    print("... where BANNER_TERM is what is put into")
    print("    the request to banner, eg '201710'.")
