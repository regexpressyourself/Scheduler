'''
------------
TO DO
------------
    [x]random assignment of shifts to employees
    [x]does not go over hours alloted for each TM
    [x]does not interfere with TM day off requests
    [ ]does not interfere with TM shift off requests
    [ ]if possible, avoid clopens
    [ ]change inputs for day off inputs
    [ ]comment out code
    [x]refine excel worksheet- colors, bold, data manipulation, etc
    [ ]add shift preference
    [ ]get off cli
    [x]fix day off user input
    [ ]
    [ ]
    [ ]
    [ ]
    [ ]
    [ ]
    [ ]
    [ ]

'''
import random
import xlwt
#check if time is 1-12
#Add IndexError exception
#make time input more lenient
#make all input more lenient
#user experience
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
                            time=raw_input('Please re-enter time: \n \n')
                    else:
                        print 'Please enter time in hh:mma or hh:mmp format'
                        time=raw_input('Please re-enter time: \n \n')
                except ValueError:
                    print 'Please enter time in hh:mma or hh:mmp format'
                    time=raw_input('Please re-enter time: \n \n')
            else:
                print 'Please enter time in hh:mma or hh:mmp format'
                time=raw_input('Please re-enter time: \n \n')
        except ValueError:
            print 'Please enter time in hh:mma or hh:mmp format'
            time=raw_input('Please re-enter time: \n \n')
    return time

def CheckInt(num):
    '''
    Checks that number is integer
    '''
    while True:
        try:
            int(num)
            return int(num)
            break
        except ValueError:
            num = raw_input('Please enter an integer: \n \n')

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
    hour = str(hour)
    minute = str(minute)
    if len(minute)<2:
        if minute == '0':
            minute = '0' + minute
        else:
            minute = minute + '0'
    return hour + ':' + minute + ampm


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
    def addShift(self, start, end):
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
        self.blackList = {}
        self.shiftDict = {}
        self.printShiftDict = {}
    def canWork(self, day, strDay, start, end):
        shiftTime = end-start
        if self.totalTime + shiftTime <= self.maxHours:
            if day in self.shiftDict:
                return False
            elif strDay.lower() in self.blackList:
                return False
            else:
                return True
        else:
            return False
    def addShift(self, day, stringday, start, stop):
        shiftTime = stop-start
        try:
            self.shiftDict[day]
            self.shiftDict[day][start] = stop
        except:
            self.shiftDict[day] = {start:stop}
        try:
            self.printShiftDict[day]
            self.printShiftDict[day][DectoTime(start)] = DectoTime(stop)
        except:
            self.printShiftDict[day] = {DectoTime(start):DectoTime(stop)}
        self.totalTime += shiftTime
    def maxHours(self, newShift):
        if self.totalTime + newShift > self.maxHours:
            return False
        elif self.totalTime + newShift <= self.maxHours:
            return True
    def blacklist(self, day, dayClass):
        self.blackList[day] = dayClass

'''
classify all the days
'''
Monday = Day()
Tuesday = Day()
Wednesday = Day()
Thursday = Day()
Friday = Day()
Saturday = Day()
Sunday = Day()

# dayList is used mostly for indexing purposes, as dictionaries have no index
dayList = [Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday]

#dayPrintDict is for error checking the days off entries
dayPrintDict = {'monday':Monday,'tuesday':Tuesday,'wednesday':Wednesday,'thursday':Thursday,'friday':Friday,'saturday':Saturday,'sunday':Sunday}

'''
 dayDict allows the class name to correlate with a string of the name for
 printing purposes
'''
dayDict = {Monday:'Monday', Tuesday:'Tuesday', Wednesday:'Wednesday', Thursday:'Thursday', Friday:'Friday', Saturday:'Saturday',Sunday:'Sunday'}

#get shift data for each day
for day in dayList:
    shiftNum = CheckInt(raw_input('How many shifts for ' + str(dayDict[day]) + '? \n \n'))
    x = 0
    while x < shiftNum:
        start = CheckTime(raw_input('Enter the start time of the shift: \n \n'))
        end = CheckTime(raw_input('Enter the end time of the shift: \n \n'))
        day.addShift(start, end)
        day.viewShift()
        x+=1

'''
tmDict and tmList work simlarly to dayDict and dayList to store classes and
printable names for all the employees
'''
tmDict = {}
tmList = []
tmNum = CheckInt(raw_input('How many employees are you staffing? \n \n'))

#make a class for each tm and a add a corresponding name
x = 0
while x < tmNum:
    name = raw_input('What is the name of employee number %i? \n \n'%(x+1))
    tmHours = CheckInt(raw_input('How many hours can %s work? \n \n'%name))
    classname = name
    classname = TM(tmHours)
    tmList.append(classname)
    tmDict[classname] = name
    x += 1

# add days off to tm.blackList
for tm in tmList:
    while True:
        blacklist = raw_input("What days can't %s work? (press enter to skip ) \n \n"%tmDict[tm]).lower()
        if blacklist in dayPrintDict:
            tm.blacklist(blacklist, dayPrintDict[blacklist])
        elif blacklist == '':
            break
        else:
            print "Please enter a day, or press enter to finish \n \n"

#unassigned stores all the extra shifts (hence the huge "maxhour" number)
unassigned = TM(999999999999999999999999999999999)

'''
OK this is the convuluted part. Here goes:
- For every shift, a string of random integers (which reperesent the index
numbers of tmList) is generated.
- Using these random integers, a tm is selcted at random. If they pass the
"caWork" test, the shift is assigned to them. Otherwise, we just continue down
the list.
- If every TM fails the "canWork" test, the shift is assigned to "unassigned" and
an error message is printed.
'''

for day in dayDict:
    for shift in day.shiftDecDict:
        numList = []
        for num in range(0,len(tmList)):
            numList.append(num)
        random.shuffle(numList)
        x=0
        while True:
            if x >= len(numList):
                print 'Following shift could not be assigned:'
                print dayDict[day],
                print str(DectoTime(shift)) + '-' + str(DectoTime(day.shiftDecDict[shift]))
                unassigned.addShift(day, dayDict[day], shift, day.shiftDecDict[shift])
                break
            else:
                shiftTM = tmList[numList[x]]
            if shiftTM.canWork(day, dayDict[day], shift, day.shiftDecDict[shift]):
                shiftTM.addShift(day, dayDict[day], shift, day.shiftDecDict[shift])
                break
            else:
                x+=1

#Excel printing

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Schedule')

grey = xlwt.easyxf('align: horiz center, vert center; pattern: pattern solid; borders: bottom thick, top thick, left thick, right thick')
grey.pattern.pattern_fore_colour = 22

bold = xlwt.easyxf("font: bold on; borders: bottom thick, top thick, left thick, right thick")
boldcenter = xlwt.easyxf("font: bold on; align: horiz center, vert center; borders: bottom thick, top thick, left thick, right thick")

left = xlwt.easyxf('align: horiz center; borders: left thick, top thick, right no_line, bottom no_line')
right = xlwt.easyxf('align: horiz center; borders: top thick, right thick, bottom no_line, left no_line')
center = xlwt.easyxf('align: horiz center; borders: top thick, bottom no_line, right no_line, left no_line')

thick = xlwt.easyxf('borders: bottom thick, top thick, left thick, right thick')

notop = xlwt.easyxf('borders: bottom thick, left thick, right thick')

x = 3
y = 0
while x<len(dayList)*3+3:
    sheet.write_merge(0, 0, x, x+2, dayDict[dayList[y]], boldcenter)
    y +=1
    x += 3

tmList.append(unassigned)
tmDict[unassigned] = 'unassigned'
sheet.write(0, 24, "Total Hours", bold)

x = 1
for tm in tmList:
    sheet.write_merge(x, x+1, 0, 1, tmDict[tm], boldcenter)
    for day in tm.printShiftDict:
        y = 0
        for shift in tm.printShiftDict[day]:
            sheet.write(x+y, (dayList.index(day)*3)+3, shift, left)
            sheet.write(x+y, (dayList.index(day)*3)+4, '-', center)
            sheet.write(x+y, (dayList.index(day)*3)+5, tm.printShiftDict[day][shift], right)
            sheet.write_merge(x+y+1, x+y+1, (dayList.index(day)*3)+3, (dayList.index(day)*3)+5, '', notop)
            y += 2
    for day in tm.blackList:
        sheet.write(x, dayList.index(tm.blackList[day])+1, 'Not Available',grey)
    sheet.write_merge(x, x+1, 24, 24, tm.totalTime, thick)
    x += 2

x = 1
while x < len(tmList)*2+1:
    sheet.write_merge(x, x+1, 2, 2, '', thick)
    x += 2

y = 1
while y <= len(tmList)*2:
    x = 1
    while x <= len(dayList)*3+3:
        try:
            sheet.write_merge(y, y+1, x, x+2, 'OFF', grey)
        except:
            pass
        x += 1
    y += 1


workbook.save('schedule.xls')
