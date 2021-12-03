import unittest
from LogCookieProcessor import LogCookieProcessor
from datetime import datetime
  
class LogProcessorTest(unittest.TestCase):
    def __convert_to_datetime_date(self, date_string):
        return datetime.fromisoformat(date_string).date()
  
  # test constructor with diff dates
    def test_reg_num_as_date(self):
        with self.assertRaises(ValueError):
            LogCookieProcessor("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n", 
                               1)
    
    def test_valid_date(self):
        date = "2018-12-08"
        log_cookie_processor = LogCookieProcessor("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n", 
                               date)
        self.assertEqual(self.__convert_to_datetime_date(date), log_cookie_processor.TARGET_DATE)
        
    def test_valid_time(self):
        time = "2018-12-07T23:30:00+00:00"
        log_cookie_processor = LogCookieProcessor("4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n", 
                               time)
        self.assertEqual(self.__convert_to_datetime_date(time), log_cookie_processor.TARGET_DATE)
        
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
        self.assertEqual({"4sMM2LxV07bPJzwf":1}, log_cookie_processor.cookie_dict)
    
    def test_cookie_dict_with_empty_log(self):
        date = "2018-12-08"
        log_cookie_processor = LogCookieProcessor("", date)
        self.assertEqual({}, log_cookie_processor.cookie_dict)
        
    def setup_default_log_cookie_processor(self, date):
        log = ("SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00\n" +
               "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n" +
               "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00\n" +
               "fbcn5UAVanZf6UtG,2018-12-07T23:30:00+00:00\n" +
               "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00\n" +
               "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00")
        return LogCookieProcessor(log, date)
        
    def test_most_available_cookie_with_unavailable_date(self):
        log_cookie_processor = self.setup_default_log_cookie_processor("2021-12-03")
        self.assertEqual([], log_cookie_processor.find_most_active_cookies())
    
    def test_most_available_cookie_with_one_most(self):
        log_cookie_processor = self.setup_default_log_cookie_processor("2018-12-07")
        self.assertEqual(["4sMM2LxV07bPJzwf"], log_cookie_processor.find_most_active_cookies())

    def test_most_available_cookie_with_multi_most(self):
        log_cookie_processor = self.setup_default_log_cookie_processor("2018-12-08")
        most_avail_cookies = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        self.assertEqual(most_avail_cookies, log_cookie_processor.find_most_active_cookies())

  
if __name__ == '__main__':
    unittest.main()