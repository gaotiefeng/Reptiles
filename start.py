import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from test import testMysql

def start():
    testMysql.testMysql().first()

if __name__ == '__main__':
    start()