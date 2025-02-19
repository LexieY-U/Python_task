# Make imports work in tests like they do in application
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../app")
