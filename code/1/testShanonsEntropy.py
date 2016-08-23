import unittest, ntadiko

class Test_shanonsentropy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)

    def test_entrophyfor4(self):
        arr=[0.25,0.25,0.25,0.25]
        ans=ntadiko.ShanonsEntropy(arr)
        self.assertEqual(ans, 2)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()