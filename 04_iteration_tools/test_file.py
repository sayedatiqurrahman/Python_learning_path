import datetime

def test_datetime():
    # Create a datetime object for January 1, 2020
    dt = datetime.datetime(2020, 1, 1)
    
    # Check if the year is 2020
    assert dt.year == 2020
    
    # Check if the month is January
    assert dt.month == 1
    
    # Check if the day is the first
    assert dt.day == 1
    
    # Check if the date is correct
    assert dt.date() == datetime.date(2020, 1, 1)
    
    # Check if the time is midnight
    assert dt.time() == datetime.time(0, 0)


test_datetime()
print("All tests passed successfully!")