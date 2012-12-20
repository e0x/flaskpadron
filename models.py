#from sqlalchemy import *
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import create_session
#import sys
#from flaskext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
app.config.from_pyfile('padron.cfg')
db = SQLAlchemy(app)
#reload(sys)
#sys.setdefaultencoding('ISO-8859-1')
#Base = declarative_base()
#engine = create_engine('mysql://root@localhost/drpadron')
#metadata = MetaData(bind=engine)
#metadata.bind = engine

#padron_table = Table('padron', metadata, mysql_charset='utf8', autoload=True)

class Padron(db.Model):
	__table__ = Table('padron', metadata, autoload=True)


#session = create_session(bind=engine)

#padron = session.query(Padron)

#for rs in padron.filter(Padron.nombre.like('ceu%')).all():
#	print type(rs)
#	print rs.nombre, rs.apellido, rs.cedula, rs.fecha_nacimiento

