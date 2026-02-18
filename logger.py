import logging
logging.basicConfig(level=logging.INFO)
logging.log(logging.DEBUG,"LOG DEBUG messge")
logging.log(logging.INFO,"LOG info message")
logging.log(logging.WARNING,'LOG WArning message')
logging.log(logging.ERROR,'This is the error message')


import logging

logging.basicConfig(level=logging.INFO)
######## create the name for logger
logger = logging.getLogger("User2")
logger.info("Thhis is just information of the process")
logger.critical('jjk')
logger1=logging.getLogger("User1")
logger1.error("Error in curr")

import logging
logging.basicConfig(level=logging.INFO)
######create the name for logger
logger = logging.getLogger("MYlogs")
gen_log_file = logging.FileHandler('C:\Users\admin\OneDrive\Desktop/Nature1.txt')
gen_log_file.setLevel(logging.WARNING)
logger.addHandler(gen_log_file)
print("loginpage")
logger.info("This is just information of the process")
logger.critical('jjk')
logger1=logging.getLogger("User1")
logger1.error("Error in curr")
