def TimetoDec(time):
    '''
    time is entered in the format "hh:mma" or "hh:mmp" and returned in a 
    decimal form from 00.00 up to 23.99
    '''
    
    hour = float(time.split(':')[0])
    minute = float(time.split(':')[1][:2])
    ampm = str(time.split(':')[1][2])

    if ampm == 'p':
        hour += 12.0

    minute = minute/60.0
       
    return hour+minute


def DectoTime(dec):
    '''
    time is entered in the decimal form (see TimetoDec) and
    returned in the hh:mma or hh:mmp form
    '''
    dec = str(dec)
    time = dec.split('.')
    minute = int(int(time[1])*.6)
    if int(time[0])>12:
        hour = int(time[0])-12
        ampm = 'p'
    else:
        hour = int(time[0])
        ampm = 'a'
    return str(hour)+':'+str(minute)+ampm


'''
def Day(day, shiftNum):
    shiftDict={}
    x=0
    while shiftNum<x:
        
'''
