from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker 

from models.base import Base
from models.order import Order
from models.user import User


async_engine = create_async_engine("sqlite+aiosqlite:///database/SQLiteDataBase.db")
SessionLocal = async_sessionmaker(bind = async_engine)

async def get_session():
    async with SessionLocal as session:
        yield session

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)