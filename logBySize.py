
import logging
import getpass
import os
try :
    logs_file = os.stat('logs.log')
    logs_size = logs_file.st_size
    print(f'logs file size = {logs_size} bytes')
    if logs_size > 1000 :       # if file size over 1 k
        with open('logs.log','r') as fr:
            lines = fr.readlines()
            print(lines)
            ptr = 1
            with open('logs.log','w') as fw:
                for line in lines:
                    print(line)
                    if ptr > 10:        # delete 10 line
                        fw.write(line)
                        print('delete')
                    ptr += 1
                    print('Deleted')

except Exception as e:
    print(e)
    # print('Not logs.log')
    pass


logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.logProcesses,
                    format=(f'%(asctime)s {getpass.getuser()} : %(levelname)s : %(message)s'))

def debug01():
     logging.debug('This is debug')
     logging.info('INFO')
     logging.warning('Warning')
     logging.error('ERROR ')
     logging.critical("The program crashed")

debug01()