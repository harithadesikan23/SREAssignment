import unittest
import pandas as pd
from unittest.mock import patch
from SRETool import *


class TestSRETool(unittest.TestCase):
    df = pd.read_csv('TestInput.csv')
    
    def test_compare_images(self):
        obj = SRETool()
        output_df = obj.compare_images(TestSRETool.df)
        self.assertEqual(len(TestSRETool.df), len(output_df)) 
        columns = ["image1", "image2", "Similar", "Elapsed"]
        self.assertListEqual(list(output_df.columns), columns)

if __name__ == '__main__':
    unittest.main()