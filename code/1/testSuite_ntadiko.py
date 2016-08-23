import unittest,testBirthdayParadox,testShanonsEntropy

testSuite_ntadiko = unittest.TestSuite()
testSuite_ntadiko.addTest(unittest.makeSuite(testBirthdayParadox.Test_birthdayparadox))
testSuite_ntadiko.addTest(unittest.makeSuite(testShanonsEntropy.Test_shanonsentropy))

testSuiteRunner = unittest.TextTestRunner()
testSuiteRunner.run(testSuite_ntadiko)