#!/usr/bin/python3
import logging
import getpass
import os

global logsFile
logsFile = 'logs.log'
logging.basicConfig(filename=logsFile, encoding='utf-8', level=logging.logProcesses,
                    format=(f'%(asctime)s {getpass.getuser()} : %(levelname)s : %(message)s'))

def deleteLogs(num):
    try :
        if num is not None:
            with open(logsFile,'r') as fr:
                lines = fr.readlines()
                ptr = 1
                with open(logsFile,'w') as fw:
                    for line in lines:
                        if ptr > num:
                            fw.write(line)
                        ptr += 1
                        print('Deleted')
                logging.debug('Delete older log')
        if num is None:
            pass
    except Exception as e:
        print(e)

def getLineNumberOfLogs():
    try :
        with open(logsFile,"r") as fr:
            last_line = fr.readlines()[-1]
            last1 = last_line.split(' ')[0]
            last = last1.split('-')
            last_y = last[0]
            last_m = last[1]
            last_d = last[2]
            #-----------------------  Convert to int for set delete 1 year
            lookup1 = int(last_y)-1
            lookup = (f'{str(lookup1)}-{last_m}-{last_d}')
            with open(logsFile,"r") as fr:
                for num, line in enumerate(fr,1):
                    if lookup in line:
                        return num

                    
    except Exception as e:
        print(e)
        pass
    
num = getLineNumberOfLogs()
deleteLogs(num)


def debug01():
     logging.debug('This is debug')
     logging.info('INFO')
     logging.warning('Warning')
     logging.error('ERROR ')
     logging.critical("The program crashed")

#debug01()
