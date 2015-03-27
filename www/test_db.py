from  models import User,Blog,Comment
from transwarp import db
db.create_engine(user='root',password='root',database='test')
u = User(email='wyqbupt@163.com',name='wyq',password='123456',image='about:blank')
u.insert()
print 'user id is :', u.name
u1 = u.find_first('where email=?','wyqbupt@163.com')
print u1.name
u1.delete()
u2 = u.find_first('where email=?','wyqbupt@163.com')
print 'find user:',u2
