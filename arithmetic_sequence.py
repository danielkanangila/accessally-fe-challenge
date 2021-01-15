# count the numeber of arithmetic sequence in a range of two given ahours
import datetime as dt
import numpy as np
# Initialize the start time
start_time = dt.datetime.strptime('12:00', '%H:%M').time()

# Get clock observation time input (in minute)
observed_min = int(input('Enter the observation time (in minutes):'))

# define a the function named as_counter (for arithmetic sequence counter) that will 
# receive as parameters the the start_date and the minutes if observation
def as_counter(start_time, observed_min):
    # create an arithmetic sequence found counter
    arithmetic_sequence = 0
    # Loop through the range of 1 to n=input_minutes+1
    for minute in range(1,(observed_min+1)):
        # create a temporary datetime to compute the current_time
        tmp_datetitme = dt.datetime.combine(dt.date.today(), start_time) 
        # compute the current time and format it to the format -I:M for 12 hours time format
        current_time = (tmp_datetitme + dt.timedelta(minutes=minute)).strftime('%-I:%M')
        # convert the current time to a sequence of numbers
        num_sequence = [int(char) for char in list(current_time) if char != ":"]
        # use numpy to check the number sequence is an arithmethic sequence
        if np.all(np.diff(num_sequence, 2) == 0):
            arithmetic_sequence += 1
        
    # return the counter
    return arithmetic_sequence
    
sequence_count =  as_counter(start_time, observed_min)
print(sequence_count)
