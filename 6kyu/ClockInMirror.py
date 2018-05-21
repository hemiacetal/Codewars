def what_is_the_time(time_in_mirror):
    hr = int(time_in_mirror[:2])
    min = int(time_in_mirror[3:])
    
    if (min != 0):
        if (hr == 12):
            hr = 11
        elif (hr == 11):
            hr = 12
        else:
            hr = 11 - hr
            
        min = 60 - min
    else:
        if (hr != 12 and hr != 6):
            hr = 12 - hr
    
    return "{:02}:{:02}".format(hr, min)