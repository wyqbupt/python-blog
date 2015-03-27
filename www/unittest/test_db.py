import models.models

from transwarp import db
db.create_engine(user='root',password='root',database='test')
u = User(email='wyqbupt@163.com',name='wyq',password='123456',image='about:blank')
u.insert()

