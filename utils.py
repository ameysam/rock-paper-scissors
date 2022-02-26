from datetime import datetime

def time_logger(func):
    def wrapped(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"{duration.seconds} seconds")
        return result
    
    return wrapped
