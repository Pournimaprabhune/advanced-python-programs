import logging
logging.basicConfig(filename='newfile.log',filemode='w',format='%(asctime)s-%(message)s')
logger=logging.getLogger()#create object of logger 
logger.setLevel(logging.DEBUG)
logger.debug("this is a hamrless debug meassage")
logger.warning("this is just an information")
logger.error("you are trying to diveide by zero")
logger.critical("internet is down")
