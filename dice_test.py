# This is a dice test program for calling pydice

from rpg_tools.pydice import roll
import os
import logging

__app__ = 'dice_test'

if __name__ == '__main__':

    '''
    Technically, this program starts right here when run.
    If this program is imported instead of run, none of the code below is executed.
    '''

#     logging.basicConfig(filename = 'dice_test.log',
#                         level = logging.DEBUG,
#                         format = '%(asctime)s %(levelname)s %(name)s - %(message)s',
#                         datefmt='%a, %d %b %Y %H:%M:%S',
#                         filemode = 'w')

    log = logging.getLogger('your_logger_function_here')
    log.setLevel(logging.DEBUG)

    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    
    fh = logging.FileHandler('Logs/dice_test.log', 'w')
 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s', datefmt = '%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)
    log.addHandler(fh)

    log.info('Logging started.')

    log.info(__app__ + ' started, and running...')

print(roll('3d6+2 # weapon damage'))
print(roll('4d6l3+2'))
print(roll('dd+3'))
print(roll('sicherman # like a 2d6 roll'))
print(roll('# default roll'))
print(roll('hex # (0-F)'))
print(roll('d01 # coin toss'))
