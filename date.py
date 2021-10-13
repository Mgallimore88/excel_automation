import datetime

# Think of a better class name - 
# datetime already contains a class called Date. 
class Date():
    # Class to handle the date extraction
    # and user input of date
    def __init__(self):
        self.first_date = None
        self.last_date = None
        self.date = datetime.date
        self.today = self.date.today()
        self.day = self.today.day
        self.month = self.today.month
        self.year = self.today.year
    
    def today(self):
        # Get today's date and print to terminal
        date = datetime.date
        today = date.today()
        date_str = today.strftime("%b-%d-%Y")
        return(date_str)


## Dates must be in a specific format for this function to work properly
## Make a test for this - return a meaningful error prompting for date in correct format
# ASSERT  
    def process_dates(self, input_dates):
        # Find min and max values in list of input dates
        self.first_date = input_dates.min()
        self.last_date = input_dates.max()
        
        self.first_day = int(self.first_date[:2])
        self.first_month = int(self.first_date[3:5])
        self.first_year = int(self.first_date[6:8])
        self.last_day = int(self.last_date[:2])
        self.last_month = int(self.last_date[3:5])
        self.last_year = int(self.last_date[6:8])
        
        # Turn into datetime object and create variables
        self.first_date = datetime.date(self.first_year, self.first_month, self.first_day)
        self.last_date = datetime.date(self.last_year, self.last_month, self.last_day)
        self.start_month = self.first_date.strftime("%b")
        self.start_day = self.first_date.strftime("%d")
        self.end_month = self.last_date.strftime("%b")
        self.end_day = self.last_date.strftime("%d")




    def user_dates(self):
        return None

    

