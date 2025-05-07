# VIEWS

from faker import Faker
from schemas import EyeColor, Item_, session,Items_table

faker = Faker()

async def add_item_new(name: str, height: int, mass: int, hair_color: str, skin_color: str, eye_color_id: int):
    name = name.lower()
    uuid = faker.random_number(digits=2)

    color_share = session.query(EyeColor.color).filter(EyeColor.ids==eye_color_id).first()
    

    if color_share is None:
        raise Exception("NO existe el id eye color")
    else:
        for color in color_share:
            c = color
        
        session.add(Items_table(ids = uuid,name=name,height=height,mass=mass,hair_color=hair_color,skin_color=skin_color,eye_color_name=c,eye_color_id=eye_color_id))
        session.commit()     

        item = Item_(id=uuid,
                    name=name,
                    height=height,
                    mass=mass,
                    hair_color=hair_color,
                    skin_color=skin_color,
                    eye_color=eye_color_id)    
        
        return item


async def get_all_items():
    query = session.query(Items_table).all()
    data = []
    for g in query:
        item = {
            "id":g.ids,
            "name":g.name,
            "height":g.height,
            "mass":g.mass,
            "hair_color":g.hair_color,
            "skin_color":g.skin_color,
            "eye_color":g.eye_color
        }
        data.append(item)

    return data


async def get_item_name(name: str):
    name = name.lower()
    gets = session.query(Items_table).filter(Items_table.name==name).first()
    
    match gets:
        case None:
            item = None
        case _:
            
                item = {
                        "id":gets.ids,
                        "name":gets.name,
                        "height":gets.height,
                        "mass":gets.mass,
                        "hair_color":gets.hair_color,
                        "skin_color":gets.skin_color,
                        "eye_color":gets.eye_color_id
                    }
    
    return item


async def delete_item_id(id: int):

    resp = False
    item = session.query(Items_table).filter(Items_table.ids==id).first()

    if item is not None:
        session.delete(item)
        session.commit()
        resp = True

    return resp




async def get_all_eye_colors():
    colors = session.query(EyeColor).all()

    lista_colors = []
    
    for c in colors:
        colors_ = {
            "id":c.ids,
            "color":c.color
        }

        lista_colors.append(colors_)

    return lista_colors





