def CheckTime(time):
    '''
    checks that time is entered in the format "hh:mma" or "hh:mmp"
    '''
    while True:
        try:
            float(time.split(':')[0])
            if len(((time.split(':')[0])))==2:
                try:
                    float((time.split(':')[1][:2]))
                    if len(((time.split(':')[1][:2])))==2:
                        if str((time.split(':')[1][2]))=='a' or str((time.split(':')[1][2]))=='b':
                            break
                        else:
                            print 'Please enter time in hh:mma or hh:mmp format'
                            time=raw_input('Please re-enter time: ')
                    else:
                        print 'Please enter time in hh:mma or hh:mmp format'
                        time=raw_input('Please re-enter time: ')
                except:
                    print 'Please enter time in hh:mma or hh:mmp format'
                    time=raw_input('Please re-enter time: ')
            else:
                print 'Please enter time in hh:mma or hh:mmp format'
                time=raw_input('Please re-enter time: ')
        except:
            print 'Please enter time in hh:mma or hh:mmp format'
            time=raw_input('Please re-enter time: ')
    return time

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


class Day:
    '''
    The Day class keeps a dictionary consisting of the 
    start and stop times of each shift in the form
    {start:stop, start:stop}.
    Times are maintained in both decimal and regular form.
    '''
    def __init__(self):
        self.shiftRegDict = {}
        self.shiftDecDict = {}
    def addShift(self):
        print 'List of current shifts:'
        print self.shiftRegDict
        start = CheckTime(raw_input('Enter the start time of the shift: '))
        end = CheckTime(raw_input('Enter the end time of the shift: '))
        self.shiftRegDict[start] = end
        self.shiftDecDict[TimetoDec(start)] = TimetoDec(end)
#    def editShift(self):
         
    def viewShift(self):
        return self.shiftRegDict

class TM:
    '''
    Maintains a class for each employee (TM). Keeps track of 
    maximum hours, a blacklist for days they can't work, and functions
    to add a shift
    '''
    def __init__(self, maxHours):
        self.maxHours = maxHours
        self.totalTime = 0
        self.blackList = []
    def addShift(self, time):
        self.totalTime += time
    def maxHours(self, newShift):
        if self.totalTime + newShift > self.maxHours:
            return False
        elif self.totalTime + newShift <= self.maxHours:
            return True
    def blackList(self, day):
        self.blackList.append(day)

Monday = Day()
Tuesday = Day()
Wednesday = Day()
Thursday = Day()
Friday = Day()
Saturday = Day()
Sunday = Day()

dayDict = {Monday:'Monday', Tuesday:'Tuesday', Wednesday:'Wednesday', Thursday:'Thursday', Friday:'Friday', Saturday:'Saturday',Sunday:'Sunday'}
'''
for day in dayDict:
    shiftNum = int(raw_input('How many shifts for ' + dayDict[day] + '? '))
    x = 0
    while x < shiftNum:
        day.addShift()
        day.viewShift()
        x+=1
'''
tmDict={}
tmNum = int(raw_input('How many employees are you staffing? '))
x = 0
while x < tmNum:
    name = raw_input('What is the name of employee number %i? '%(x+1))
    tmHours = int(raw_input('How many hours can %s work? '%name))
    classname = name
    classname = TM(tmHours)
    tmDict[classname] = name
    print tmDict
    x += 1
