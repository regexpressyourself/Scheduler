import random
HourDict={'12:00a':0,'1:00a':1,'2:00a':2,'3:00a':3,'4:00a':4,'5:00a':5,'6:00a':6,'7:00a':7,'8:00a':8,'9:00a':9,'10:00a':10,'11:00a':11,'12:00p':12,'1:00p':13,'2:00p':14,'3:00p':15,'4:00p':16,'5:00p':17,'6:00p':18,'7:00p':19,'8:00p':20,'9:00p':21,'10:00p':22,'11:00p':23,}


class Day:
	def __init__(self):
		self.opnstart=[]
		self.opnend=[]
		self.midstart=[]
		self.midend=[]
		self.clsstart=[]
		self.clsend=[]
		self.fullshiftsstart=[]
		self.fullshiftsend=[]
	def AddOpn(self, start, stop):
		self.opnstart.append(start)
		self.opnend.append(stop)
		self.fullshiftsstart.append(start)
		self.fullshiftsend.append(stop)
	def AddMid(self, start, stop):
		self.midstart.append(start)
		self.midend.append(stop)
		self.fullshiftsstart.append(start)
		self.fullshiftsend.append(stop)
	def AddCls (self, start, stop):
		self.clsstart.append(start)
		self.clsend.append(stop)
		self.fullshiftsstart.append(start)
		self.fullshiftsend.append(stop)
	def PrintShift(self):
		x=0
		while x<len(self.fullshiftsstart):
			print self.fullshiftsstart[x],
			print '-',
			print self.fullshiftsend[x]
			x+=1

class TM:
#TM is made to keep track a team member's (aka 'TM') hours. you can enter how many hours a week a tm works, and call AtFullTime to see if they have reached their weekly quota. 
	def __init__(self, fulltime):
		self.time=0
		self.fulltime=fulltime
		self.blackList=[]
	def AddHours(self, hours):
		self.time+=hours
	def RemoveHours(self,hours):
		self.time=self.time-hours
	def AtFullTime(self,hours):
		self.AddHours(hours)
		if self.time>self.fulltime:
			self.RemoveHours(hours)
			return True
		else:
			self.RemoveHours(hours)
			return False
	def BlackList(self, day):
		self.blackList.append(day)
def IsNumber(num):
	
	while True:
		try:
			int(num)
			return True
			break
		except ValueError:
			print 'Oops make sure to enter a number'
			return False
		except SyntaxError:
			print 'Oops make sure to enter a number' 
			return False
		except NameError:
			print 'Oops make sure to enter a number' 
			return False

def ShiftSet(day):     
#ShiftSet takes a "Day()" class and assigns the proper times to its dictionaries. 

#the following takes in the number of open, mid, and close shifts, along with checking a (rather exhaustive) group of errors.
	while True:
		OpnNum=1#input('how many open shifts? \n')
		if OpnNum=='quit':
			break
		if IsNumber(OpnNum)==True:
			break
	while True:
		MidNum=1#input('how many open shifts? \n')
		if MidNum=='quit':
			break
		if IsNumber(MidNum)==True:
			break
	while True:
		ClsNum=1#input('how many open shifts? \n')
		if ClsNum=='quit':
			break
		if IsNumber(ClsNum)==True:
			break
	
#after gathering how many shifts are needed throughout the day, ShiftSet then prompts the user for the specific times of the shifts. The individual shifts are kept in their respective dictionaries (open, mid, and close), in the format {start time:close time} as well as a full dictionary of shifts for each day. 	
	x=0
	while x<OpnNum:
		day.AddOpn('7:00a','3:00p')#str(raw_input('open %s start time? Please use format HH:MMa or HH:MMp (ex: 12:30p, 07:00a, etc)'%str(x+1))),str(raw_input('open %s end time? Please use format HH:MMa or HH:MMp (ex: 12:30p, 07:00a, etc) '%str(x+1))))
	
		x+=1

	x=0
	while x<MidNum:
		day.AddMid('11:00a','7:00p')#str(raw_input('mid %s start time? Please use format HH:MMa or HH:MMp (ex: 12:30p, 07:00a, etc) '%str(x+1))),str(raw_input('mid %s end time?  Please use format HH:MMa or HH:MMp (ex: 12:30p, 07:00a, etc) '%str(x+1))))
		x+=1
	x=0
	while x<ClsNum:
		day.AddCls('2:00p','10:00p')#str(raw_input('close %s start time?  Please use format HH:MMa or HH:MMp (ex: 12:30p, 07:00a, etc) '%str(x+1))),str(raw_input('close %s end time?  Please use format HH:MMa or HH:MMp (ex: 12:30p, 07:00a, etc) '%str(x+1))))
		x+=1
def TmAvail(tm,start,stop,day):
	time=HourDict[stop]-HourDict[start]
	if tm.AtFullTime(time):
		return False
	elif day.lower() in tm.blackList:
		return False
	else:
		return True
#eventually will be a way to check against multiple availability issues like clopens, buying classes, available hours, etc. perhaps implement a way for the user to input limitations on TMs?


def RandListGen():
        x=0
        randList=[]
        while x<len(TMList):
                randList.append(x)
                x+=1
        return randList
#this is simple, just generates a list of numbers for randList. arguably easier thn just typing it out?


def PrintShifts(day):
	y=0
	z=len(TMList)-1
#y and z are simply parameters
	print WeekDict[day]
	i=0
	x=0
	j=len(day.opnstart)
	randList=RandListGen()
	while x<j:
		if len(randList)==0:
			print "You're all out of TMs. Please start over and make sure not to add more shifts than TMs available. Silly."
			break
#above checks if everyone has already worked that day
		print day.opnstart[0]+' - ',
		print day.opnend[0],
		print '       ',
		i=0
		while i==0:
			tmNum=random.randint(y,z)
			if tmNum in randList:
				if TmAvail(ClassTMList[tmNum],day.opnstart[0],day.opnend[0],WeekDict[day]):
					print TMList[tmNum]
					randList.remove(tmNum)
					i+=1
				else:
					pass
			elif tmNum not in randList:
				pass
		x+=1

		day.opnstart.pop(0)
		day.opnend.pop(0)
        i=0
	x=0
	j=len(day.midstart)
	while x< j:
		if len(randList)==0:
			print "You're all out of TMs. Please start over and make sure not to add more shifts than TMs available. Silly."
			break
		print day.midstart[0]+' - ',
		print day.midend[0],
		print '       ',
		i=0
		while i==0:
			tmNum=random.randint(y,z)
			if tmNum in randList:
				if TmAvail(ClassTMList[tmNum],day.midstart[0],day.midend[0],WeekDict[day]):
					print TMList[tmNum]
					randList.remove(tmNum)
					i+=1
				else:
					pass
			elif tmNum not in randList:
				pass
		x+=1

		day.midstart.pop(0)
		day.midend.pop(0)
        i=0
	x=0
	j=len(day.clsstart)
	while x<j:
		if len(randList)==0:
			print "You're all out of TMs. Please start over and make sure not to add more shifts than TMs available. Silly."
			break
		print day.clsstart[0]+' - ',
		print day.clsend[0],
		print '       ',
		i=0
		while i==0:
			tmNum=random.randint(y,z)
			if tmNum in randList:
				if TmAvail(ClassTMList[tmNum],day.clsstart[0],day.clsend[0],WeekDict[day]):
					print TMList[tmNum]
					randList.remove(tmNum)
					i+=1
				else:
					pass
			elif tmNum not in randList:
				pass
		x+=1

		day.clsstart.pop(0)
		day.clsend.pop(0)


Monday=Day()
Tuesday=Day()
Wednesday=Day()
Thursday=Day()
Friday=Day()
Saturday=Day()
Sunday=Day()
#WeekList is a list of each day's class
WeekList=[Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday]
StrWeekList=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
#WeekDict corresponds the class to a name in string format. Probable a better way to be able to call the name, but this works too :)
WeekDict={Monday:'Monday',Tuesday:'Tuesday',Wednesday:'Wednesday',Thursday:'Thursday',Friday:'Friday',Saturday:'Saturday',Sunday:'Sunday'}

#This simply calls ShiftSet for each day of the week
for day in WeekList:
	print '\n'
	print 'SHIFTS FOR %s' %WeekDict[day]
	print '\n'
	ShiftSet(day)


x= int(raw_input('How many TMs (PT and FT) will be working this week?'))
y=0
TMList=[]
ClassTMList=[]
TMDict={}
while y<x:
	tm=str(raw_input('TM name? '))
	TMList.append(tm)
	y+=1
for tm in TMList:

	while True:
		hours=raw_input('how many hours can %s work this week? '%tm)
		if hours=='quit':
			break
		if IsNumber(hours)==True:
			break
	tm1=tm
	tm=TM(hours)
	ClassTMList.append(tm)
	
	x=raw_input('are there any days %s cannot work this week? (enter "y" for yes or "n" for no) '%tm1)
	x.lower()
	if x=='y':
	
		while True:
			i=raw_input('how many day is %s unavailable? '%tm1)
			if i=='quit':
				break
			if IsNumber(i)==True:
				break
		y=0
		while y<int(i):
			while True:
				day=raw_input('enter each day %s cannot work, hitting enter after each entry: '%tm1)
				day.lower()
				if day in StrWeekList:
					tm.BlackList(day)
					break
				else:
					print 'make sure to enter a day'
			y+=1
	elif x=='n':
		pass
	else:
		print 'please enter "y" or "n"'


x=0
while x<len(TMList):
	TMDict[ClassTMList[x]]=TMList[x]
	x+=1
for day in WeekList:
	PrintShifts(day)
