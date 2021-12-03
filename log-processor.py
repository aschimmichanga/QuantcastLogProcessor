from datetime import datetime
import os
                
class LogCookieProcessor:    
    def update_cookie_dictionary(self, cookie_id, time):
        try:
            date = datetime.fromisoformat(time).date()
            if date == self.target_date:
                if cookie_id in self.cookie_dict:
                    self.cookie_dict[cookie_id] += 1
                else:
                    self.cookie_dict[cookie_id] = 1
        except Exception:
            raise ValueError("Cookie's time format is invalid," /
                             "should be in iso format YYYY-MM-DD[T-HH:MM+TZ]" /
                             " (TZ is time zone)")

    def read_cookies_from_log_file(self):
        LOG_FILE_NAME = "cookie_log.csv"
        if os.exists(LOG_FILE_NAME):
            with open(LOG_FILE_NAME, "r") as log_file:
                for line in log_file.readlines():
                    self.update_cookie_dictionary(*line.split(","))
        else:
            raise ValueError("The log file, named as", 
                            LOG_FILE_NAME, 
                            "must exist to proceed with the program.")
            
    # most active cookie meaning the cookie that appears most often in the
    # log at the specified target date
    def find_most_active_cookies(self):
        active_cookies = []
        max_occurrence = 0
        for cookie_id, num_occurrence in self.cookie_dict.items():
            if num_occurrence > max_occurrence:
                max_occurrence = num_occurrence
                active_cookies = [cookie_id]
            elif num_occurrence == max_occurrence:
                active_cookies += [cookie_id]
        return active_cookies
    
    def __init__(self, target_date):
        try:
            self.target_date = datetime.fromisoformat(target_date).date()
        except Exception:
            raise ValueError("Target date's format is invalid," /
                             "should be in iso format YYYY-MM-DD[T-HH:MM+TZ]" /
                             " (TZ is time zone)")
            
        self.cookie_dict = {}
        self.read_cookies_from_log_file()
            
            
def main():
    log_cookie_processor = LogCookieProcessor()
    active_cookies = log_cookie_processor.find_most_active_cookies()
    print(*active_cookies, sep="\n")