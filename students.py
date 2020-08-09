import pymysql

#获取数据库配置
db = pymysql.connect(
    host='localhost',
    database='stu_info',  #库名
    user='root',
    password='021026',
    port=3306,
    charset='utf8'
    )

#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

#使用execute()方法执行sql,如果表存在则删除
cursor.execute("drop table if exists students")

#执行sql处理语句创建表
sql_students = """create table students(
ID int(8) primary key auto_increment,
Name varchar(20) not null,
Grade float)ENGINE=InnoDB DEFAULT CHARSET=utf8"""

#创建
cursor.execute(sql_students)

#关闭数据库,无论对数据库如何操作,都要关闭数据库,防止出错
db.close()

db = pymysql.connect(
    host='localhost',
    database='stu_info',  #库名
    user='root',
    password='021026',
    port=3306,
    charset='utf8'
    )

#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
sql_Course = "alter table students add Course varchar(50) after Name"
cursor.execute(sql_Course)
cursor.close()
db.close()

db = pymysql.connect(
    host='localhost',
    database='stu_info',  #库名
    user='root',
    password='021026',
    port=3306,
    charset='utf8'
    )
cursor = db.cursor()
sql = "INSERT INTO students(ID,Name,Course,Grade) VALUES(%s,%s,%s,%s)"
params = (('00128','zhang','Comp.sci',102),('12345','Shankar','Comp.sci',82))
try:
    cursor.executemany(sql,params)
    db.commit()
    print("插入数据成功")
except Exception as e:
    print("插入数据失败：case%s"%e)
    # 如果发生错误则回滚
    db.rollback()
finally:
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    db.close()


 
