from datetime import datetime

# processing cookie from log -----------------------------------------             
class LogCookieProcessor:    
    # private helper to update cookie dictionary with a single cookie log entry
    def __update_cookie_dictionary(self, cookie_id, time):
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

    # private helper to update cookie dictionary with all cookie log entries
    def __fill_cookie_dictionary(self, log):
        for cookie in log.split("\n"):
            if cookie:
                if not "," in cookie:
                    raise ValueError("incorrectly formatted log")
                cookie_id, time = cookie.split(",")
                self.__update_cookie_dictionary(cookie_id, time)
            
    # returns the most active cookies 
    # meaning the cookies that appears most often in the log at the specified target date
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
    
    def __init__(self, log, target_date):
        # date validity already checked while cmd arg parsing
        if log is None:
            raise ValueError("invalid log given")
        try:
            self.target_date = datetime.fromisoformat(target_date).date()
            self.cookie_dict = {}
            self.__fill_cookie_dictionary(log)
        except Exception:
            raise ValueError("Target date's format is invalid,",
                             "should be in iso format YYYY-MM-DD[T-HH:MM+TZ]",
                             " (TZ is time zone)")