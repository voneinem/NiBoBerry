import nibo
import unittest
from unittest.mock import MagicMock

class TestNiboFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        nibo.Send = MagicMock()

    def test_SetLED_On(self):
        nibo.GetLEDMask = MagicMock(return_value=1)        
        nibo.SetLED(nibo.LED.RedLeft, 1)
        nibo.Send.assert_called_with('request set 3, 3')

    def test_SetLED_Off(self):
        nibo.GetLEDMask = MagicMock(return_value=3)        
        nibo.SetLED(nibo.LED.RedLeft, 0)
        nibo.Send.assert_called_with('request set 3, 1')

if __name__ == '__main__':
    unittest.main()