import os
import sys
import unittest
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
print(PROJECT_PATH)
print(SOURCE_PATH)
sys.path.append(SOURCE_PATH)