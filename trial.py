def CheckTime(time):
     '''
     checks that time is entered in the format "hh:mma" or "hh:mmp"
     '''
     while True:
         try:
             int(time.split(':')[0])
             if len(((time.split(':')[0])))==2:
                 try:
                     int((time.split(':')[1][:2]))
                     if len(((time.split(':')[1][:2])))==2:
                         print str((time.split(':')[1][2]))
                         if str((time.split(':')[1][2]))=='a':
                             break
                         elif str((time.split(':')[1][2]))=='p':
                             break
                         else:
                             print '1Please enter time in hh:mma or hh:mmp format'
                             time=raw_input('Please re-enter time: ')
                     else:
                         print '2Please enter time in hh:mma or hh:mmp format'
                         time=raw_input('Please re-enter time: ')
                 except ValueError:
                     print '3Please enter time in hh:mma or hh:mmp format'
                     time=raw_input('Please re-enter time: ')
             else:
                 print '4Please enter time in hh:mma or hh:mmp format'
                 time=raw_input('Please re-enter time: ')
         except ValueError:
              print '5Please enter time in hh:mma or hh:mmp format'
              time=raw_input('Please re-enter time: ')
     return time

CheckTime(raw_input(' : '))
