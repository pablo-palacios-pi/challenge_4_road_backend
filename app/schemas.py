from pydantic import BaseModel
from sqlalchemy.orm import declarative_base, sessionmaker,relationship
from sqlalchemy import ForeignKey, String, Integer,Column,create_engine





# clase que representa la tabla generada para sqlalchemy



" CLASES "
class Item_Create(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: int


class Item_(Item_Create):
    id: int


eyes_colors = [
        {
            "name":"Brown"
        },
        {
            "name":"Blue"
        },
        {
            "name":"Green"
        },
        {
            "name":"Hazel"
        },
        {
            "name":"Amber"
        },
        {
            "name":"Violet"
        },
        {
            "name":"Gray"
        },
        {
            "name":"Red"
        },
    ]




" CONEXION BASE DATOS NO RELACIONAL"
#redis_db = redis.Redis(host="localhost",port=6379,db=0, decode_responses=True)


"""" CONEXION CON sqlalchemy """

try:
    engine = create_engine("sqlite:///db_test.sqlite3", echo=True)  
except Exception as e:
        raise Exception(F"ERROR CONEXION BASEDATOS: {e}")
        
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()



class EyeColor(Base):
    
    __tablename__ = 'eyeColor'

    ids = Column(Integer, primary_key=True)
    color = Column(String(50), nullable=False)


class Items_table(Base):
    
    __tablename__ = 'items_table'

    ids = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(100), nullable=False)
    skin_color = Column(String(100), nullable=False)
    eye_color_id = Column(Integer, ForeignKey('eyeColor.ids'))
    eye_color_name = Column(String(100), nullable=False)
    eye_color = relationship('EyeColor')  



def inicio_db():
    try:

        Base.metadata.create_all(engine)

        result = session.query(EyeColor.color).filter(EyeColor.ids==1).first()

        if result is None:
            for eye in eyes_colors:
                name = eye["name"]
                color_ = EyeColor(color=name)
                session.add(color_)
            session.commit()
        elif result[0] == 'Brown':
            pass

    except Exception as e:
        raise Exception(F"ERROR CARGA DE DATOS EN DB: {e}")




""" CONEXION CON LIBRERIA ASINCRONICA """
# import aiomysql
# import asyncio


# try:
#     conn = aiomysql.connect(
#         host="127.0.0.1",
#         user="root",
#         password="",
#         db="test"
#     )

#     cursor = conn.cursor()

# except Exception as e:
#     raise BaseException(e)








