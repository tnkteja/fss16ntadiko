import unittest, ntadiko

class Test_birthdayparadox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trials = 10000
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)

    def test_birthdayparadox23(self):
        self.assertGreaterEqual(ntadiko.birthdayParadox(Test_birthdayparadox.trials, 23), 0.5)

    def test_birthdayparadox70(self):
        self.assertGreaterEqual(ntadiko.birthdayParadox(Test_birthdayparadox.trials, 70), 0.999)

    def test_birthdayparadox70E(self):
        self.assertLessEqual(ntadiko.birthdayParadox(Test_birthdayparadox.trials, 70 ), 0.9)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

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