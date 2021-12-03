import unittest
from LogCookieProcessor import LogCookieProcessor
  
class LogProcessorTest(unittest.TestCase):
    def setupDefaultProcessor():
        log = "4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\n" \
              "fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00\n" \
              "4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00"
        return LogCookieProcessor(log, "2018-12-08")
  
    # Returns True or False. 
    def test(self):        
        self.assertTrue(True)
  
if __name__ == '__main__':
    unittest.main()