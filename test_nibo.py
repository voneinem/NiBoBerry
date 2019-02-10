import nibo
from nibo import LED
import unittest
from unittest.mock import MagicMock

class TestNiboFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        nibo.Send = MagicMock()

### LEDs ###
    def test_SetLED_On(self):
        nibo.GetLEDMask = MagicMock(return_value=1)        
        nibo.SetLED(LED.RedLeft, 1)
        nibo.Send.assert_called_with('request set 3, 3')

    def test_SetLED_Off(self):
        nibo.GetLEDMask = MagicMock(return_value=3)        
        nibo.SetLED(LED.RedLeft, 0)
        nibo.Send.assert_called_with('request set 3, 1')

    def test_SetLedUpper(self):
        nibo.SetGPIO = MagicMock()
        nibo.SetLED(LED.GreenUpper, 1)
        nibo.SetGPIO.assert_called_with(18,1)
        nibo.SetLED(LED.RedUpper, 1)
        nibo.SetGPIO.assert_called_with(22,1)

### Feelers ###
    def test_GetFeeler_1(self):
        nibo.Send = MagicMock(return_value='request set 4, 1')
        flo, fli, fro, fri = nibo.GetFeeler()
        self.assertTrue(flo)
        self.assertFalse(fli)
        self.assertFalse(fro)
        self.assertFalse(fri)

    def test_GetFeeler_34(self):
        nibo.Send = MagicMock(return_value='request set 4, 34')
        flo, fli, fro, fri = nibo.GetFeeler()
        self.assertFalse(flo)
        self.assertTrue(fli)
        self.assertFalse(fro)
        self.assertTrue(fri)

### Push Buttons ###
    def test_GetPushButton_NotPushed(self):
        nibo.GetGPIO = MagicMock(return_value=1)
        a, b = nibo.GetPushButton()     
        self.assertFalse(a)
        self.assertFalse(b)   

    def test_GetPushButton_Pushed(self):
        nibo.GetGPIO = MagicMock(return_value=0)
        a, b = nibo.GetPushButton()     
        self.assertTrue(a)
        self.assertTrue(b)   

### Motors ###
    def test_Motors(self):
        nibo.Send = MagicMock()
        nibo.SetMotorMode(3)
        nibo.Send.assert_called_with('request set 6, 3')
        nibo.SetMotors(42,-42)
        nibo.Send.assert_called_with('request set 7, 42 set 8, -42')


if __name__ == '__main__':
    unittest.main()