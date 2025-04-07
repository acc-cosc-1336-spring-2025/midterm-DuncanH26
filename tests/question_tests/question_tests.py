#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_a import use_global 
from src.question_b import get_assessment_value
from src.question_b import get_tax_assessed
from src.question_b import use_local_variable 
from src.question_d import get_miles_per_hour

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_global_variable(self):
        GLOBAL_INT = 1000
        global use_global
        self.assertEqual(100, use_global)

    def test_get_assessment_value(self):
        self.assertEqual(6000, get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))

    def test_get_tax_assessed(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
        self.assertEqual(72, get_tax_assessed(10000))

    def test_use_local_variable(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(True, use_local_variable(100))

    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32, 60))


