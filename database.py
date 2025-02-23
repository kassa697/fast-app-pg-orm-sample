from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL用の接続URL
DB_URL = "postgresql+asyncpg://postgres:jaja0303@localhost:5432/fastapp"

engine = create_async_engine(DB_URL, echo=True)

Base = declarative_base()

db_session = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine,
  class_=AsyncSession
)

async def get_db():
  async with db_session as session:
    yield session