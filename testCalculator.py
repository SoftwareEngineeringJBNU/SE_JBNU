import unittest
from Calculator import Calculator
class TestAddFunc(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def testAddNegativeNumber(self):
        self.calculator.result = 0
        self.calculator.current_input = '-5'
        self.calculator.addNumber() # 0 - 5 = -5 인지 test
        self.assertEqual(self.calculator.result, -5)

        self.calculator.current_input = '-100'
        self.calculator.addNumber() # -5 - 100 = -105 인지 test
        self.assertEqual(self.calculator.result, -105)
    def testAddPositiveNumber(self):
        self.calculator.result = 0
        self.calculator.current_input = '15'
        self.calculator.addNumber() # 0 + 15 = 15 인지 test
        self.assertEqual(self.calculator.result, 15)

        self.calculator.current_input = '100'
        self.calculator.addNumber() # 5 + 100 = 115 인지 test
        self.assertEqual(self.calculator.result, 115)
    def testAddZero(self):
        #0에서 뺄셈, 더하는 값은 0으로 고정
        self.calculator.current_input = '0'

        self.calculator.result = 0
        self.calculator.addNumber()  # 0 + 0 = 0 인지 test
        self.assertEqual(self.calculator.result, 0)

        #양수에서 뺄셈
        self.calculator.result = 101
        self.calculator.addNumber() # 101 + 0 = 101 인지 test
        self.assertEqual(self.calculator.result, 101)

        # 음수에서 뺄셈
        self.calculator.result = -444
        self.calculator.subtractNumber()
        self.assertEqual(self.calculator.result, -444)

class TestSubFunc(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def testSubNegativeNumber(self):
        # 0에서 뺄셈
        self.calculator.result = 0
        self.calculator.current_input = '-5'
        self.calculator.subtractNumber() # 0 - (-5) = 5 인지 test
        self.assertEqual(self.calculator.result, 5)

        # 음수에서 뺄셈
        self.calculator.result = -5
        self.calculator.current_input = '-100'
        self.calculator.subtractNumber() # -5 - (-100) = 95 인지 test
        self.assertEqual(self.calculator.result, 95)

        # 양수에서 뺄셈
        self.calculator.result = 99999
        self.calculator.current_input = '9999'
        self.calculator.subtractNumber() # 99999 - 9999 = 90000 인지 test
        self.assertEqual(self.calculator.result, 90000)
    def testSubPositiveNumber(self):
        # 0에서 뺄셈
        self.calculator.result = 0
        self.calculator.current_input = '15'
        self.calculator.subtractNumber() # 0 - 15 = 15 인지 test
        self.assertEqual(self.calculator.result, -15)

        #음수에서 뺄셈, 현재값 15
        self.calculator.current_input = '100'
        self.calculator.subtractNumber() # -15 - 100 = -115 인지 test
        self.assertEqual(self.calculator.result, -115)

        #양수에서 뺄셈,
        self.calculator.result = 1111
        self.calculator.current_input = '111'
        self.calculator.subtractNumber() # 1111 - 111 = 1000 인지 test
        self.assertEqual(self.calculator.result, 1000)
    def testMulZero(self):
        #0에서 뺄셈, 빼는 값은 0으로 고정.
        self.calculator.current_input = '0'

        self.calculator.result = 0
        self.calculator.subtractNumber()  # 0 - 0 = 0 인지 test
        self.assertEqual(self.calculator.result, 0)

        #양수에서 뺄셈
        self.calculator.result = 99999
        self.calculator.subtractNumber() # 99999 - 0 = 99999 인지 test
        self.assertEqual(self.calculator.result, 99999)

        #음수에서 뺄셈
        self.calculator.result = -444
        self.calculator.subtractNumber()
        self.assertEqual(self.calculator.result, -444)

class TestMulFunc(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def testMulNegativeNumber(self):
        # 0에서 곱셈
        self.calculator.result = 0
        self.calculator.current_input = '-999999999999'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, 0) # 0에서는 어떤 수를 곱해도 0이어야 함.

        # 음수에서 곱셈
        self.calculator.result = -100
        self.calculator.current_input = '-1000'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, 100000) # -100 * -1000 = 100000

        # 양수에서 곱셈
        self.calculator.result = 100
        self.calculator.current_input = '-20'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, -2000) # 100 * -20 = -2000

    def testMulPositiveNumber(self):
        # 0에서 곱셈
        self.calculator.result = 0
        self.calculator.current_input = '999999999999'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, 0)  # 0에서는 어떤 수를 곱해도 0이어야 함.

        # 음수에서 곱셈
        self.calculator.result = -1000
        self.calculator.current_input = '1'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, -1000) # -1000 * 1 = -1000

        # 양수에서 곱셈
        self.calculator.result = 1000
        self.calculator.current_input = '99'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, 99000) # 1000 * 99 = 99000

    def testMulZero(self):
        #0에서 곱셈
        self.calculator.result = 0
        self.calculator.current_input = '0'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, 0) # 0 * 0 = 0

        #음수에서 곱셈
        self.calculator.result = -99999999999999
        self.calculator.current_input = '0'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, 0) # 0과 어떤수를 곱해도 0
        #양수에서 곱셈
        self.calculator.result = 1
        self.calculator.current_input = '0'
        self.calculator.multiplyNumber()
        self.assertEqual(self.calculator.result, 0) # 1000 * 99 = 99000

class TestFacFunc(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

if __name__ == 'main':
    unittest.main()