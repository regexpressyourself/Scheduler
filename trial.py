# -*- coding: utf-8 -*-
while True:
    time=raw_input('here: ')
    try:
        float(time.split(':')[0]) 
        if len(((time.split(':')[0])))==2:
            try:
                float((time.split(':')[1][:2]))
                if len(((time.split(':')[1][:2])))==2:

                    if str((time.split(':')[1][2]))=='a' or str((time.split(':')[1][2]))=='b':
                        print 'yay'
                        break
            except:
                print 'hello'
    except:
        print 'hello'
