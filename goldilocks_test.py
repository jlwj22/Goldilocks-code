import unittest
from unittest.mock import patch  
from app_logic import fetch_current_temperature 

class TestCurrentTemperature(unittest.TestCase):

    @patch('app_logic.serial_comm')  
    def test_normal_temperature(self, mock_serial):
        mock_serial.read_serial_data.return_value = "TEMP:22°C" 
        result = fetch_current_temperature()
        self.assertEqual(result, 71.6)

    @patch('app_logic.serial_comm')
    def test_freezing_temperature(self, mock_serial):
        mock_serial.read_serial_data.return_value = "TEMP:0°C"
        result = fetch_current_temperature()
        self.assertEqual(result, 32) 

    @patch('app_logic.serial_comm')
    def test_high_temperature(self, mock_serial):
        mock_serial.read_serial_data.return_value = "TEMP:40°C"
        result = fetch_current_temperature()
        self.assertEqual(result, 104)

    @patch('app_logic.serial_comm')
    def test_invalid_format(self, mock_serial):
        mock_serial.read_serial_data.return_value = "TEMP: Invalid"
        result = fetch_current_temperature()
        self.assertEqual(result, None) 

    @patch('app_logic.serial_comm')
    def test_no_data(self, mock_serial):
        mock_serial.read_serial_data.return_value = None
        result = fetch_current_temperature()
        self.assertEqual(result, None) 

if __name__ == '__main__':
    unittest.main()
