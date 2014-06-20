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
    
    def test3(self):
        assert (t1.conv(20,1,0) == 10)# 20 euros should make 10 pounds
        
    def test4(self):
        assert(t1.conv(20,1,3)==40)#20eur should make JPY40
        
        
if __name__ =='__main__':
    unittest.main()