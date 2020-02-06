from datetime import datetime

PATH = '/var/log/mysite.log'

def logit(info):

    ''' where info == string to be logged '''

    # Get time and date
    now = datetime.now()
    # Format the date and time
    time_string = now.strftime("%b %d %Y %H:%M:%S")
    # Combine date/time with info to be logged
    log_entry = '%s %s\n' % (time_string, info)

    # open log file
    lf = open(PATH, 'a') # lf == log file
    lf.write(log_entry) # write log entry
    lf.close() # close log file

