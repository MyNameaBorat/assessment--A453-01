import task1 as t1
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        t1.rates = [1,2,3,4]
    

    def test1(self):
        assert t1.rates[0] == 1# test 1 fails rate for GBP not 1
        
    def test2(self):
        assert (t1.rates[1]==2)#rate for euros should be 2
        assert (t1.conv(10,0,1)== 20)# 10 GBP(curr0) should make 20 eur(currency1)
        
if __name__ =='__main__':
    unittest.main()