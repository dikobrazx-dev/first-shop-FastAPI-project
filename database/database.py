from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import event

from models.base import Base
from models.order import Order
from models.user import User
from models.product import Product
from models.order_item import OrderItem

async_engine = create_async_engine("sqlite+aiosqlite:///database/SQLiteDataBase.db")


@event.listens_for(async_engine.sync_engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")


SessionLocal = async_sessionmaker(bind = async_engine)

async def get_session():
    async with SessionLocal() as session:
        yield session

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)