from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from typing import Annotated
from fastapi import Depends

URL_LINK_DB = 'sqlite+aiosqlite:///./application.db'

engine = create_async_engine(url=URL_LINK_DB, echo=True, connect_args={"check_same_thread": False})
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_session():
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]
