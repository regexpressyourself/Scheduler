'''
------------
TO DO
------------
    [x]random assignment of shifts to employees
    [x]does not go over hours alloted for each TM
    [x]does not interfere with TM day off requests
    [x]does not interfere with TM shift off requests
    [x]refine excel worksheet- colors, bold, data manipulation, etc
    [x]fix day off user input
    [x]check if time is 1-12
    [x]Add IndexError exception for "10" input on time
    [x]make timeinput more lenient in general
    [x]make all input more lenient in general
    [x]on time input, make it more clear what shift you're adding to
    [x]check if end time is later than start time
    [x]run some checks on the time math- round dectotime
    [x]change the time confimation to the end of the time input.
    [x]add method to day class to return string and replace the dayDict BS
    [x]allow user to edit shift after print
    [x]check overnight shifts
    [x]"are there any OTHER days tm cant work?"
    [x]check that time off on a day doesnt conflict on either side
    [x]what days cant they work input needs work
    [kindof]Unavailable for shift unavailibility as well as day unavailability
    [ ]add shift preference
    [ ]get off cli
    [ ]focus on user experience - could a toddler do it?
    [ ]check all raw_inputs for new line on answer.
    [ ]also, with above, add new line after the answer
    [ ]if possible, avoid clopens
    [ ]change inputs for day off inputs
    [ ]comment out code
    [ ]add additional excel outputs
    [ ]
'''

#!/usr/bin/python2

import random
import xlwt

print '\n\n\n'
print '################################################################'
print '                 Welcome to my scheduling app!                  '
print 'Find more information at github.com/regexpressyourself/Scheduler'
print '                           Thanks!                              '
print '################################################################'
print "\nNow let's get started\n\n"


def NumberIncrement(number):
    if number in [1, '1']:
        return str(number) + 'st'
    elif number in [2, '2']:
        return str(number) + 'nd'
    elif number in [3, '3']:
        return str(number) + 'rd'
    else:
        return str(number) + 'th'


def TimetoDec(time):
    '''
    time is entered in the format "hh:mma" or "hh:mmp" and returned in a
    decimal form from 00.00 up to 23.99
    '''
    hour = float(time.split(':')[0])
    minute = float(time.split(':')[1][:2])
    ampm = str(time.split(':')[1][2])

    if hour == 12:
        if ampm == 'p':
            hour = 12
        elif ampm == 'a':
            hour == 0
    if ampm == 'p':
        if hour != 12:
            hour += 12.0

    minute = round(minute/60.0, 2)

    return hour+minute


def DectoTime(dec):
    '''
    time is entered in the decimal form (see TimetoDec) and
    returned in the hh:mma or hh:mmp form
    '''
    dec = str(dec)
    time = dec.split('.')
    minute = int(int(time[1])*.6)
    if int(time[0]) > 12:
        hour = int(time[0])-12
        ampm = 'p'
    else:
        hour = int(time[0])
        ampm = 'a'
    hour = str(hour)
    minute = str(minute)
    if len(minute) < 2:
        if minute == '0':
            minute = '0' + minute
        else:
            minute = minute + '0'
    return hour + ':' + minute + ampm


def FormatTime(time):
    '''
    Sanitize different time inputs to fit the hh:mma/hh:mmp format needed for
    conversion between decimal value and readable time value. The goal here
    is to make the time input a little more intuitive.

    NOTE: CheckInput does a final check in a loop, giving the user a chance to
    revise input. FormatTime is meant to fix common input errors for the user.
    Hopefully, it makes things a little easier.
    '''
    try:
        if time[-1] not in '0123456789':
            if time[-1] in ['m', 'M']:
                time = time[:-1]
            elif time[-1] == 'A':
                time = time[:-1]
                time = time + 'a'
            elif time[-1] == 'P':
                time = time[:-1]
                time = time + 'p'
            elif time[-1] in ['a', 'p']:
                time = time
            else:
                return False
        if time[-1] in ['a', 'p']:
            if len(time[:-1]) == 1:
                time = '0' + time[:-1] + ':00' + time[-1]
            elif len(time[:-1]) == 2:
                time = time[:-1] + ':00' + time[-1]
            elif len(time[:-1]) == 4:
                if ':' in time:
                    time = '0' + time
                else:
                    return False
            elif len(time[:-1]) == 5:
                if ':' in time:
                    time = time
                else:
                    return False
            else:
                return False
        elif ':' in time:
            hour = time.split(':')[0]
            if len(hour) == 1:
                try:
                    int(hour)
                    time = '0' + time
                except ValueError:
                    return False
            minute = time.split(':')[1]
            if minute[-1] in ['a', 'p']:
                minute = minute[:-1]
            try:
                int(minute)
            except ValueError:
                return False
            if len(minute) != 2:
                return False
        elif len(time) == 1:
            try:
                int(time)
                time = '0' + time + ':00'
            except ValueError:
                return False
        elif len(time) == 2:
            try:
                int(time)
                time = time + ':00'
            except ValueError:
                return False
        else:
            return False
    except IndexError:
        return False
    except ValueError:
        return False
    if time:
        if time[-1] not in ['a', 'p']:
            while True:
                print 'And was that AM or PM?'
                print ('(hint: put "a" or "p" at the end of your time ' +
                       'to avoid this step)')

                flag = raw_input(' (enter a for am or p for pm)\t')
                if flag in ['a', 'am', 'AM', 'Am', 'aM']:
                    time = time + 'a'
                    break
                elif flag in ['p', 'pm', 'PM', 'Pm', 'pM']:
                    time = time + 'p'
                    break
                else:
                    print "Sorry, I didn't get that"
                    continue
    return time


def CheckTime(time):
    def ErrorMessage():
        print '\nERROR: Please enter time in an approved format'
        newtime = FormatTime(raw_input('Please re-enter time: \n \n'))
        CheckTime(newtime)
        return newtime
    '''
    checks that time is entered in the format "hh:mma" or "hh:mmp"
    '''
    while True:
        try:
            float(time.split(':')[0])
            if len(((time.split(':')[0]))) == 2:
                if 0 < int((time.split(':')[0])) < 13:
                    try:
                        float((time.split(':')[1][:2]))
                        if -1 < int((time.split(':')[1][:2])) < 60:
                            if len(((time.split(':')[1][:2]))) == 2:
                                if str((time.split(':')[1][2])) == 'a':
                                    break
                                elif str((time.split(':')[1][2])) == 'p':
                                    break
                                else:
                                    time = ErrorMessage()
                            else:
                                time = ErrorMessage()
                        else:
                            time = ErrorMessage()
                    except IndexError:
                        time = ErrorMessage()
                    except AttributeError:
                        time = ErrorMessage()
                    except ValueError:
                        time = ErrorMessage()
                else:
                    time = ErrorMessage()
            else:
                time = ErrorMessage()
        except ValueError:
            time = ErrorMessage()
        except AttributeError:
            time = ErrorMessage()
        except IndexError:
            time = ErrorMessage()

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
        self.shiftRegList.append((start, end))  # list of shift in normal form
        self.shiftRegDict = dict(self.shiftRegList)
        # also in normal form, {start:end}

        self.shiftDecList.append((TimetoDec(start), TimetoDec(end)))
        # List of times in decimal form

        self.shiftDecDict = dict(self.shiftDecList)

    def removeShift(self, shiftIndex):
        del self.shiftRegDict[self.shiftRegList[shiftIndex][0]]
        self.shiftRegList.remove(self.shiftRegList[shiftIndex])
        del self.shiftDecDict[self.shiftDecList[shiftIndex][0]]
        self.shiftDecList.remove(self.shiftDecList[shiftIndex])

    def editShift(self, shiftIndex, newStart, newEnd):
        self.removeShift(shiftIndex)
        self.addShift(newStart, newEnd)

    def viewShift(self):
        x = 1
        for shift in self.shiftRegDict:
            viewTime = (self.shiftRegList[x-1][0] + ' - ' +
                        self.shiftRegList[x-1][1])
            print 'Shift ' + str(x) + ': ' + viewTime
            x += 1


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
        self.blackShiftDict = {}
        self.shiftDict = {}
        self.printShiftDict = {}

    def canWork(self, day, strDay, start, end):
        shiftTime = end-start
        if shiftTime < 0:
            shiftTime += 24
        if self.totalTime + shiftTime <= self.maxHours:
            if day in self.shiftDict:
                return False
            elif strDay.lower() in self.blackShiftDict:
                for time in self.blackShiftDict[strDay.lower()]:
                    if start < time < end:
                        return False
            elif strDay.lower() in self.blackList:
                return False
            else:
                return True
        else:
            return False

    def addShift(self, day, stringday, start, stop):

        shiftTime = stop-start
        if shiftTime < 0:
            shiftTime += 24
        try:
            self.shiftDict[day]
            self.shiftDict[day][start] = stop
        except:
            self.shiftDict[day] = {start: stop}
        try:
            self.printShiftDict[day]
            self.printShiftDict[day][DectoTime(start)] = DectoTime(stop)
        except:
            self.printShiftDict[day] = {DectoTime(start): DectoTime(stop)}
        self.totalTime += shiftTime

    def maxHours(self, newShift):
        if self.totalTime + newShift > self.maxHours:
            return False
        elif self.totalTime + newShift <= self.maxHours:
            return True

    def blacklist(self, day, dayClass):
        self.blackList[day] = dayClass

    def shiftBlacklist(self, day, start, end):
        try:
            self.blackShiftDict[day]
            self.blackShiftDict[day][start] = end
        except:
            self.blackShiftDict[day] = {start: end}

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
dayList = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

# dayPrintDict is for error checking the days off entries
dayPrintDict = {'monday': Monday, 'tuesday': Tuesday, 'wednesday': Wednesday,
                'thursday': Thursday, 'friday': Friday, 'saturday': Saturday,
                'sunday': Sunday}

'''
 dayDict allows the class name to correlate with a string of the name for
 printing purposes
 NOTE: this should be eradicated and replaced with a method "print" in the
 day class
'''
dayDict = {Monday: 'Monday', Tuesday: 'Tuesday', Wednesday: 'Wednesday',
           Thursday: 'Thursday', Friday: 'Friday', Saturday: 'Saturday',
           Sunday: 'Sunday'}

# get shift data for each day
for day in dayList:
    print '================================================'
    dayVar = dayDict[day]
    shiftNum = CheckInt(raw_input('How many shifts for ' +
                                  dayVar + '? \n \n'))
    x = 0
    while x < shiftNum:
        while True:
            print '------------------------------------------------'
            start = FormatTime(raw_input('Enter the STARTING time of the ' +
                                         NumberIncrement(str(x+1)) +
                                         ' shift on ' + dayVar + ": \n \n"))
            start = CheckTime(start)
            print '------------------------------------------------'
            end = FormatTime(raw_input('Enter the ENDING time of the ' +
                                       NumberIncrement(str(x+1)) +
                                       ' shift on ' + dayVar + ': \n \n' +
                                       start + ' - '))
            end = CheckTime(end)

            if TimetoDec(end) - TimetoDec(start) < 0:
                print "That's either an overnight shift or a mistake."
                validate = raw_input("Do you want to keep it as is?\n\n")
                if validate.lower() in ['yes', '', 'y', 'ye']:
                    day.addShift(start, end)
                    break
                else:
                    print "Ok, Let's try this again. \n"
                    pass
        print '\n--Added Shift-- \n\n'
        print '++++++++++++++++++++++++'
        print 'Shifts for ' + dayVar + ': \n'
        day.viewShift()
        print '++++++++++++++++++++++++\n\n'
        x += 1

# check that shifts are correct
while True:
    print '\n\n++++++++++++++++++++++++'
    for day in dayList:
        print '-----',
        print dayDict[day],
        print '-----'
        day.viewShift()
        print ''
    print '++++++++++++++++++++++++\n'

    print 'You may now edit your shifts. ',
    print 'If they look good, just press enter or',
    print ' enter "done" and we can move on to your employees.'
    editOption = raw_input('edit | remove | add | done >> ')
    print '\n'
    editOption = editOption.lower()
    if editOption == 'edit':
        while True:
            editDay = raw_input('What day do you need to edit?\n')
            editDay = editDay.lower()
            if editDay in dayPrintDict:
                editDay = dayPrintDict[editDay]
                while True:
                    print '++++++++++++++++++++++++'
                    editDay.viewShift()
                    print '++++++++++++++++++++++++\n'
                    print '\nEnter the NUMBER of the shift you wish to edit'
                    shiftIndex = raw_input('>> ')
                    try:
                        shiftIndex = int(shiftIndex)
                    except ValueError:
                        print "\n**Sorry, I didn't get that**\n"
                        continue
                    if shiftIndex in range(0, len(editDay.shiftRegDict)+1):
                        print '-----------------------------------------------'
                        inqueryString = ('Enter the new STARTING time of ' +
                                         'shift ' + str(shiftIndex) + '\n\n')
                        newStart = FormatTime(raw_input(inqueryString))
                        newStart = CheckTime(newStart)
                        print '-----------------------------------------------'
                        inqueryString = ('Enter the new ENDING time of ' +
                                         'shift ' + str(shiftIndex) + '\n\n')
                        newEnd = FormatTime(raw_input(inqueryString))
                        newEnd = CheckTime(newEnd)
                        editDay.editShift(shiftIndex-1, newStart, newEnd)
                        break
                    else:
                        print "\n**Sorry, I didn't get that**\n"
                        continue
                break
            else:
                print "\n**Sorry, I didn't get that**\n"
                continue

    elif editOption == 'remove':
        while True:
            editDay = raw_input('On what day do you need to remove a shift?\n')
            editDay = editDay.lower()
            if editDay in dayPrintDict:
                editDay = dayPrintDict[editDay]
                print '++++++++++++++++++++++++'
                editDay.viewShift()
                print '++++++++++++++++++++++++\n'
                while True:
                    print '\nEnter the NUMBER of the shift you wish to edit'
                    shiftIndex = raw_input('>> ')
                    try:
                        shiftIndex = int(shiftIndex)
                    except ValueError:
                        print "\n**Sorry, I didn't get that**\n"
                        continue
                    if shiftIndex in range(0, len(editDay.shiftRegDict)+1):
                        editDay.removeShift(shiftIndex-1)
                        break
                    else:
                        print "\n**Sorry, I didn't get that**\n"
                        continue
                break
            else:
                print "\n**Sorry, I didn't get that**\n"
                continue

    elif editOption == 'add':
        while True:
            editDay = raw_input('On what day do you need to add a shift?\n')
            editDay = editDay.lower()
            if editDay in dayPrintDict:
                editDay = dayPrintDict[editDay]
                print '------------------------------------------------'
                newStart = FormatTime(raw_input('Enter the new STARTING time' +
                                                ' of your new shift \n\n'))
                newStart = CheckTime(newStart)
                print '------------------------------------------------'
                newEnd = FormatTime(raw_input('Enter the new ENDING time of' +
                                              ' your new shift \n\n'))
                newEnd = CheckTime(newEnd)
                editDay.addShift(newStart, newEnd)
                break
            else:
                print "\n**Sorry, I didn't get that**\n"
                continue

    elif editOption in ['done', '']:
        break
    else:
        print "\n**Sorry, I didn't get that**\n"
        continue
'''
tmDict and tmList work simlarly to dayDict and dayList to store classes and
printable names for all the employees
'''
tmDict = {}
tmList = []
print '------------------------------------------------'
tmNum = CheckInt(raw_input('How many employees are you staffing? \n \n'))

# make a class for each tm and a add a corresponding name
x = 0
while x < tmNum:
    print '------------------------------------------------'
    name = raw_input('What is the name of your ' + NumberIncrement((x+1)) +
                     ' employee? \n \n')
    print '------------------------------------------------'
    tmHours = CheckInt(raw_input('How many hours can %s work? \n \n' % name))
    classname = name
    classname = TM(tmHours)
    tmList.append(classname)
    tmDict[classname] = name
    while True:
        print '------------------------------------------------'
        if len(classname.blackList) + len(classname.blackShiftDict) == 0:
            blacklist = raw_input("What days can't %s work?"
                                  % tmDict[classname].lower() +
                                  " (press enter if none) \n")
        else:
            blacklist = raw_input("Are there any other days %s can't work?"
                                  % tmDict[classname].lower() +
                                  " (simply press enter when finished) \n")
        if blacklist.lower() in dayPrintDict:
            while True:
                shiftCheck = raw_input("\n\n****Is " + name + " unavailable " +
                                       "for all of " + blacklist + "?\n\n")
                if shiftCheck in ['n', 'no', 'No', 'NO', 'N']:
                    print "-----------------------------------------------"
                    inqueryString = ("Enter the STARTING time of " + name +
                                     "'s" + " unavailability for " +
                                     blacklist + "\n\n")
                    shiftBlacklistStart = FormatTime(raw_input(inqueryString))
                    shiftBlacklistStart = CheckTime(shiftBlacklistStart)
                    print "-----------------------------------------------"
                    inqueryString = ("Enter the ENDING time of " + name +
                                     "'s" + " unavailability for " +
                                     blacklist + "\n\n")
                    shiftBlacklistEnd = FormatTime(raw_input(inqueryString))
                    shiftBlacklistEnd = CheckTime(shiftBlacklistEnd)
                    classname.shiftBlacklist(blacklist, shiftBlacklistStart,
                                             shiftBlacklistEnd)
                    break

                elif shiftCheck in ['y', 'yes', 'Yes', 'YEs', 'YES', 'Y']:
                    classname.blacklist(blacklist, dayPrintDict[blacklist])
                    break
                else:
                    print "***Sorry, didn't get that.***"
                    print ("Enter yes if " + name + " is not available for " +
                           "the whole day)")
                    print ("Enter no if " + name + " is available for " +
                           "just a part of the day. \n")
        elif blacklist in ['0', 'none', 'no', 'n', 'done']:
            break
        elif blacklist == '':
            break
        else:
            print "Please enter a day, or press enter to finish \n \n"
    x += 1


# unassigned stores all the extra shifts (hence the huge "maxhour" number)
unassigned = TM(999999999999999999999999999999999)

'''
OK this is the convuluted part. Here goes:
- For every shift, a string of random integers (which reperesent the index
numbers of tmList) is generated.
- Using these random integers, a tm is selcted at random. If they pass the
"caWork" test, the shift is assigned to them. Otherwise, we just continue down
the list.
- If every TM fails the "canWork" test, the shift is assigned to "unassigned"
and an error message is printed.
'''

print 'Assigning shifts...'
unassignedString = ''
for day in dayDict:
    for shift in day.shiftDecDict:
        numList = []
        for num in range(0, len(tmList)):
            numList.append(num)
        random.shuffle(numList)
        x = 0
        while True:
            if x >= len(numList):
                unassignedString += str(dayDict[day]) + '  '
                unassignedString += str(DectoTime(shift)) + '-'
                unassignedString += (str(DectoTime(day.shiftDecDict[shift])) +
                                     '\n')
                unassigned.addShift(day, dayDict[day], shift,
                                    day.shiftDecDict[shift])
                break
            else:
                shiftTM = tmList[numList[x]]
            if shiftTM.canWork(day, dayDict[day], shift,
                               day.shiftDecDict[shift]):
                shiftTM.addShift(day, dayDict[day], shift,
                                 day.shiftDecDict[shift])
                break
            else:
                x += 1

if len(unassignedString) > 0:
    print 'Following shift(s) could not be assigned:'
    print unassignedString
print 'Done! Your schedule can be found in the same directory as this program.'
print 'Look for schedule.xls'

# Excel printing
# the next 30 lines or so just make a template for the cells to work with.
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Schedule')

tempString = ("align: horiz center, vert center; pattern: pattern solid; " +
              "borders: bottom thick, top thick, left thick, right thick")
grey = xlwt.easyxf(tempString)
grey.pattern.pattern_fore_colour = 22

tempString = ("font: bold on; borders: bottom thick, top thick, " +
              "left thick, right thick")
bold = xlwt.easyxf(tempString)

tempString = ("font: bold on; align: horiz center, vert center; " +
              "borders: bottom thick, top thick, left thick, right thick")
boldcenter = xlwt.easyxf(tempString)

tempString = ("align: horiz center; borders: left thick, top thick, " +
              "right no_line, bottom no_line")
left = xlwt.easyxf(tempString)

tempString = ("align: horiz center; borders: top thick, right thick, " +
              "bottom no_line, left no_line")
right = xlwt.easyxf(tempString)

tempString = ("align: horiz center; borders: top thick, bottom no_line, " +
              "right no_line, left no_line")
center = xlwt.easyxf(tempString)

tempString = ("borders: bottom thick, top thick, left thick, right thick")

thick = xlwt.easyxf(tempString)
notop = xlwt.easyxf('borders: bottom thick, left thick, right thick')

# Onto the actual data input for excel
x = 3
y = 0
while x < len(dayList)*3+3:
    sheet.write_merge(0, 0, x, x+2, dayDict[dayList[y]], boldcenter)
    y += 1
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
            sheet.write(x+y, (dayList.index(day)*3)+5,
                        tm.printShiftDict[day][shift], right)
            sheet.write_merge(x+y+1, x+y+1, (dayList.index(day)*3)+3,
                              (dayList.index(day)*3)+5, '', notop)
            y += 2
    for day in tm.blackList:
        sheet.write_merge(x, x+1, (dayList.index(tm.blackList[day])*3)+3,
                          (dayList.index(tm.blackList[day])*3)+5,
                          'Not Available', grey)
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
