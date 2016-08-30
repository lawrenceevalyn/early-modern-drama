# import libraries
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os.path
import collections
import csv
import operator

# easy way: how many people speak more than 12% of the lines?

# hard way: each play will have its own power-law-ish distribution;
# find the average curve, then compare each play's curve to that