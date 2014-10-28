def decTime(time):
    '''
    time is entered in the format "hh:mma" or "hh:mmp" and returned in a 
    decimal form from 00.00 up to 23.99
    '''
    
    hour=float(time.split(':')[0])
    minute=float(time.split(':')[1][:2])
    ampm=str(time.split(':')[1][2])

    if ampm=='p':
        hour+=12.0

    minute=minute/60.0
    
    return hour+minute

        
