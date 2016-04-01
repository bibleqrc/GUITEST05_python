# -*- coding: UTF-8 -*-
#数据库操作
import ConfigParser
import sys
import MySQLdb

#def connectToDatabase(firstInfo):
cf = ConfigParser.ConfigParser()
cf.read('config.ini')
host = cf.get("db","host")
port = int(cf.get("db","port"))
user = cf.get("db","user")
passwd = cf.get("db","passwd")
db_name = cf.get("db","db")
charset = cf.get("db","charset")
use_unicode = cf.get("db","use_unicode")
try:
    db = MySQLdb.connect(host=host, port=port, user=user, \
                              passwd=passwd, db=db_name, \
                              charset=charset,use_unicode=use_unicode)
    cursor = db.cursor()
except:
    print "Fail to connect to database"
    sys.exit(-1)
print "connet to databse success ..."




def check_zhanghu(N):
    final=0
    sql = 'select gid from one '
    count=cursor.execute(sql)
    results=cursor.fetchall()
    for each in results:
      print each[0] , type(each[0])
      if  N ==str(each[0]):
        final = 1
        break
    if final == 0:
        final = 2

    return final


def check_mima(number,mima):
    final=0
    sql = 'select password from one where gid ='+str(number)
    count=cursor.execute(sql)
    results=cursor.fetchall()
    for each in results:
      print each[0] , type(each[0])
      if  mima ==str(each[0]):
        final = 1
        break
    if final == 0:
        final = 2

    return final


def getmoney(gid):
    sql = 'select money from one where gid ='+str(gid)
    count=cursor.execute(sql)
    result=cursor.fetchall()
    return result[0][0]


def reduce_money(gid,redu):
    m=getmoney(gid)
    print type(m),type(redu)
    m = m-redu
    sql = 'update one set money='+str(m)+" where gid = "+str(gid)
    cursor.execute(sql)
    db.commit()
    print 'reduce successfully'



def add_money(gid ,add):
    m=getmoney(gid)
    m=m+add
    sql = 'update one set money='+str(m)+" where gid = "+str(gid)
    cursor.execute(sql)
    db.commit()
    print 'add successfully'

def changepwd(gid,new_pwd):
    sql = 'update one set password ='+str(new_pwd) +' where gid ='+str(gid)
    cursor.execute(sql)
    db.commit()
    print "change password successfully"

changepwd(95577,95577)

'''
print getmoney(95588)
reduce_money(95588,100)
print getmoney(95588)
add_money(95588,1000)
print getmoney(95588)
#print getbalance(95588)
'''
'''
final = 0
sql = 'select gid from one '
count=cursor.execute(sql)
results=cursor.fetchall()
for each in results:
    print each[0] , type(each[0])
    if '95588'==str(each[0]):
        final = 1
        break
if final == 0:
    final =2

print final

'''


'''
sql = "select * from one"

cout=cursor.execute(sql)
print 'there has %s rows record'%cout

result=cursor.fetchone()
print result

result=cursor.fetchone()
print result

result=cursor.fetchone()
print result

cursor.execute('select gid from one where id = 4 ')
result=cursor.fetchone()
print result[0]

db.commit()
'''