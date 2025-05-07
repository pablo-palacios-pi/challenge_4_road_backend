from ast import Await
from fastapi import HTTPException,APIRouter,status
from schemas import Item_Create
from services import add_item_new,get_all_items,get_item_name,delete_item_id, get_all_eye_colors

router = APIRouter()

@router.get("/items/getAll", status_code=status.HTTP_200_OK)
async def get_all_item():
    items = await get_all_items()
    return {"items":items}


@router.get("/items/get/{name}")
async def get_specific_item(name: str):
    
    func = await get_item_name(name) 

    if func is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campo no encontrado en la base de datos")
        
    return {"item": func}

                

@router.post("/items/add", status_code=status.HTTP_201_CREATED)
async def insert_item(data: Item_Create):
    if data is None or data == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Campo vacios")
    else:
        add = await add_item_new(data.name,data.height,data.mass,data.hair_color,
                            data.skin_color,data.eye_color)
        return {"Añadido exitosamente":add}
    

@router.delete("/items/delete/{id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_specifict_item(id: int):
    delete = await delete_item_id(id=id)
    match delete:
        case False:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not found in database")
        case True:
            return {f"Usuario {id} se elimino exitosamente!!"}
        case _:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

@router.get("/items/eyes_colors", status_code=status.HTTP_200_OK)
async def gets_eyes_colors():
    colors = await get_all_eye_colors()
    return colors


