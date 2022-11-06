from typing import List, Dict, Union

from fastapi import APIRouter, Security, security, Depends, Query
from fastapi.security import HTTPAuthorizationCredentials
from sqlmodel import select
from starlette.responses import JSONResponse
from starlette.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED
from fastapi.encoders import jsonable_encoder
import repos.gem_repository
from endpoints.user_endpoints import auth_handler
#from populate import calculate_gem_latitude
from models.gem_models import *
from db.db import session
from geopy.geocoders import Nominatim


gem_router = APIRouter()


@gem_router.get('/')
def greet():
    return 'Hello please use the link: ' + 'http://127.0.0.1:8000/docs'


@gem_router.get('/gems', tags=['Gems'])
def gems(lte_lat: Optional[int] = None, gte_lat: Optional[int] = None,lte_lon: Optional[int] = None,gte_lon:Optional[int] = None):
    gems = select(Gem)
    if lte_lat:
        gems = gems.where(Gem.latitude <= lte_lat)
    if gte_lat:
        gems = gems.where(Gem.latitude >= gte_lat)

    if lte_lon:
        gems = gems.where(Gem.longitude <= lte_lon)

    if gte_lon:
        gems = gems.where(Gem.longitude >= gte_lon)
    if type:
        gems = gems.order_by(-Gem.latitude).order_by(-Gem.longitude).order_by(None)
    gems = session.exec(gems).all()
    # emp = []
    # for x in gems:
    #     emp.append(list(x)[0])
    # print(emp)
    return {'gems': gems}





@gem_router.post('/gems', tags=['Gems'])
def create_gem(gem: Gem, user=Depends(auth_handler.get_current_user)):
    """Creates Entry"""
    if not user.is_auth:
        return JSONResponse(status_code=HTTP_401_UNAUTHORIZED,content="not authorised")

    loc = Nominatim(user_agent="GetLoc")
 
    # entering the location name
    getLoc = loc.geocode(gem.location)
    
    # printing address
    
    
    # printing latitude and longitude
    

    val_lat = getLoc.latitude
    val_lon = getLoc.longitude

    gem_v = Gem(latitude=val_lat, seller=user,location=gem.location,longitude=val_lon)
    session.add(gem_v)

    session.commit()
    return gem


@gem_router.put('/gems/{id}', response_model=Gem, tags=['Gems'])
def update_gem(id: int, gem: Gem, user=Depends(auth_handler.get_current_user)):
    gem_found = session.get(Gem, id)

    try:
   
        if not user.is_auth:
            return JSONResponse(status_code=HTTP_401_UNAUTHORIZED,content = "not authorized")
        update_item_encoded = jsonable_encoder(gem)
        update_item_encoded.pop('id', None)
        for key, val in update_item_encoded.items():
            gem_found.__setattr__(key, val)
        session.commit()
        return gem_found

    except:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,content="not found")




@gem_router.delete('/gems/{id}', status_code=HTTP_204_NO_CONTENT, tags=['Gems'])
def delete_gem(id:int, user=Depends(auth_handler.get_current_user)):
    gem_found = session.get(Gem, id)
    try:

        if not user.is_auth:
            return JSONResponse(status_code=HTTP_401_UNAUTHORIZED,content="not authorized")


        session.delete(gem_found)
        session.commit()
    except:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,content="not found")


# @gem_router.get('/gems/seller/me', tags=['seller'],
#                 response_model=List[Dict[str, Union[Gem, GemProperties]]])
# def gems_seller(user=Depends(auth_handler.get_current_user)):
#     if not user.is_seller:
#         return JSONResponse(status_code=HTTP_401_UNAUTHORIZED)
#     statement = select(Gem, GemProperties).where(Gem.seller_id == user.id).join(GemProperties)
#     gems = session.exec(statement).all()
#     res = [{'gem': gem, 'props': props} for gem, props in gems]
#     return res