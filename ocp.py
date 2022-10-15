from srp import Logger
import syslog
import sqlite3
from sqlite3 import Error

class ErrorLogger(Logger):
    def WriteLogToFile(self, message):
        with open('log.txt', 'a') as writer:
            writer.write(message + '\n')
            writer.flush()

    def WriteLogToDB(self, message):
        con = sqlite3.connect('./sqldb.db')
        sql = "INSERT INTO ErrorLog(Message) VALUES ('{0}')".format(message)
        con.execute(sql)
        con.commit()

from datetime import datetime
try:
    a = int(input("Enter Value for No1: "))
    b = int(input("Enter Value for No2: "))
    result = a/b
    print(f"{a} / {b} = {result}")
except Exception as ex:
    el = ErrorLogger()
    message = f"From {__file__} Program:\nError: Error Occured while performing calculations \
        please check the inputs\nDate Time: {datetime.now()}\n-------------------"
    el.write_log_to_system(message)
    el.WriteLogToFile(message)
    el.WriteLogToDB(message)
    print(f"Error: {message}")