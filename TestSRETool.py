import unittest
import pandas as pd
from unittest.mock import patch
from SRETool import *


class TestSRETool(unittest.TestCase):
    df = pd.read_csv('TestInput.csv')
    
    def test_compute_similarity_score(self):
        obj = SRETool()
        output_df = obj.compute_similarity_score(TestSRETool.df)
        self.assertEqual(len(TestSRETool.df), len(output_df)) 
        columns = ["image1", "image2", "Similar", "Elapsed"]
        self.assertListEqual(list(output_df.columns), columns)

if __name__ == '__main__':
    unittest.main()