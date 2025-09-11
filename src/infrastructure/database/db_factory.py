from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

def get_engine_and_session(db_url: str):
    engine = create_async_engine(db_url, echo=True)
    session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    return engine, session