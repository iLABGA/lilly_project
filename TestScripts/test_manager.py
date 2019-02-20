import unittest

from TestScripts.RegressionTests.mainpage_tests import MainTest
# Get all tests from classes
maintest= unittest.TestLoader().loadTestsFromTestCase(MainTest)

# Create a test suite combining all test cases
regressionSuite = unittest.TestSuite()
regressionSuite.addTest(maintest)

smokeSuite = unittest.TestSuite()
smokeSuite.addTest(maintest)

# Test runner
unittest.TextTestRunner(verbosity=2).run(smokeSuite)
