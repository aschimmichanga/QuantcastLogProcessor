import unittest
from LogCookieProcessor import LogCookieProcessor
from datetime import datetime
  
class LogProcessorTest(unittest.TestCase):
    def __convert_to_datetime_date(self, date_string):
        datetime.fromisoformat(date_string).date()
  
  # test constructor with diff dates
    def test_reg_num_as_date(self):
        with self.assertRaises(ValueError):
            LogCookieProcessor("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n", 
                               1)
    
    def test_valid_date(self):
        date = "2018-12-08"
        log_cookie_processor = LogCookieProcessor("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n", 
                               date)
        self.assertEqual(self.__convert_to_datetime_date(date), log_cookie_processor.target_date)
        
    def test_valid_time(self):
        time = "2018-12-07T23:30:00+00:00"
        log_cookie_processor = LogCookieProcessor("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n", 
                               time)
        self.assertEqual(self.__convert_to_datetime_date(time), log_cookie_processor.target_date)
        
    # test constructor with diff logs
    def test_none_as_log(self):
        with self.assertRaises(ValueError):
            LogCookieProcessor(None,
                               "2018-12-08")
            
    def test_invalid_format_log(self):
        with self.assertRaises(ValueError):
            LogCookieProcessor("hi bye",
                               "2018-12-08")
            
    def test_valid_log(self):
        log = "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n"
        date = "2018-12-08"
        log_cookie_processor = LogCookieProcessor(log, date)
        print(log_cookie_processor.cookie_dict)
        #self.assertEqual(log, log_cookie_processor.log)
    
  
  
if __name__ == '__main__':
    unittest.main()