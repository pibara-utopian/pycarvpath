#!/usr/bin/env python3
from carvpath import CarvPath,SparseFragment,BaseFragment
import unittest

class carvpathTest(unittest.TestCase):
    # Positive test 1
    def testsparse1(self):
        cp1 = CarvPath([SparseFragment(1000)])
        cp2 = CarvPath([SparseFragment(234)])
        cp3 = cp1 + cp2
        self.assertTrue(str(cp3) == "S1234")
    def testsparse2(self):
        cp1 = CarvPath("S4000/1000+2000")
        self.assertTrue(str(cp1) == "S2000")
    def testsparse3(self):
        cp1 = CarvPath("S4/S3000")
        self.assertTrue(str(cp1) == "S3000")
    def testsparse4(self):
        self.assertRaises(RuntimeError, CarvPath, "S400/300+300")
    def testfrag(self):
        cp1 = CarvPath([BaseFragment(1000,123),BaseFragment(2000,456)])
        cp2 = cp1[BaseFragment(100,100)]
        self.assertTrue(str(cp2) == "1100+23_2000+77")

if __name__ == "__main__":
    unittest.main()


