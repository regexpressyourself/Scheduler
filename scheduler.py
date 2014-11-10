import random
import xlwt

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
                        if str((time.split(':')[1][2]))=='a':
                            break
                        elif str((time.split(':')[1][2]))=='p':
                            break
                        else:
                            print 'Please enter time in hh:mma or hh:mmp format'
                            time=raw_input('Please re-enter time: ')
                    else:
                        print 'Please enter time in hh:mma or hh:mmp format'
                        time=raw_input('Please re-enter time: ')
                except ValueError:
                    print 'Please enter time in hh:mma or hh:mmp format'
                    time=raw_input('Please re-enter time: ')
            else:
                print 'Please enter time in hh:mma or hh:mmp format'
                time=raw_input('Please re-enter time: ')
        except ValueError:
            print 'Please enter time in hh:mma or hh:mmp format'
            time=raw_input('Please re-enter time: ')
    return time

def CheckInt(num):
    while True:
        try: 
            int(num)
            return int(num)
            break
        except ValueError:
            num = raw_input('Please enter an integer: ')

def TimetoDec(time):
    '''
    time is entered in the format "hh:mma" or "hh:mmp" and returned in a 
    decimal form from 00.00 up to 23.99
    '''
    hour = float(time.split(':')[0])
    minute = float(time.split(':')[1][:2])
    ampm = str(time.split(':')[1][2])

    if ampm == 'p':
        if hour != 12:
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
        self.shiftRegList = []
        self.shiftDecDict = {}
        self.shiftDecList = []
    def addShift(self):
        start = CheckTime(raw_input('Enter the start time of the shift: '))
        end = CheckTime(raw_input('Enter the end time of the shift: '))
        self.shiftRegList.append((start,end))
        self.shiftRegDict = dict(self.shiftRegList)
        self.shiftDecList.append((TimetoDec(start),TimetoDec(end)))
        self.shiftDecDict = dict(self.shiftDecList)
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
        self.shiftDict = {}
        self.printShiftDict = {}
    def canWork(self, day, start, end):
        shiftTime = end-start
        if self.totalTime + shiftTime <= self.maxHours:
            if day not in self.shiftDict:
                return True
            else:
                return False
        else:
            return False
    def addShift(self, day, stringday, start, stop):
        shiftTime = stop-start
        self.shiftDict[day] = {start:stop}
        self.printShiftDict[day] = {DectoTime(start):DectoTime(stop)}
        self.totalTime += shiftTime
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

dayList = [Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday]

dayDict = {Monday:'Monday', Tuesday:'Tuesday', Wednesday:'Wednesday', Thursday:'Thursday', Friday:'Friday', Saturday:'Saturday',Sunday:'Sunday'}

for day in dayList:
    shiftNum = CheckInt(raw_input('How many shifts for ' + str(dayDict[day]) + '? '))
    x = 0
    while x < shiftNum:
        day.addShift()
        day.viewShift()
        x+=1


tmDict = {}
tmList = []
tmNum = CheckInt(raw_input('How many employees are you staffing? '))
x = 0
while x < tmNum:
    name = raw_input('What is the name of employee number %i? '%(x+1))
    tmHours = CheckInt(raw_input('How many hours can %s work? '%name))
    classname = name
    classname = TM(tmHours)
    tmList.append(classname)
    tmDict[classname] = name
    x += 1

for day in dayDict:
    for shift in day.shiftDecDict:
        numList = []
        for num in range(0,len(tmList)):
            numList.append(num)
        random.shuffle(numList)
        x=0
        while True:
            shiftTM = tmList[numList[x]]
            if shiftTM.canWork(day, shift, day.shiftDecDict[shift]):
                shiftTM.addShift(day, dayDict[day], shift, day.shiftDecDict[shift])
                break
            elif x >= len(numList):
                print 'Following shift could not be assigned:'
                print dayDict[day],
                print str(DectoTime(shift)) + '-' + str(DectoTime(day.shiftDecDict[shift]))
                break
            else:
                x+=1
'''
for tm in tmList:
    print tmDict[tm] + ':'
    for day in dayList:
        if day in tm.shiftDict:
            print dayDict[day],
            for item in tm.printShiftDict[dayDict[day]]:
                print item + ' - ' +  tm.printShiftDict[dayDict[day]][item]
'''

#Excel

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Schedule')
x=0
while x<len(dayList):
    sheet.write(0,x+1,dayDict[dayList[x]])
    x += 1

x=1
for tm in tmList:
    sheet.write(x,0,tmDict[tm])
    for shift in tm.printShiftDict:
        for item in tm.printShiftDict[shift]:
            time = item + ' - ' +  tm.printShiftDict[shift][item]
        sheet.write(x, dayList.index(shift)+1, time)
        
    x += 1
workbook.save('schedule.xls')
