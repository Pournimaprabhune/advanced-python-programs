import logging 
logging.basicConfig(filename='msg.log',filemode='w',format='%(name)s-%(levelname)s-%(message)s')
logging.warning('This wil get logged to a file')