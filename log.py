import logging
logging.basicConfig(
	level=logging.DEBUG,
	filename="log.txt",
	format="%(asctime)s->%(levelname)s==>%(message)s")
logging.info("welcome")
a=input("Enter a value:")
logging.info("A value entered")
b=input("enter b value:")
logging.info("b value entered.")
logging.debug("before conversion: a=%s,b=%s"%(a,b))
try:
    a=float(a)
    logging.info("a value converted")
    b=float(b)
    logging.info("b value converted")
    logging.debug("after conversion: a=%s,b=%s"%(a,b))
    res=a/b
    logging.info("result calculated")
    print("ress=%s"%res)
    logging.debug("res=%s"%res)
except ZeroDivisionError as err:
    print("expecting b!=0")
    logging.error("%s,%s"%(err,"expecting b!=0"))
except ValueError as err:
    print("expecting only digits")
    logging.error("%s,%s"%(err,"expecting only digits"))
except Exception as err:
    print("ERROR:",err)
    logging.error("%s"%(err))
logging.info("thank you")