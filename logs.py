import logging
import os

logfile = os.path.join(os.getenv('HOME'), 'test.log')
print 'logfile: ' + logfile

logging.basicConfig(level=logging.DEBUG, 
        format='%(asctime)s: %(levelname)s: %(message)s', 
        datefmt='%d/%m/%Y %I:%M:%S %p', 
        filename=logfile, 
        filemode='a')
#logging.basicConfig(level=logging.DEBUG, filename=logfile, filemode='w')

if __name__ == '__main__':
    logging.debug("Debug info about the program")
    logging.info("Information about the program")
    logging.warning("Warning about the program")

