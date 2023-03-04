from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func
from sqlalchemy import select, insert
from database import get_async_session
from db.models import City, Weather
from .schemas import CitySchema, WeatherSchema

router = APIRouter(prefix="", tags=["Weather"])


@router.get("/cities/")
async def get_cities(session: AsyncSession = Depends(get_async_session)):
    stmt = select(City)
    result = await session.execute(stmt)
    # print(result.scalars())
    # return CitySchema(name="some city")
    return result.scalars().all()


@router.post("/weather/{city_name}")
async def add_city(city_name: str, session: AsyncSession = Depends(get_async_session)):
    # TODO: добавить проверку, что город есть в openweathermap
    stmt = insert(City).values(name=city_name)
    result = await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
